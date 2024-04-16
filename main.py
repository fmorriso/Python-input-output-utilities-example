import sys

# from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from output_utilities import OutputUtils


# from PyQt6.QtCore import *


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    app = QApplication(sys.argv)
    OutputUtils.display_message("message","title")
