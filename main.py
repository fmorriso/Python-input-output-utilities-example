import decimal
import sys

from input_utilities import InputUtils
from output_utilities import OutputUtils


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")

    # app = QApplication(sys.argv)

    OutputUtils.display_message("when in the course of human events", "title")

    val = InputUtils.get_whole_number("Enter a whole number", "title")
    OutputUtils.display_message(f"Thanks for entering {val}", "title")

    val: decimal = InputUtils.get_decimal_number("Enter a decimal number", "title")
    OutputUtils.display_message(f"Thanks for entering {val:.2f}", "title")
