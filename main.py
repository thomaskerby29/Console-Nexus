import sys
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
import os


def check_setup():
    if not os.path.exists('state/setup'):
        return False
    else:
        return True


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))
    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])
    if not check_setup():
        engine.load("QML/setup.qml")
    else:
        engine.load("QML/main.qml")
    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)