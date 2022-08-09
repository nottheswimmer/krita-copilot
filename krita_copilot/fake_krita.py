# Auto-generated file that reads from H files in the libkis folder
# The purpose is to use as auto-complete in Python IDEs

# auto-generated from: Resource.h
from typing import List

from PyQt5.QtCore import QByteArray, QObject
from PyQt5.QtGui import QImage


class Resource:
    """ A Resource represents a gradient, pattern, brush tip, brush preset, palette or
    workspace definition.

    @code
    allPresets = Application.resources("preset")
    for preset in allPresets:
        print(preset.name())
    @endcode

    Resources are identified by their type, name and filename. If you want to change
    the contents of a resource, you should read its data using data(), parse it and
    write the changed contents back.
       """

    @staticmethod
    def Resource(KoResource, QObject):
        """Return Type: void
        Missing function documentation"""

    @staticmethod
    def type():
        """Return Type: QString
        Return the type of this resource. Valid types are: <ul> <li>pattern: a raster image representing a pattern <li>gradient: a gradient <li>brush: a brush tip <li>preset: a brush preset <li>palette: a color set <li>workspace: a workspace definition. </ul>"""

    @staticmethod
    def name():
        """Return Type: QString
        The user-visible name of the resource."""

    @staticmethod
    def setName(QString):
        """Return Type: void
        setName changes the user-visible name of the current resource."""

    @staticmethod
    def filename():
        """Return Type: QString
        The filename of the resource, if present. Not all resources are loaded from files."""

    @staticmethod
    def image() -> QImage:
        """Return Type: QImage
        An image that can be used to represent the resource in the user interface. For some resources, like patterns, the image is identical to the resource, for others it's a mere icon."""

    @staticmethod
    def setImage(pq: QImage):
        """Return Type: void
        Change the image for this resource."""

    @staticmethod
    def data():
        """Return Type: QByteArray
        Return the resource as a byte array."""

    @staticmethod
    def setData(QByteArray):
        """Return Type: bool
        Change the internal data of the resource to the given byte array. If the byte array is not valid, setData returns false, otherwwise true."""

    @staticmethod
    def resource():
        """Return Type: KoResource
        Change the internal data of the resource to the given byte array. If the byte array is not valid, setData returns false, otherwwise true./bool setData(QByteArray data);private:friend class PresetChooser;"""

    # auto-generated from: Notifier.h


class Notifier:
    """ The Notifier can be used to be informed of state changes in the Krita application.
       """

    @staticmethod
    def Notifier(QObject):
        """Return Type: void
        The Notifier can be used to be informed of state changes in the Krita application./class KRITALIBKIS_EXPORT Notifier : public QObject{Q_OBJECTQ_DISABLE_COPY(Notifier)Q_PROPERTY(bool Active READ active WRITE setActive)"""

    @staticmethod
    def active():
        """Return Type: bool
        @return true if the Notifier is active."""

    @staticmethod
    def setActive(bool):
        """Return Type: void
        Enable or disable the Notifier"""

    @staticmethod
    def applicationClosing():
        """Return Type: void
        @brief applicationClosing is emitted when the application is about to close. This happens after any documents and windows are closed."""

    @staticmethod
    def imageCreated(Document):
        """Return Type: void
        @brief imageCreated is emitted whenever a new image is created and registered with the application."""

    @staticmethod
    def imageSaved(QString):
        """Return Type: void
        @brief imageSaved is emitted whenever a document is saved. @param filename the filename of the document that has been saved."""

    @staticmethod
    def imageClosed(QString):
        """Return Type: void
        @brief imageClosed is emitted whenever the last view on an image is closed. The image does not exist anymore in Krita @param filename the filename of the image."""

    @staticmethod
    def viewCreated(View):
        """Return Type: void
        @brief viewCreated is emitted whenever a new view is created. @param view the view"""

    @staticmethod
    def viewClosed(View):
        """Return Type: void
        @brief viewClosed is emitted whenever a view is closed @param view the view"""

    @staticmethod
    def windowCreated(Window):
        """Return Type: void
        @brief windowCreated is emitted whenever a window is created @param window the window"""

    @staticmethod
    def configurationChanged():
        """Return Type: void
        @brief configurationChanged is emitted every time Krita's configuration has changed."""

    @staticmethod
    def imageCreated(KisDocument):
        """Return Type: void
        @brief configurationChanged is emitted every time Krita's configuration has changed./void configurationChanged();private Q_SLOTS:"""

    @staticmethod
    def viewCreated(KisView):
        """Return Type: void
        @brief configurationChanged is emitted every time Krita's configuration has changed./void configurationChanged();private Q_SLOTS:void imageCreated(KisDocument document);"""

    @staticmethod
    def viewClosed(KisView):
        """Return Type: void
        @brief configurationChanged is emitted every time Krita's configuration has changed./void configurationChanged();private Q_SLOTS:void imageCreated(KisDocument document);"""

    @staticmethod
    def windowCreated(KisMainWindow):
        """Return Type: void
        @brief configurationChanged is emitted every time Krita's configuration has changed./void configurationChanged();private Q_SLOTS:void imageCreated(KisDocument document);void viewCreated(KisView view);void viewClosed(KisView view);"""

    # auto-generated from: Document.h


class Document:
    """ The Document class encapsulates a Krita Document/Image. A Krita document is an Image with
    a filename. Libkis does not differentiate between a document and an image, like Krita does
    internally.
       """

    @staticmethod
    def Document(KisDocument, QObject):
        """Return Type: void
        The Document class encapsulates a Krita Document/Image. A Krita document is an Image with a filename. Libkis does not differentiate between a document and an image, like Krita does internally./class KRITALIBKIS_EXPORT Document : public QObject{Q_OBJECTQ_DISABLE_COPY(Document)"""

    @staticmethod
    def batchmode():
        """Return Type: bool
        Batchmode means that no actions on the document should show dialogs or popups. @return true if the document is in batchmode."""

    @staticmethod
    def setBatchmode(bool):
        """Return Type: void
        Set batchmode to @param value. If batchmode is true, then there should be no popups or dialogs shown to the user."""

    @staticmethod
    def activeNode() -> 'Node':
        """Return Type: Node
        @brief activeNode retrieve the node that is currently active in the currently active window @return the active node. If there is no active window, the first child node is returned."""

    @staticmethod
    def setActiveNode(Node):
        """Return Type: void
        @brief setActiveNode make the given node active in the currently active view and window @param value the node to make active."""

    @staticmethod
    def topLevelNodes():
        """Return Type: QList<Node>
        @brief toplevelNodes return a list with all top level nodes in the image graph"""

    @staticmethod
    def nodeByName(QString) -> 'Node':
        """Return Type: Node
        @brief nodeByName searches the node tree for a node with the given name and returns it @param name the name of the node @return the first node with the given name or 0 if no node is found"""

    @staticmethod
    def colorDepth():
        """Return Type: QString
        colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul> @return the color depth."""

    @staticmethod
    def colorModel():
        """Return Type: QString
        @brief colorModel retrieve the current color model of this document: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul> @return the internal color model string."""

    @staticmethod
    def colorProfile():
        """Return Type: QString
        @return the name of the current color profile"""

    @staticmethod
    def setColorProfile(QString):
        """Return Type: bool
        @brief setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is <i>not</i> converted. @param colorProfile @return false if the colorProfile name does not correspond to to a registered profile or if assigning the profile failed."""

    @staticmethod
    def setColorSpace(s1: str, s2: str, s3: str):
        """Return Type: bool
        Missing function documentation"""

    @staticmethod
    def documentInfo():
        """Return Type: QString
        Missing function documentation"""

    @staticmethod
    def setDocumentInfo(QString):
        """Return Type: void
        @brief setDocumentInfo set the Document information to the information contained in document @param document A string containing a valid XML document that conforms to the document-info DTD that can be found here: https://phabricator.kde.org/source/krita/browse/master/krita/dtd/"""

    @staticmethod
    def fileName():
        """Return Type: QString
        @return the full path to the document, if it has been set."""

    @staticmethod
    def setFileName(QString):
        """Return Type: void
        @brief setFileName set the full path of the document to @param value"""

    @staticmethod
    def height():
        """Return Type: int
        @return the height of the image in pixels"""

    @staticmethod
    def setHeight(int):
        """Return Type: void
        @brief setHeight resize the document to @param value height. This is a canvas resize, not a scale."""

    @staticmethod
    def name():
        """Return Type: QString
        @return the name of the document. This is the title field in the @see documentInfo"""

    @staticmethod
    def setName(QString):
        """Return Type: void
        @brief setName sets the name of the document to @param value. This is the title field in the @see documentInfo"""

    @staticmethod
    def resolution():
        """Return Type: int
        @return the resolution in pixels per inch"""

    @staticmethod
    def setResolution(int):
        """Return Type: void
        @brief setResolution set the resolution of the image; this does not scale the image @param value the resolution in pixels per inch"""

    @staticmethod
    def rootNode() -> 'Node':
        """Return Type: Node
        @brief rootNode the root node is the invisible group layer that contains the entire node hierarchy. @return the root of the image"""

    @staticmethod
    def selection() -> 'Selection':
        """Return Type: Selection
        @brief selection Create a Selection object around the global selection, if there is one. @return the global selection or None if there is no global selection."""

    @staticmethod
    def setSelection(s: 'Selection'):
        """Return Type: void
        @brief setSelection set or replace the global selection @param value a valid selection object."""

    @staticmethod
    def width() -> int:
        """Return Type: int
        @return the width of the image in pixels."""

    @staticmethod
    def setWidth(p1: int):
        """Return Type: void
        @brief setWidth resize the document to @param value width. This is a canvas resize, not a scale."""

    @staticmethod
    def xRes() -> float:
        """Return Type: double
        @return xRes the horizontal resolution of the image in pixels per pt (there are 72 pts to an inch)"""

    @staticmethod
    def setXRes(double: float):
        """Return Type: void
        @brief setXRes set the horizontal resolution of the image to xRes in pixels per pt. (there are 72 pts to an inch)"""

    @staticmethod
    def yRes() -> float:
        """Return Type: double
        @return yRes the vertical resolution of the image in pixels per pt (there are 72 pts to an inch)"""

    @staticmethod
    def setYRes(double: float):
        """Return Type: void
        @brief setYRes set the vertical resolution of the image to yRes in pixels per pt. (there are 72 pts to an inch)"""

    @staticmethod
    def pixelData(a: int, b: int, c: int, d: int, /):
        """Return Type: QByteArray
        Missing function documentation"""

    @staticmethod
    def close():
        """Return Type: bool
        @brief close Close the document: remove it from Krita's internal list of documents and close all views. If the document is modified, you should save it first. There will be no prompt for saving. @return true if the document is closed."""

    @staticmethod
    def crop(a: int, b: int, c: int, d: int, /):
        """Return Type: void
        @brief crop the image to rectangle described by @param x, @param y, @param w and @param h"""

    @staticmethod
    def exportImage(QString, InfoObject):
        """Return Type: bool
        @brief exportImage export the image, without changing its URL to the given path. @param filename the full path to which the image is to be saved @param exportConfiguration a configuration object appropriate to the file format @return true if the export succeeded, false if it failed."""

    @staticmethod
    def flatten():
        """Return Type: void
        @brief flatten all layers in the image"""

    @staticmethod
    def resizeImage(a: int, b: int):
        """Return Type: void
        @brief resizeImage resize the image to the given width and height. @param w the new width @param h the new height"""

    @staticmethod
    def save():
        """Return Type: bool
        @brief save the image to its currently set path. The modified flag of the document will be reset @return true if saving succeeded, false otherwise."""

    @staticmethod
    def saveAs(QString):
        """Return Type: bool
        @brief saveAs save the document under the @param filename. The document's filename will be reset to @param filename. @param filename the new filename (full path) for the document @return true if saving succeeded, false otherwise."""

    @staticmethod
    def createNode(s1: str, s2: str) -> "Node":
        """Return Type: Node
        Missing function documentation"""

    @staticmethod
    def projection(a: int, b: int, c: int, d: int, /) -> QImage:
        """Return Type: QImage
        @brief projection creates a QImage from the rendered image or a cutout rectangle."""

    @staticmethod
    def thumbnail(a: int, b: int) -> QImage:
        """Return Type: QImage
        @brief thumbnail create a thumbnail of the given dimensions. If the requested size is too big a null QImage is created. @return a QImage representing the layer contents."""

    @staticmethod
    def lock():
        """Return Type: void
        Why this should be used, When it should be used, How it should be used, and warnings about when not."""

    @staticmethod
    def unlock():
        """Return Type: void
        Why this should be used, When it should be used, How it should be used, and warnings about when not."""

    @staticmethod
    def waitForDone():
        """Return Type: void
        Why this should be used, When it should be used, How it should be used, and warnings about when not."""

    @staticmethod
    def tryBarrierLock():
        """Return Type: bool
        Why this should be used, When it should be used, How it should be used, and warnings about when not."""

    @staticmethod
    def isIdle():
        """Return Type: bool
        Why this should be used, When it should be used, How it should be used, and warnings about when not."""

    @staticmethod
    def refreshProjection():
        """Return Type: void
        Starts a synchronous recomposition of the projection: everything will wait until the image is fully recomputed."""

    @staticmethod
    def document():
        """Return Type: QPointer<KisDocument>
        Starts a synchronous recomposition of the projection: everything will wait until the image is fully recomputed./void refreshProjection();private:friend class Krita;friend class Window;"""

    #	createFileLayer (const QString &name, const QString fileName, const QString scalingMethod)
    @staticmethod
    def createFileLayer(name: str, fileName: str, scalingMethod: str) -> "Node":
        """Return Type: Layer
        @brief createFileLayer create a new layer from a file @param name the name of the layer @param fileName the name of the file @param scalingMethod the scaling method to use when loading the file @return a new layer, or 0 if the layer could not be created."""



# auto-generated from: Krita.h
class Krita:
    """ Krita is a singleton class that offers the root access to the Krita object hierarchy.

    The Krita.instance() is aliased as two builtins: Scripter and Application.
       """

    @staticmethod
    def Krita(QObject):
        """Return Type: void
        Krita is a singleton class that offers the root access to the Krita object hierarchy. The Krita.instance() is aliased as two builtins: Scripter and Application./class KRITALIBKIS_EXPORT Krita : public QObject{Q_OBJECT"""

    @staticmethod
    def activeDocument() -> 'Document':
        """Return Type: Document
        @return the currently active document, if there is one."""

    @staticmethod
    def setActiveDocument(Document):
        """Return Type: void
        @brief setActiveDocument activates the first view that shows the given document @param value the document we want to activate"""

    @staticmethod
    def batchmode():
        """Return Type: bool
        @brief batchmode determines whether the script is run in batch mode. If batchmode is true, scripts should now show messageboxes or dialog boxes. Note that this separate from Document.setBatchmode(), which determines whether export/save option dialogs are shown. @return true if the script is run in batchmode"""

    @staticmethod
    def setBatchmode(bool):
        """Return Type: void
        @brief setBatchmode sets the the batchmode to @param value; if true, scripts should not show dialogs or messageboxes."""

    @staticmethod
    def actions():
        """Return Type: QList<Action>
        @return return a list of all actions for the currently active mainWindow."""

    @staticmethod
    def action(QString):
        """Return Type: Action
        @return the action that has been registered under the given name, or 0 if no such action exists."""

    @staticmethod
    def documents():
        """Return Type: QList<Document>
        @return a list of all open Documents"""

    @staticmethod
    def filters():
        """Return Type: QStringList
        @brief Filters are identified by an internal name. This function returns a list of all existing registered filters. @return a list of all registered filters"""

    @staticmethod
    def filter(QString):
        """Return Type: Filter
        @brief filter construct a Filter object with a default configuration. @param name the name of the filter. Use Krita.instance().filters() to get a list of all possible filters. @return the filter or None if there is no such filter."""

    @staticmethod
    def profiles(s1: str, s2: str):
        """Return Type: QStringList
        Missing function documentation"""

    @staticmethod
    def addProfile(QString):
        """Return Type: bool
        @brief addProfile load the given profile into the profile registry. @param profilePath the path to the profile. @return true if adding the profile succeeded."""

    @staticmethod
    def notifier():
        """Return Type: Notifier
        @brief notifier the Notifier singleton emits signals when documents are opened and closed, the configuration changes, views are opened and closed or windows are opened. @return the notifier object"""

    @staticmethod
    def version():
        """Return Type: QString
        @brief version Determine the version of Krita Usage: print(Application.version ()) @return the version string including git sha1 if Krita was built from git"""

    @staticmethod
    def views():
        """Return Type: QList<View>
        @return a list of all views. A Document can be shown in more than one view."""

    @staticmethod
    def activeWindow() -> 'Window':
        """Return Type: Window
        @return the currently active window or None if there is no window"""

    @staticmethod
    def windows():
        """Return Type: QList<Window>
        @return a list of all windows"""

    @staticmethod
    def Resource(QString):
        """Return Type: QMap<QString,
        @brief resources returns a list of Resource objects of the given type @param type Valid types are: <ul> <li>pattern</li> <li>gradient</li> <li>brush</li> <li>preset</li> <li>palette</li> <li>workspace</li> </ul>"""

    @staticmethod
    def createDocument(a: int, b: int, s1: str, s2: str, s3: str, s4: str):
        """Return Type: Document
        Missing function documentation"""

    @staticmethod
    def openDocument(QString) -> 'Document':
        """Return Type: Document
        @brief openDocument creates a new Document, registers it with the Krita application and loads the given file. @param filename the file to open in the document @return the document"""

    @staticmethod
    def openWindow():
        """Return Type: Window
        @brief openWindow create a new main window. The window is not shown by default."""

    @staticmethod
    def createAction(QString):
        """Return Type: Action
        @brief createAction creates an action with the given text and passes it to Krita. Every newly created     mainwindow will create an instance of this action. @param text the user-visible text @return the Action you can connect a slot to."""

    @staticmethod
    def addExtension(Extension):
        """Return Type: void
        @brief addExtension add the given plugin to Krita. There will be a single instance of each Extension in the Krita process. @param extension the extension to add."""

    @staticmethod
    def extensions():
        """Return Type: QList<Extension>
        return a list with all registered extension objects."""

    @staticmethod
    def addDockWidgetFactory(DockWidgetFactoryBase):
        """Return Type: void
        @brief addDockWidgetFactory Add the given docker factory to the application. For scripts loaded on startup, this means that every window will have one of the dockers created by the factory. @param factory The factory object."""

    @staticmethod
    def writeSetting(s1: str, s2: str, s3: str):
        """Return Type: void
        @brief writeSetting write the given setting under the given name to the kritarc file in the given settings group. @param group The group the setting belongs to. If empty, then the setting is written in the general section @param name The name of the setting @param value The value of the setting. Script settings are always written as strings."""

    @staticmethod
    def readSetting(s1: str, s2: str, s3: str):
        """Return Type: QString
        @brief readSetting read the given setting value from the kritarc file. @param group The group the setting is part of. If empty, then the setting is read from the general group. @param name The name of the setting @param defaultValue The default value of the setting @return a string representing the setting."""

    @staticmethod
    def instance() -> 'Krita':
        """Return Type: static
        @brief instance retrieve the singleton instance of the Application object."""

    @staticmethod
    def QObject(QVariant):
        """Return Type: static
        @brief instance retrieve the singleton instance of the Application object./static Krita instance();"""


# auto-generated from: Channel.h
class Channel:
    """ A Channel represents a singel channel in a Node. Krita does not
    use channels to store local selections: these are strictly the
    color and alpha channels.
       """

    @staticmethod
    def Channel(KisNodeSP, KoChannelInfo, QObject):
        """Return Type: void
        A Channel represents a singel channel in a Node. Krita does not use channels to store local selections: these are strictly the color and alpha channels./class KRITALIBKIS_EXPORT Channel : public QObject{Q_OBJECT"""

    @staticmethod
    def visible():
        """Return Type: bool
        @brief visible checks whether this channel is visible in the node @return the status of this channel"""

    @staticmethod
    def setVisible(bool):
        """Return Type: void
        @brief setvisible set the visibility of the channel to the given value."""

    @staticmethod
    def name():
        """Return Type: QString
        @return the name of the channel"""

    @staticmethod
    def position():
        """Return Type: int
        @returns the position of the first byte of the channel in the pixel"""

    @staticmethod
    def channelSize():
        """Return Type: int
        @return the number of bytes this channel takes"""

    @staticmethod
    def bounds():
        """Return Type: QRect
        @return the exact bounds of the channel. This can be smaller than the bounds of the Node this channel is part of."""

    @staticmethod
    def pixelData(QRect):
        """Return Type: QByteArray
        Read the values of the channel into the a byte array for each pixel in the rect from the Node this channel is part of, and returns it. Note that if Krita is built with OpenEXR and the Node has the 16 bits floating point channel depth type, Krita returns 32 bits float for every channel; the libkis scripting API does not support half."""

    @staticmethod
    def setPixelData(QByteArray, QRect):
        """Return Type: void
        @brief setPixelData writes the given data to the relevant channel in the Node. This is only possible for Nodes that have a paintDevice, so nothing will happen when trying to write to e.g. a group layer. Note that if Krita is built with OpenEXR and the Node has the 16 bits floating point channel depth type, Krita expects to be given a 4 byte, 32 bits float for every channel; the libkis scripting API does not support half. @param value a byte array with exactly enough bytes. @param rect the rectangle to write the bytes into"""

    # auto-generated from: Filter.h


class Filter:
    """ Filter: represents a filter and its configuration. A filter is identified by
    an internal name. The configuration for each filter is defined as an InfoObject:
    a map of name and value pairs.

    Currently available filters are:

    'autocontrast', 'blur', 'bottom edge detections', 'brightnesscontrast', 'burn', 'colorbalance', 'colortoalpha', 'colortransfer',
    'desaturate', 'dodge', 'emboss', 'emboss all directions', 'emboss horizontal and vertical', 'emboss horizontal only',
    'emboss laplascian', 'emboss vertical only', 'gaussian blur', 'gaussiannoisereducer', 'gradientmap', 'halftone', 'hsvadjustment',
    'indexcolors', 'invert', 'left edge detections', 'lens blur', 'levels', 'maximize', 'mean removal', 'minimize', 'motion blur',
    'noise', 'normalize', 'oilpaint', 'perchannel', 'phongbumpmap', 'pixelize', 'posterize', 'raindrops', 'randompick',
    'right edge detections', 'roundcorners', 'sharpen', 'smalltiles', 'sobel', 'threshold', 'top edge detections', 'unsharp',
    'wave', 'waveletnoisereducer']
       """

    @staticmethod
    def Filter():
        """Return Type: void
        @brief Filter: create an empty filter object. Until a name is set, the filter cannot be applied."""

    @staticmethod
    def name():
        """Return Type: QString
        @brief name the internal name of this filter. @return the name."""

    @staticmethod
    def setName(QString):
        """Return Type: void
        @brief setName set the filter's name to the given name."""

    @staticmethod
    def configuration():
        """Return Type: InfoObject
        @return the configuration object for the filter"""

    @staticmethod
    def setConfiguration(InfoObject):
        """Return Type: void
        @brief setConfiguration set the configuration object for the filter"""

    @staticmethod
    def apply(Node, a: int, b: int, c: int, d: int, /):
        """Return Type: bool
        @brief Apply the filter to the given node. @param node the node to apply the filter to @params x, y, w, h: describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node. @return true if the filter was applied succesfully, or false if the filter could not be applied because the node is locked or does not have an editable paint device."""

    @staticmethod
    def startFilter(Node, a: int, b: int, c: int, d: int, /):
        """Return Type: bool
        @brief startFilter starts the given filter on the given node. @param node the node to apply the filter to @params x, y, w, h: describe the rectangle the filter should be apply. This is always in image pixel coordinates and not relative to the x, y of the node."""

    # auto-generated from: Extension.h


class Extension:
    """ An Extension is the base for classes that extend Krita. An Extension
    is loaded on startup, when the setup() method will be executed.

    The extension instance should be added to the Krita Application object
    using Krita.instance().addViewExtension or Application.addViewExtension
    or Scripter.addViewExtension.

    Example:

    @code
    import sys
    from PyQt5.QtGui import
    from PyQt5.QtWidgets import
    from krita import
    class HelloExtension(Extension):

    @staticmethod
    def  __init__(self, parent):
        super().__init__(parent)

    @staticmethod
    def  hello(self):
        QMessageBox.information(QWidget(), "Test", "Hello! This is Krita " + Application.version())

    @staticmethod
    def  setup(self):
        qDebug("Hello Setup")
        action = Krita.instance().createAction("hello")
        action.triggered.connect(self.hello)

    Scripter.addExtension(HelloExtension(Krita.instance()))

    @endcode
       """

    @staticmethod
    def Extension(QObject):
        """Return Type: void
        Create a new extension. The extension will be owned by @param parent."""

    @staticmethod
    def setup():
        """Return Type: void
        Override this function to setup your Extension. You can use it to add Actions to the action collection or integrate in any other way with the application."""

    # auto-generated from: Canvas.h


class Canvas:
    """ Canvas wraps the canvas inside a view on an image/document.
    It is responsible for the view parameters of the document:
    zoom, rotation, mirror, wraparound and instant preview.
       """

    @staticmethod
    def Canvas(KoCanvasBase, QObject):
        """Return Type: void
        Canvas wraps the canvas inside a view on an image/document. It is responsible for the view parameters of the document: zoom, rotation, mirror, wraparound and instant preview./class KRITALIBKIS_EXPORT Canvas : public QObject{Q_OBJECT"""

    @staticmethod
    def zoomLevel():
        """Return Type: qreal
        @return the current zoomlevel. 1.0 is 100%."""

    @staticmethod
    def setZoomLevel(qreal):
        """Return Type: void
        @brief setZoomLevel set the zoomlevel to the given @param value. 1.0 is 100%."""

    @staticmethod
    def resetZoom():
        """Return Type: void
        @brief resetZoom set the zoomlevel to 100%"""

    @staticmethod
    def rotation():
        """Return Type: qreal
        @return the rotation of the canvas in degrees."""

    @staticmethod
    def setRotation(qreal):
        """Return Type: void
        @brief setRotation set the rotation of the canvas to the given  @param angle in degrees."""

    @staticmethod
    def resetRotation():
        """Return Type: void
        @brief resetRotation reset the canvas rotation."""

    @staticmethod
    def mirror():
        """Return Type: bool
        @return return true if the canvas is mirrored, false otherwise."""

    @staticmethod
    def setMirror(bool):
        """Return Type: void
        @brief setMirror turn the canvas mirroring on or off depending on @param value"""

    @staticmethod
    def wrapAroundMode():
        """Return Type: bool
        @return true if the canvas is in wraparound mode, false if not. Only when OpenGL is enabled, is wraparound mode available."""

    @staticmethod
    def setWrapAroundMode(bool):
        """Return Type: void
        @brief setWrapAroundMode set wraparound mode to  @param enable"""

    @staticmethod
    def levelOfDetailMode():
        """Return Type: bool
        @return true if the canvas is in Instant Preview mode, false if not. Only when OpenGL is enabled, is Instant Preview mode available."""

    @staticmethod
    def setLevelOfDetailMode(bool):
        """Return Type: void
        @brief setLevelOfDetailMode sets Instant Preview to @param enable"""

    @staticmethod
    def view():
        """Return Type: View
        @return the view that holds this canvas"""

    # auto-generated from: InfoObject.h


class InfoObject:
    """ InfoObject wrap a properties map. These maps can be used to set the
    configuration for filters.
       """

    @staticmethod
    def InfoObject(KisPropertiesConfigurationSP):
        """Return Type: void
        InfoObject wrap a properties map. These maps can be used to set the configuration for filters./class KRITALIBKIS_EXPORT InfoObject : public QObject{Q_OBJECT"""

    @staticmethod
    def InfoObject(QObject):
        """Return Type: void
        Create a new, empty InfoObject."""

    @staticmethod
    def QVariant():
        """Return Type: QMap<QString,
        Return all properties this InfoObject manages."""

    @staticmethod
    def setProperties(qmap: dict):
        """Return Type: void
        Add all properties in the @param propertyMap to this InfoObject"""
        pass

    @staticmethod
    def setProperty(QString, QVariant):
        """Return Type: void
        set the property identified by @key to @value"""

    @staticmethod
    def property(QString):
        """Return Type: QVariant
        return the value for the property identified by key, or None if there is no suck key."""

    @staticmethod
    def configuration():
        """Return Type: KisPropertiesConfigurationSP
        @brief configuration gives access to the internal configuration object. Must be used used internally in libkis @return the internal configuration object."""


# auto-generated from: DockWidgetFactoryBase.h
class DockWidgetFactoryBase:
    """ @brief The DockWidgetFactoryBase class is the base class for plugins that want
    to add a dock widget to every window. You do not need to implement this class
    yourself, but create a DockWidget implementation and then add the DockWidgetFactory
    to the Krita instance like this:

    @code
    class HelloDocker(DockWidget):
      @staticmethod
    def  __init__(self):
          super().__init__()
          label = QLabel("Hello", self)
          self.setWidget(label)
          self.label = label

    @staticmethod
    def  canvasChanged(self, canvas):
          self.label.setText("Hellodocker: canvas changed");

    Application.addDockWidgetFactory(DockWidgetFactory("hello", DockWidgetFactoryBase.DockRight, HelloDocker))

    @endcode
       """

    @staticmethod
    def DockWidgetFactoryBase(QString, DockPosition, bool, bool2):
        """Return Type: void
        Missing function documentation"""

    @staticmethod
    def id():
        """Return Type: QString
        Missing function documentation"""

    @staticmethod
    def defaultDockPosition():
        """Return Type: DockPosition
        Missing function documentation"""

    @staticmethod
    def isCollapsable():
        """Return Type: bool
        Missing function documentation"""

    @staticmethod
    def defaultCollapsed():
        """Return Type: bool
        Missing function documentation"""

    # auto-generated from: Window.h


class Window:
    """ Window represents one Krita mainwindow. A window can have any number
    of views open on any number of documents.
       """

    @staticmethod
    def Window(KisMainWindow, QObject):
        """Return Type: void
        Window represents one Krita mainwindow. A window can have any number of views open on any number of documents./class KRITALIBKIS_EXPORT Window : public QObject{Q_OBJECT"""

    @staticmethod
    def qwindow():
        """Return Type: QMainWindow
        Return a handle to the QMainWindow widget. This is useful to e.g. parent dialog boxes and message box."""

    @staticmethod
    def views():
        """Return Type: QList<View>
        @return a list of open views in this window"""

    @staticmethod
    def addView(Document):
        """Return Type: View
        Open a new view on the given document in this window"""

    @staticmethod
    def showView(View):
        """Return Type: void
        Make the given view active in this window. If the view does not belong to this window, nothing happens."""

    @staticmethod
    def activate():
        """Return Type: void
        @brief activate activates this Window."""

    @staticmethod
    def close():
        """Return Type: void
        @brief close the active window and all its Views. If there are no Views left for a given Document, that Document will also be closed."""

    @staticmethod
    def windowClosed():
        """Return Type: void
        @brief close the active window and all its Views. If there are no Views left for a given Document, that Document will also be closed./void close();Q_SIGNALS:"""

    # auto-generated from: PresetChooser.h


class PresetChooser:
    """ @brief The PresetChooser widget wraps the KisPresetChooser widget.
    The widget provides for selecting brush presets. It has a tagging
    bar and a filter field. It is not automatically synchronized with
    the currently selected preset in the current Windows.
       """

    @staticmethod
    def PresetChooser(QWidget):
        """Return Type: void
        @brief The PresetChooser widget wraps the KisPresetChooser widget. The widget provides for selecting brush presets. It has a tagging bar and a filter field. It is not automatically synchronized with the currently selected preset in the current Windows./class KRITALIBKIS_EXPORT PresetChooser : public KisPresetChooser{Q_OBJECT"""

    @staticmethod
    def setCurrentPreset(Resource):
        """Return Type: void
        Make the given preset active."""

    @staticmethod
    def currentPreset():
        """Return Type: Resource
        @return a Resource wrapper around the currently selected preset."""

    @staticmethod
    def presetSelected(Resource):
        """Return Type: void
        Emited whenever a user selects the given preset."""

    @staticmethod
    def presetClicked(Resource):
        """Return Type: void
        Emited whenever a user clicks on the given preset."""

    @staticmethod
    def slotResourceSelected(KoResource):
        """Return Type: void
        Emited whenever a user clicks on the given preset./void presetClicked(Resource resource);private Q_SLOTS:"""

    @staticmethod
    def slotResourceClicked(KoResource):
        """Return Type: void
        Emited whenever a user clicks on the given preset./void presetClicked(Resource resource);private Q_SLOTS:"""

    # auto-generated from: Selection.h


class Selection:
    """ Selection represents a selection on Krita. A selection is
    not necessarily associated with a particular Node or Image.

    @code
    from krita import

    d = Application.activeDocument()
    n = d.activeNode()
    r = n.bounds()
    s = Selection()
    s.select(r.width() / 3, r.height() / 3, r.width() / 3, r.height() / 3, 255)
    s.cut(n)
    @endcode
       """

    @staticmethod
    def Selection(KisSelectionSP, QObject):
        """Return Type: void
        For internal use only."""

    @staticmethod
    def Selection(QObject):
        """Return Type: void
        Create a new, empty selection object."""

    @staticmethod
    def width() -> int:
        """Return Type: int
        @return the width of the selection"""

    @staticmethod
    def height() -> int:
        """Return Type: int
        @return the height of the selection"""

    @staticmethod
    def x() -> int:
        """Return Type: int
        @return the left-hand position of the selection."""

    @staticmethod
    def y() -> int:
        """Return Type: int
        @return the top position of the selection."""

    @staticmethod
    def move(a: int, b: int):
        """Return Type: void
        Move the selection's top-left corner to the given coordinates."""

    @staticmethod
    def clear():
        """Return Type: void
        Make the selection entirely unselected."""

    @staticmethod
    def contract(int):
        """Return Type: void
        Make the selection's width and height smaller by the given value. This will not move the selection's top-left position."""

    @staticmethod
    def copy(Node):
        """Return Type: void
        @brief copy copies the area defined by the selection from the node to the clipboard. @param node the node from where the pixels will be copied."""

    @staticmethod
    def cut(Node):
        """Return Type: void
        @brief cut erases the area defined by the selection from the node and puts a copy on the clipboard. @param node the node from which the selection will be cut."""

    @staticmethod
    def paste(Node, a: int, b: int):
        """Return Type: void
        @brief paste pastes the content of the clipboard to the given node, limited by the area of the current selection. @param destination the node where the pixels will be written @param x: the x position at which the clip will be written @param y: the y position at which the clip will be written"""

    @staticmethod
    def erode():
        """Return Type: void
        Erode the selection with a radius of 1 pixel."""

    @staticmethod
    def dilate():
        """Return Type: void
        Dilate the selection with a radius of 1 pixel."""

    @staticmethod
    def border(a: int, b: int):
        """Return Type: void
        Border the selection with the given radius."""

    @staticmethod
    def feather(int):
        """Return Type: void
        Feather the selection with the given radius."""

    @staticmethod
    def grow(a: int, b: int):
        """Return Type: void
        Grow the selection with the given radius."""

    @staticmethod
    def shrink(a: int, b: int, bool):
        """Return Type: void
        Shrink the selection with the given radius."""

    @staticmethod
    def smooth():
        """Return Type: void
        Smooth the selection."""

    @staticmethod
    def invert():
        """Return Type: void
        Invert the selection."""

    @staticmethod
    def resize(a: int, b: int):
        """Return Type: void
        Resize the selection to the given width and height. The top-left position will not be moved."""

    @staticmethod
    def select(a: int, b: int, c: int, d: int, e: int, /):
        """Return Type: void
        Select the given area. The value can be between 0 and 255; 0 is totally unselected, 255 is totally selected."""

    @staticmethod
    def selectAll(p1: 'Node', p2: int):
        """Return Type: void
        Select all pixels in the given node. The value can be between 0 and 255; 0 is totally unselected, 255 is totally selected."""

    @staticmethod
    def replace(p1: Selection):
        """Return Type: void
        Replace the current selection's selection with the one of the given selection."""

    @staticmethod
    def add(p1: Selection):
        """Return Type: void
        Add the given selection's selected pixels to the current selection."""

    @staticmethod
    def subtract(p1: Selection):
        """Return Type: void
        Subtract the given selection's selected pixels from the current selection."""

    @staticmethod
    def intersect(p1: Selection):
        """Return Type: void
        Intersect the given selection with this selection."""

    @staticmethod
    def pixelData(a: int, b: int, c: int, d: int, /) -> QByteArray:
        """Return Type: QByteArray
        Missing function documentation"""

    @staticmethod
    def setPixelData(p1: QByteArray, a: int, b: int, c: int, d: int, /):
        """Return Type: void
        @brief setPixelData writes the given bytes, of which there must be enough, into the Selection. @param value the byte array representing the pixels. There must be enough bytes available. Krita will take the raw pointer from the QByteArray and start reading, not stopping before (w  h) bytes are read. @param x the x position to start writing from @param y the y position to start writing from @param w the width of each row @param h the number of rows to write"""

    @staticmethod
    def selection() -> 'KisSelectionSP':
        """Return Type: KisSelectionSP
        Missing function documentation"""

    # auto-generated from: DockWidget.h


class DockWidget:
    """ DockWidget is the base class for custom Dockers. Dockers are created by a
    factory class which needs to be registered by calling Application.addDockWidgetFactory:

    @code
    class HelloDocker(DockWidget):
      @staticmethod
    def  __init__(self):
          super().__init__()
          label = QLabel("Hello", self)
          self.setWidget(label)
          self.label = label

    @staticmethod
    def  canvasChanged(self, canvas):
          self.label.setText("Hellodocker: canvas changed");

    Application.addDockWidgetFactory(DockWidgetFactory("hello", DockWidgetFactoryBase.DockRight, HelloDocker))

    @endcode

    One docker per window will be created, not one docker per canvas or view. When the user
    switches between views/canvases, canvasChanged will be called. You can override that
    method to reset your docker's internal state, if necessary.
       """

    @staticmethod
    def DockWidget():
        """Return Type: void
        Missing function documentation"""

    @staticmethod
    def setCanvas(p1: 'KoCanvasBase'):
        """Return Type: void
        Missing function documentation"""

    @staticmethod
    def unsetCanvas():
        """Return Type: void
        Missing function documentation"""

    @staticmethod
    def canvas() -> Canvas:
        """Return Type: Canvas
        @@return the canvas object that this docker is currently associated with"""

    @staticmethod
    def canvasChanged(p1: Canvas):
        """Return Type: void
        @brief canvasChanged is called whenever the current canvas is changed in the mainwindow this dockwidget instance is shown in. @param canvas The new canvas."""



# auto-generated from: Action.h
class Action:
    """ Action encapsulates a KisAction. By default, actions are put in the Tools/Scripts menu.
       """

    @staticmethod
    def Action(p1: QObject):
        """Return Type: void
        @brief Action Create a new action object @param parent the parent if it's in a QObject hierarchy"""

    @staticmethod
    def Action(p1: str, p2: str, p3: QObject):
        """Return Type: void
        @brief Action Create a new action object @param name the name of the action @param action the QAction it wraps @param parent the parent if it's in a QObject hierarchy"""

    @staticmethod
    def text() -> str:
        """Return Type: QString
        @return the user-visible text of the action."""

    @staticmethod
    def settext(p1: str):
        """Return Type: void
        set the user-visible text of the action to @param text."""

    @staticmethod
    def name() -> str:
        """Return Type: QString
        @return the internal name of the action."""

    @staticmethod
    def setName(p1: str):
        """Return Type: void
        set the name of the action to @param name. This is not the user-visible name, but the internal one"""

    @staticmethod
    def isCheckable():
        """Return Type: bool
        @return true if the action is checkable, false if it isn't"""

    @staticmethod
    def setCheckable(bool):
        """Return Type: void
        Set the action action checkable if @param value is true, unchecked if it's false"""

    @staticmethod
    def isChecked():
        """Return Type: bool
        @return true if the action is checked, false if it isn't"""

    @staticmethod
    def setChecked(bool):
        """Return Type: void
        Set the action checked if @param value is true, unchecked if it's false"""

    @staticmethod
    def shortcut():
        """Return Type: QString
        Return the action's shortcut as a string"""

    @staticmethod
    def setShortcut(QString):
        """Return Type: void
        set the action's shortcut to the given string. @code action.setShortcut("CTRL+SHIFT+S") @endcode"""

    @staticmethod
    def isVisible():
        """Return Type: bool
        set the action's shortcut to the given string. @code action.setShortcut("CTRL+SHIFT+S") @endcode/void setShortcut(QString value);"""

    @staticmethod
    def setVisible(bool):
        """Return Type: void
        @brief setVisible determines whether the action will be visible in the scripting menu. @param value true if the action is to be shown in the menu, false otherwise"""

    @staticmethod
    def isEnabled():
        """Return Type: bool
        @return true if the action is enabled, false if not"""

    @staticmethod
    def setEnabled(bool):
        """Return Type: void
        Set the action enabled or disabled according to @param value"""

    @staticmethod
    def setToolTip(QString):
        """Return Type: void
        Set the tooltip to the given @param tooltip"""

    @staticmethod
    def trigger():
        """Return Type: void
        Trigger this action"""

    @staticmethod
    def triggered(bool):
        """Return Type: void
        Emitted whenever the action is triggered."""

    # auto-generated from: Node.h


class Node:
    """ Node represents a layer or mask in a Krita image's Node hierarchy. Group layers can contain
    other layers and masks; layers can contain masks.

       """

    @staticmethod
    def Node(KisImageSP, KisNodeSP, QObject):
        """Return Type: void
        Node represents a layer or mask in a Krita image's Node hierarchy. Group layers can contain other layers and masks; layers can contain masks./class KRITALIBKIS_EXPORT Node : public QObject{Q_OBJECTQ_DISABLE_COPY(Node)"""

    @staticmethod
    def alphaLocked():
        """Return Type: bool
        @brief alphaLocked checks whether the node is a paint layer and returns whether it is alpha locked @return whether the paint layer is alpha locked, or false if the node is not a paint layer"""

    @staticmethod
    def setAlphaLocked(bool):
        """Return Type: void
        @brief setAlphaLocked set the layer to value if the the node is paint layer."""

    @staticmethod
    def blendingMode():
        """Return Type: QString
        @return the blending mode of the layer. The values of the blending modes are defined in @see KoCompositeOpRegistry.h"""

    @staticmethod
    def setBlendingMode(QString):
        """Return Type: void
        @brief setBlendingMode set the blending mode of the node to the given value @param value one of the string values from @see KoCompositeOpRegistry.h"""

    @staticmethod
    def channels():
        """Return Type: QList<Channel>
        @brief channels creates a list of Channel objects that can be used individually to show or hide certain channels, and to retrieve the contents of each channel in a node separately. Only layers have channels, masks do not, and calling channels on a Node that is a mask will return an empty list. @return the list of channels ordered in by position of the channels in pixel position"""

    @staticmethod
    def childNodes() -> List[Node]:
        """Return Type: QList<Node>
        Return a list of child nodes of the current node. The nodes are ordered from the bottommost up. The function is not recursive."""

    @staticmethod
    def addChildNode(Node, Node2):
        """Return Type: bool
        @brief addChildNode adds the given node in the list of children. @param child the node to be added @param above the node above which this node will be placed @return false if adding the node failed"""

    @staticmethod
    def removeChildNode(Node):
        """Return Type: bool
        @brief removeChildNode removes the given node from the list of children. @param child the node to be removed"""

    @staticmethod
    def setChildNodes(QList):
        """Return Type: void
        @brief setChildNodes this replaces the existing set of child nodes with the new set. @param nodes The list of nodes that will become children, bottom-up -- the first node, is the bottom-most node in the stack."""

    @staticmethod
    def colorDepth():
        """Return Type: QString
        colorDepth A string describing the color depth of the image: <ul> <li>U8: unsigned 8 bits integer, the most common type</li> <li>U16: unsigned 16 bits integer</li> <li>F16: half, 16 bits floating point. Only available if Krita was built with OpenEXR</li> <li>F32: 32 bits floating point</li> </ul> @return the color depth."""

    @staticmethod
    def colorModel():
        """Return Type: QString
        @brief colorModel retrieve the current color model of this document: <ul> <li>A: Alpha mask</li> <li>RGBA: RGB with alpha channel (The actual order of channels is most often BGR!)</li> <li>XYZA: XYZ with alpha channel</li> <li>LABA: LAB with alpha channel</li> <li>CMYKA: CMYK with alpha channel</li> <li>GRAYA: Gray with alpha channel</li> <li>YCbCrA: YCbCr with alpha channel</li> </ul> @return the internal color model string."""

    @staticmethod
    def colorProfile():
        """Return Type: QString
        @return the name of the current color profile"""

    @staticmethod
    def setColorProfile(QString):
        """Return Type: bool
        @brief setColorProfile set the color profile of the image to the given profile. The profile has to be registered with krita and be compatible with the current color model and depth; the image data is <i>not</i> converted. @param colorProfile @return if assigining the colorprofiel worked"""

    @staticmethod
    def setColorSpace(s1: str, s2: str, s3: str):
        """Return Type: bool
        Missing function documentation"""

    @staticmethod
    def animated():
        """Return Type: bool
        @brief Krita layers can be animated, i.e., have frames. @return return true if the layer has frames. Currently, the scripting framework does not give access to the animation features."""

    @staticmethod
    def enableAnimation():
        """Return Type: void
        @brief enableAnimation make the current layer animated, so it can have frames."""

    @staticmethod
    def setCollapsed(bool):
        """Return Type: void
        Sets the state of the node to the value of @param collapsed"""

    @staticmethod
    def collapsed():
        """Return Type: bool
        returns the collapsed state of this node"""

    @staticmethod
    def colorLabel():
        """Return Type: int
        Sets a color label index associated to the layer.  The actual color of the label and the number of available colors is defined by Krita GUI configuration."""

    @staticmethod
    def setColorLabel(int):
        """Return Type: void
        @brief setColorLabel sets a color label index associated to the layer.  The actual color of the label and the number of available colors is defined by Krita GUI configuration. @param index an integer corresponding to the set of available color labels."""

    @staticmethod
    def inheritAlpha():
        """Return Type: bool
        @brief inheritAlpha checks whether this node has the inherits alpha flag set @return true if the Inherit Alpha is set"""

    @staticmethod
    def setInheritAlpha(bool):
        """Return Type: void
        set the Inherit Alpha flag to the given value"""

    @staticmethod
    def locked():
        """Return Type: bool
        @brief locked checkes whether the Node is locked. A locked node cannot be changed. @return true if the Node is locked, false if it hasn't been locked."""

    @staticmethod
    def setLocked(bool):
        """Return Type: void
        set the Locked flag to the give value"""

    @staticmethod
    def name():
        """Return Type: QString
        @return the user-visible name of this node."""

    @staticmethod
    def setName(QString):
        """Return Type: void
        rename the Node to the given name"""

    @staticmethod
    def opacity():
        """Return Type: int
        return the opacity of the Node. The opacity is a value between 0 and 255."""

    @staticmethod
    def setOpacity(int):
        """Return Type: void
        set the opacity of the Node to the given value. The opacity is a value between 0 and 255."""

    @staticmethod
    def parentNode():
        """Return Type: Node
        return the Node that is the parent of the current Node, or 0 if this is the root Node."""

    @staticmethod
    def type():
        """Return Type: QString
        Missing function documentation"""

    @staticmethod
    def visible():
        """Return Type: bool
        Check whether the current Node is visible in the layer stack"""

    @staticmethod
    def setVisible(bool):
        """Return Type: void
        Set the visibility of the current node to @param visible"""

    @staticmethod
    def pixelData(a: int, b: int, c: int, d: int, /):
        """Return Type: QByteArray
        Missing function documentation"""

    @staticmethod
    def projectionPixelData(a: int, b: int, c: int, d: int, /):
        """Return Type: QByteArray
        Missing function documentation"""

    @staticmethod
    def setPixelData(QByteArray, a: int, b: int, c: int, d: int, /):
        """Return Type: void
        Missing function documentation"""

    @staticmethod
    def bounds():
        """Return Type: QRect
        @brief bounds return the exact bounds of the node's paint device @return the bounds, or an empty QRect if the node has no paint device or is empty."""

    @staticmethod
    def move(a: int, b: int):
        """Return Type: void
         move the pixels to the given x, y location in the image coordinate space."""

    @staticmethod
    def position():
        """Return Type: QPoint
        @brief position returns the position of the paint device of this node @return the top-left position of the node"""

    @staticmethod
    def remove():
        """Return Type: bool
        @brief remove removes this node from its parent image."""

    @staticmethod
    def duplicate() -> 'Node':
        """Return Type: Node
        @brief duplicate returns a full copy of the current node. The node is not inserted in the graphc @return a valid Node object or 0 if the node couldn't be duplicated."""

    @staticmethod
    def save(QString, double, double2):
        """Return Type: bool
        @brief save exports the given node with this filename. The extension of the filename determins the filetype. @param filename the filename including extension @param xRes the horizontal resolution in pixels per pt (there are 72 pts in an inch) @param yRes the horizontal resolution in pixels per pt (there are 72 pts in an inch) @return true if saving succeeded, false if it failed."""

    @staticmethod
    def mergeDown() -> 'Node':
        """Return Type: Node
        @brief mergeDown merges the given node with the first visible node underneath this node in the layerstack. This will drop all per-layer metadata. @param node the node to merge down; this node will be removed from the layer stack"""

    @staticmethod
    def thumbnail(a: int, b: int) -> QImage:
        """Return Type: QImage
        @brief thumbnail create a thumbnail of the given dimensions. The thumbnail is sized according to the layer dimensions, not the image dimensions. If the requested size is too big a null QImage is created. If the current node cannot generate a thumbnail, a transparent QImage of the requested size is generated. @return a QImage representing the layer contents."""

    @staticmethod
    def paintDevice():
        """Return Type: KisPaintDeviceSP
        @brief paintDevice gives access to the internal paint device of this Node @return the paintdevice or 0 if the node does not have an editable paint device."""

    @staticmethod
    def image() -> 'KisImageP':
        """Return Type: KisImageSP
        @brief paintDevice gives access to the internal paint device of this Node @return the paintdevice or 0 if the node does not have an editable paint device./"""

    @staticmethod
    def node():
        """Return Type: KisNodeSP
        @brief paintDevice gives access to the internal paint device of this Node @return the paintdevice or 0 if the node does not have an editable paint device./KisPaintDeviceSP paintDevice() const;"""


# auto-generated from: View.h
class View:
    """ View represents one view on a document. A document can be
    shown in more than one view at a time.
       """

    @staticmethod
    def View(KisView, QObject):
        """Return Type: void
        View represents one view on a document. A document can be shown in more than one view at a time./class KRITALIBKIS_EXPORT View : public QObject{Q_OBJECTQ_DISABLE_COPY(View)"""

    @staticmethod
    def window():
        """Return Type: Window
        @return the window this view is shown in."""

    @staticmethod
    def document():
        """Return Type: Document
        @return the document this view is showing."""

    @staticmethod
    def visible():
        """Return Type: bool
        @return true if the current view is visible, false if not."""

    @staticmethod
    def setVisible():
        """Return Type: void
        Make the current view visible."""

    @staticmethod
    def canvas():
        """Return Type: Canvas
        @return the canvas this view is showing. The canvas controls things like zoom and rotation."""

    @staticmethod
    def activateResource(Resource):
        """Return Type: void
        @brief activateResource activates the given resource. @param resource: a pattern, gradient or paintop preset"""

    @staticmethod
    def view():
        """Return Type: KisView
        @brief activateResource activates the given resource. @param resource: a pattern, gradient or paintop preset/void activateResource(Resource resource);private:"""
