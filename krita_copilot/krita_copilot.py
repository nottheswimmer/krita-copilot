import base64
import json
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from PyQt5.QtCore import Qt, QByteArray, QBuffer, QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QScrollArea, \
    QToolButton, QLineEdit, QMessageBox, QCheckBox, QHBoxLayout

from .dependencies import ensure_dependencies, APP_DIR

VERSION = "v1.0.2"

ensure_dependencies()


def set_key_value(key, value):
    kv_path = APP_DIR / f"{key}.setting"
    with open(kv_path, "w") as f:
        json.dump(value, f)


def get_key_value(key, default=None):
    kv_path = APP_DIR / f"{key}.setting"
    if kv_path.exists():
        with open(kv_path, "r") as f:
            return json.load(f)
    else:
        return default


from pydalle import Dalle

try:
    from krita import Krita, DockWidget, DockWidgetFactory, DockWidgetFactoryBase
except ImportError:
    from fake_krita import Krita as FakeKrita, \
        DockWidget as FakeDockWidget, \
        DockWidgetFactory as FakeDockWidgetFactory, \
        DockWidgetFactoryBase as FakeDockWidgetFactoryBase


    class Krita(FakeKrita):
        @classmethod
        def krita_i18n(cls, s):
            return s


    class DockWidget(QWidget, FakeDockWidget):
        def setWindowTitle(self, title):
            pass

        def setWidget(self, widget):
            pass


    class DockWidgetFactory(FakeDockWidgetFactory):
        def __init__(self, *args, **kwargs):
            pass


    class DockWidgetFactoryBase(FakeDockWidgetFactoryBase):
        DockRight = None

KI = Krita.instance()


def get_image_png_base64(image: QImage) -> str:
    # the image has to be 1024x1024 for krita_copilot to accept it
    if image.width() != 1024 or image.height() != 1024:
        image = image.scaled(1024, 1024, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    ba = QByteArray()
    buf = QBuffer(ba)
    buf.open(QBuffer.WriteOnly)
    image.save(buf, 'PNG')
    png_base64 = base64.b64encode(ba.data()).decode('utf-8')
    return png_base64


class DalleMonitor(QObject):
    # login_out_signal emits (success, credits, message)
    login_out_signal = pyqtSignal(bool, int, str)

    # credit_out_signal emits (credits)
    credit_out_signal = pyqtSignal(int)

    # login_in_signal emits (username, password)
    login_in_signal = pyqtSignal(str, str)

    # edit_task_in_signal emits (prompt, w, h, x, y, selection_image, direct)
    edit_task_in_signal = pyqtSignal(str, int, int, int, int, QImage, bool)

    # create_task_in_signal emits (prompt, w, h, x, y, direct)
    create_task_in_signal = pyqtSignal(str, int, int, int, int, bool)

    # variation_task_in_signal emits (w, h, x, y, selection_image, direct)
    variation_task_in_signal = pyqtSignal(int, int, int, int, QImage, bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dalle = None
        self.login_in_signal.connect(self.on_login)
        self.edit_task_in_signal.connect(self.on_edit)
        self.create_task_in_signal.connect(self.on_create)
        self.variation_task_in_signal.connect(self.on_variation)

    @pyqtSlot(str, str)
    def on_login(self, username, password):
        self.dalle = Dalle(username, password)
        try:
            summary = self.dalle.get_credit_summary()
            self.login_out_signal.emit(True, summary.aggregate_credits, "")
        except Exception as e:
            self.login_out_signal.emit(False, -1, str(e))

    def emit_credit(self):
        if self.dalle is not None:
            summary = self.dalle.get_credit_summary()
            self.credit_out_signal.emit(summary.aggregate_credits)

    def on_edit(self, prompt, w, h, x, y, selection_image: QImage, direct: bool):
        selection_base64 = get_image_png_base64(selection_image)
        try:
            task = self.dalle.create_inpainting_task(prompt, selection_base64)
            self.paste_task_results(task, w, h, x, y, f"Edit ~ {prompt}", direct)
        finally:
            self.emit_credit()

    def on_create(self, prompt, w, h, x, y, direct: bool):
        try:
            task = self.dalle.create_text2im_task(prompt)
            self.paste_task_results(task, w, h, x, y, f"Create ~ {prompt}", direct)
        finally:
            self.emit_credit()

    def on_variation(self, w, h, x, y, selection_image: QImage, direct: bool):
        selection_base64 = get_image_png_base64(selection_image)
        try:
            task = self.dalle.create_variations_task(selection_base64)
            self.paste_task_results(task, w, h, x, y, "Variation", direct)
        finally:
            self.emit_credit()

    def paste_task_results(self, task, w, h, x, y, extra_layer_text, direct=True):
        doc = KI.activeDocument()
        task = task.wait()
        if not task.status == "succeeded":
            return

        task_paths = []

        if direct:
            ext = "webp"
        else:
            ext = "png"

        def process_generation(generation):
            task_path = APP_DIR / "generations" / f"{task.id}_{generation.id}.{ext}"
            task_path.parent.mkdir(parents=True, exist_ok=True)
            with open(task_path.as_posix(), "wb") as f:
                f.write(generation.download(direct=direct).wrapped)
            task_paths.append(task_path)

        with ThreadPoolExecutor(max_workers=len(task.generations)) as executor:
            executor.map(process_generation, task.generations)

        new_nodes = []
        for i, task_path in enumerate(task_paths):
            img = QImage(task_path.as_posix())
            m = max(w, h)
            img = img.scaled(m, m, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            task_path_cropped = task_path.parent / f"{task_path.stem}_cropped.png"
            img.save(task_path_cropped.as_posix(), 'PNG')

            title = f"[{i}] {extra_layer_text}"
            new_node = doc.createFileLayer(title, task_path_cropped.as_posix(), "None")

            new_node.move(x, y)
            new_nodes.append(new_node)

        root = doc.rootNode()
        for node in new_nodes:
            root.addChildNode(node, None)


class DalleApp(DockWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(Krita.krita_i18n("Krita Copilot ({})").format(VERSION))

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Add a thread
        self.thread = QThread()
        self.thread.start()

        # Add a worker
        self.worker = DalleMonitor()
        self.worker.moveToThread(self.thread)

        # Add preview
        self.previewContainer = QWidget()
        layout.addWidget(self.previewContainer)
        self.previewContainer.setContentsMargins(0, 0, 0, 0)
        previewContainerLayout = QHBoxLayout()
        previewContainerLayout.setContentsMargins(0, 0, 0, 0)
        previewContainerLayout.setSpacing(0)
        self.previewContainer.setLayout(previewContainerLayout)
        self.scrollArea = QScrollArea()
        previewContainerLayout.addWidget(self.scrollArea)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.previewLabel = QLabel()
        self.scrollArea.setWidget(self.previewLabel)

        # Add buttons
        self.buttonLayout = QHBoxLayout()
        layout.addLayout(self.buttonLayout)
        self.buttonLayout.setAlignment(Qt.AlignLeft)

        # Add a username and password field
        self.usernameLabel = QLabel(Krita.krita_i18n("Username:"))
        self.usernameLineEdit = QLineEdit(get_key_value("username", ""))
        self.usernameLineEdit.textChanged.connect(self.usernameChanged)
        self.passwordLabel = QLabel(Krita.krita_i18n("Password:"))
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.buttonLayout.addWidget(self.usernameLabel)
        self.buttonLayout.addWidget(self.usernameLineEdit)
        self.buttonLayout.addWidget(self.passwordLabel)
        self.buttonLayout.addWidget(self.passwordLineEdit)

        # Add a button to login
        self.loginButton = QToolButton()
        self.loginButton.setText(Krita.krita_i18n("Login"))
        self.loginButton.clicked.connect(self.login)
        self.buttonLayout.addWidget(self.loginButton)

        # -- Logged in functionality --

        # Add a tracker for the number of credits available. Default to ?.
        self.creditsLabel = QLabel()
        self.creditsLabel.setText(Krita.krita_i18n("Credits: {}").format("?"))
        self.creditsLabel.setVisible(False)
        self.buttonLayout.addWidget(self.creditsLabel)

        # Add checkbox for whether to include a watermark
        self.watermarkCheckBox = QCheckBox(Krita.krita_i18n("Mark"))
        self.watermarkCheckBox.setChecked(get_key_value("watermark", True))
        self.watermarkCheckBox.stateChanged.connect(self.watermarkChanged)
        self.buttonLayout.addWidget(self.watermarkCheckBox)
        self.watermarkCheckBox.setVisible(False)

        # Add prompt input
        self.promptLabel = QLabel()
        self.promptLabel.setText(Krita.krita_i18n("Prompt:"))
        self.promptLabel.setVisible(False)
        self.promptLineEdit = QLineEdit(get_key_value("prompt", ""))
        self.promptLineEdit.setVisible(False)
        self.promptLineEdit.textChanged.connect(self.promptChanged)
        self.buttonLayout.addWidget(self.promptLabel)
        self.buttonLayout.addWidget(self.promptLineEdit)

        # Add button to create
        self.createButton = QToolButton()
        self.createButton.setText(Krita.krita_i18n("Create"))
        self.createButton.clicked.connect(self.create_with_prompt)
        self.createButton.setVisible(False)
        self.buttonLayout.addWidget(self.createButton)

        # Add a button to edit the selection
        self.editButton = QToolButton()
        self.editButton.setText(Krita.krita_i18n("Inpaint"))
        self.editButton.clicked.connect(self.edit_selection_with_prompt)
        self.editButton.setVisible(False)
        self.buttonLayout.addWidget(self.editButton)

        # Add a button to create a variation of the selection
        self.variationButton = QToolButton()
        self.variationButton.setText(Krita.krita_i18n("Variate"))
        self.variationButton.clicked.connect(self.variate_selection)
        self.variationButton.setVisible(False)
        self.buttonLayout.addWidget(self.variationButton)

        # Add worker signals
        self.worker.login_out_signal.connect(self.on_login_done)
        self.worker.credit_out_signal.connect(self.on_update_credits_done)

        # Add tooltips to all the buttons
        self.loginButton.setToolTip(Krita.krita_i18n("Login with your OpenAI account"))
        self.createButton.setToolTip(Krita.krita_i18n("Create a new image in the selected area with your prompt"))
        self.editButton.setToolTip(Krita.krita_i18n("Inpaint the transparent areas of the selection with your prompt"))
        self.variationButton.setToolTip(Krita.krita_i18n("Create a variation of the selected area, prompt is not used"))
        self.watermarkCheckBox.setToolTip(Krita.krita_i18n("Mark the image with a DALL-E 2 watermark"))
        self.promptLineEdit.setToolTip(Krita.krita_i18n("The prompt to use for creating and inpainting"))
        self.usernameLineEdit.setToolTip(Krita.krita_i18n("Your OpenAI username"))
        self.passwordLineEdit.setToolTip(Krita.krita_i18n("Your OpenAI password"))
        self.previewLabel.setToolTip(Krita.krita_i18n("Preview of the selected area. "
                                                      "It will be a bit larger if you did not select a perfect square"))
        self.scrollArea.setToolTip(Krita.krita_i18n("The selected area"))
        self.creditsLabel.setToolTip(
            Krita.krita_i18n("The number of credits you have available. Updated after each create/inpaint/variation"))
        self.promptLabel.setToolTip(Krita.krita_i18n("The prompt to use for creating and inpainting"))
        self.usernameLabel.setToolTip(Krita.krita_i18n("Your OpenAI username"))
        self.passwordLabel.setToolTip(Krita.krita_i18n("Your OpenAI password"))

        # Main layout
        mainWidget = QWidget(self)
        mainWidget.setLayout(layout)
        self.setWidget(mainWidget)

        self.startTimer(500)  # refresh twice a second

    def get_preview_size(self):
        return (
            self.previewContainer.contentsRect().width() - self.scrollArea.contentsMargins().top() * 2,
            self.previewContainer.contentsRect().height() - self.scrollArea.contentsMargins().top() * 2
        )

    def get_selection(self):
        doc = KI.activeDocument()
        if doc is None:
            return None
        return doc.selection()

    def get_selection_image(self) -> Optional[QImage]:
        doc = KI.activeDocument()
        if doc is None:
            return None
        sel = doc.selection()
        if not sel:
            return None
        m = max(sel.width(), sel.height())
        return doc.projection(sel.x(), sel.y(), m, m)

    def scale_selection_size(self, w, h, scale):
        selection = self.get_selection()
        if selection is None:
            return (w * scale, h * scale)
        selection_width = selection.width()
        selection_height = selection.height()
        return (int(selection_width * scale), int(selection_height * scale))

    def login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        if not username or not password:
            QMessageBox.warning(self, Krita.krita_i18n("Login"),
                                Krita.krita_i18n("Please enter a username and password."))
            return
        self.worker.login_in_signal.emit(username, password)

        # Disable the login button until the login is done.
        self.loginButton.setEnabled(False)

    def on_login_done(self, success: bool, credits: int, message: str):
        if success:
            self.creditsLabel.setText(Krita.krita_i18n("Credits: {}").format(credits))

            # Remove the login form
            self.usernameLabel.setVisible(False)
            self.usernameLineEdit.setVisible(False)
            self.passwordLabel.setVisible(False)
            self.passwordLineEdit.setVisible(False)
            self.loginButton.setVisible(False)

            # Enable the logged in functionality
            self.creditsLabel.setVisible(True)
            self.promptLabel.setVisible(True)
            self.promptLineEdit.setVisible(True)
            self.editButton.setVisible(True)
            self.createButton.setVisible(True)
            self.variationButton.setVisible(True)
            self.watermarkCheckBox.setVisible(True)
        else:
            # Re-enable the login button
            self.loginButton.setEnabled(True)
            QMessageBox.warning(self, Krita.krita_i18n("Login"),
                                Krita.krita_i18n("Login failed: {}").format(message))

    def on_update_credits_done(self, credits):
        self.creditsLabel.setText(Krita.krita_i18n("Credits: {}").format(credits))

    def create_with_prompt(self):
        selection = self.get_selection()
        if not selection:
            QMessageBox.warning(self, Krita.krita_i18n("Edit"),
                                Krita.krita_i18n("Edit failed: No selection."))
            return
        prompt = self.promptLineEdit.text()
        if not prompt:
            QMessageBox.warning(self, Krita.krita_i18n("Edit"),
                                Krita.krita_i18n("Edit failed: No prompt."))
            return
        w = selection.width()
        h = selection.height()
        x = selection.x()
        y = selection.y()
        self.worker.create_task_in_signal.emit(prompt, w, h, x, y, not self.watermarkCheckBox.isChecked())

    def edit_selection_with_prompt(self):
        selection = self.get_selection()
        selection_image = self.get_selection_image()
        if not selection or not selection_image:
            QMessageBox.warning(self, Krita.krita_i18n("Create"),
                                Krita.krita_i18n("Create failed: No selection."))
            return
        prompt = self.promptLineEdit.text()
        if not prompt:
            QMessageBox.warning(self, Krita.krita_i18n("Create"),
                                Krita.krita_i18n("Create failed: No prompt."))
            return
        w = selection.width()
        h = selection.height()
        x = selection.x()
        y = selection.y()
        self.worker.edit_task_in_signal.emit(prompt, w, h, x, y, selection_image,
                                             not self.watermarkCheckBox.isChecked())

    def variate_selection(self):
        selection = self.get_selection()
        selection_image = self.get_selection_image()
        if not selection or not selection_image:
            QMessageBox.warning(self, Krita.krita_i18n("Create"),
                                Krita.krita_i18n("Create failed: No selection."))
            return
        w = selection.width()
        h = selection.height()
        x = selection.x()
        y = selection.y()
        self.worker.variation_task_in_signal.emit(w, h, x, y, selection_image, not self.watermarkCheckBox.isChecked())

    def usernameChanged(self, username):
        set_key_value("username", username)

    def promptChanged(self, prompt):
        set_key_value("prompt", prompt)

    def watermarkChanged(self, watermark):
        set_key_value("watermark", watermark)

    def canvasChanged(self, canvas):
        self.refresh()

    def timerEvent(self, event):
        self.refresh()

    def resizeEvent(self, event):
        self.refresh()

    def refresh(self):
        doc = KI.activeDocument()

        # return if no document is open
        if doc is None:
            self.setDisabled(True)
            self.previewLabel.setPixmap(QPixmap())
            return

        self.setDisabled(False)

        # get current drawing
        sel = doc.selection()
        if not sel:
            return

        m = max(sel.width(), sel.height())

        # The preview image is a square
        previewImage = doc.projection(sel.x(), sel.y(), m, m)

        # scale images
        width, height = self.get_preview_size()
        previewImage = previewImage.scaled(width, height, Qt.KeepAspectRatio, Qt.FastTransformation)

        # merge images
        resultImage = QImage(previewImage.width(), previewImage.height(), QImage.Format_ARGB32_Premultiplied)
        resultImage.fill(0)
        painter = QPainter(resultImage)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.drawImage(0, 0, previewImage)
        painter.end()

        self.previewLabel.setPixmap(QPixmap.fromImage(resultImage))

        self.scrollArea.setMaximumSize(previewImage.width() + 4, previewImage.height() + 4)


KI.addDockWidgetFactory(DockWidgetFactory("krita_copilot", DockWidgetFactoryBase.DockRight, DalleApp))
