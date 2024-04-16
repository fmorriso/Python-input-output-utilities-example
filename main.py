import sys

# from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
# from PyQt6.QtCore import *

from main_window import MainWindow


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def create_and_display_gui():
    app = QApplication(sys.argv)
    w: MainWindow = MainWindow(get_python_version())
    app.exec()


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")
    create_and_display_gui()
