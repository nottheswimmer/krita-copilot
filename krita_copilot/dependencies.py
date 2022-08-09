import os
import sys
import tarfile
import zipfile
import ssl
from hashlib import sha256
from urllib.error import URLError
from urllib.request import urlretrieve
from pathlib import Path
from platform import system


def get_app_dir():
    if system() == "Windows":
        return Path(os.environ["APPDATA"]) / "KritaCopilot"
    elif os.environ.get("HOME"):
        return Path(os.environ["HOME"]) / ".krita_copilot"
    else:
        return Path(".") / ".krita_copilot"


APP_DIR = get_app_dir()
APP_DIR.mkdir(parents=True, exist_ok=True)
PACKAGES_DIR = APP_DIR / "packages"
PACKAGES_DIR.mkdir(parents=True, exist_ok=True)

DEPENDENCIES = {
    "certifi": {
        "url": "https://files.pythonhosted.org/packages/cc/85/319a8a684e8ac6d87a1193090e06b6bbb302717496380e225ee10487c888/certifi-2022.6.15.tar.gz",
        "sha256": "84c85a9078b11105f04f3036a9482ae10e4621616db313fe045dd24743a0820d",
        "retry_without_ssl": True,
    },
    "pydalle": {
        "url": "https://files.pythonhosted.org/packages/a6/76/0c4c6da23537f0a002c31fd741e03ae09f7413c5f74fc031229c0aa9c253/pydalle-0.1.2.tar.gz",
    },
    "requests": {
        "url": "https://files.pythonhosted.org/packages/a5/61/a867851fd5ab77277495a8709ddda0861b28163c4613b011bc00228cc724/requests-2.28.1.tar.gz",
    },
    "charset_normalizer": {
        "url": "https://files.pythonhosted.org/packages/93/1d/d9392056df6670ae2a29fcb04cfa5cee9f6fbde7311a1bb511d4115e9b7a/charset-normalizer-2.1.0.tar.gz",
    },
    "urllib3": {
        "url": "https://files.pythonhosted.org/packages/6d/d5/e8258b334c9eb8eb78e31be92ea0d5da83ddd9385dc967dd92737604d239/urllib3-1.26.11.tar.gz",
        "path": "src/urllib3",
    },
    "idna": {
        "url": "https://files.pythonhosted.org/packages/62/08/e3fc7c8161090f742f504f40b1bccbfc544d4a4e09eb774bf40aafce5436/idna-3.3.tar.gz",
    },
}


def delete_recursive(path):
    if path.exists():
        for file in path.iterdir():
            if file.is_dir():
                delete_recursive(file)
            else:
                file.unlink()
        path.rmdir()
    else:
        print(f"{path} does not exist")


def my_urlretrieve(url, fp, retry_without_ssl=False):
    try:
        return urlretrieve(url, fp)
    except URLError as e:
        if 'CERTIFICATE_VERIFY_FAILED' in str(e):
            try:
                import certifi
                ssl._create_default_https_context = lambda *args, **kwargs: ssl.create_default_context(cafile=certifi.where())
                return urlretrieve(url, fp)
            except ImportError:
                if retry_without_ssl:
                    tmp = ssl._create_default_https_context
                    try:
                        ssl._create_default_https_context = ssl._create_unverified_context
                        return urlretrieve(url, fp)
                    finally:
                        ssl._create_default_https_context = tmp
                else:
                    raise e
        else:
            with open("/Users/quynhhanhh/Library/Application Support/krita/pykrita/krita_copilot/dump.txt", "w") as f:
                import traceback
                f.write(f"""
                url: {url}
                exception: {e}
                traceback: {traceback.format_exc()}""")
            raise e


def install_dependency(name: str):
    url = DEPENDENCIES[name]["url"]
    filename = url.split("/")[-1]
    wheel = DEPENDENCIES[name].get("wheel", False)

    package_destination = PACKAGES_DIR / name
    if not wheel:
        tar_gz_path = PACKAGES_DIR / filename
        extracted_path = tar_gz_path.with_suffix("").with_suffix("")
        expected_sha256 = DEPENDENCIES[name].get("sha256")

        if tar_gz_path.exists() and expected_sha256:
            sha256_hash = sha256()
            with open(tar_gz_path, "rb") as f:
                sha256_hash.update(f.read())
            if sha256_hash.hexdigest() != expected_sha256:
                print(f"Mismatched sha256 for {name}: {sha256_hash.hexdigest()} != {expected_sha256}")
                tar_gz_path.unlink()

        if not tar_gz_path.exists():
            print(f"Downloading {name}...")
            my_urlretrieve(url, tar_gz_path,
                           retry_without_ssl=DEPENDENCIES[name].get("retry_without_ssl", False))
            if expected_sha256:
                sha256_hash = sha256()
                with open(tar_gz_path, "rb") as f:
                    sha256_hash.update(f.read())
                if sha256_hash.hexdigest() != expected_sha256:
                    print(f"Mismatched sha256 for {name}: {sha256_hash.hexdigest()} != {expected_sha256}")
                    tar_gz_path.unlink()
                    raise Exception(f"Mismatched sha256 for {name}: {sha256_hash.hexdigest()} != {expected_sha256}")

        if extracted_path.exists():
            delete_recursive(extracted_path)

        with tarfile.open(tar_gz_path) as tar:
            tar.extractall(PACKAGES_DIR)

        if package_destination.exists():
            delete_recursive(package_destination)

        extracted_package = extracted_path / DEPENDENCIES[name].get("path", name)
        extracted_package.rename(package_destination)

        if extracted_path.exists():
            delete_recursive(extracted_path)
    else:
        zip_path = PACKAGES_DIR / filename
        extracted_path = zip_path.with_suffix("")

        if not zip_path.exists():
            print(f"Downloading {name}...")
            urlretrieve(url, zip_path)

        if extracted_path.exists():
            delete_recursive(extracted_path)

        with zipfile.ZipFile(zip_path) as zip:
            zip.extractall(PACKAGES_DIR)

        package_destination = extracted_path

    return package_destination


def ensure_dependencies():
    print(f"Ensuring dependencies exist in {PACKAGES_DIR}...")
    sys.path.append(PACKAGES_DIR.as_posix())

    for name in DEPENDENCIES:
        install_dependency(name)


if __name__ == '__main__':
    ensure_dependencies()
