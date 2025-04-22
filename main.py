import decimal
import sys
from importlib.metadata import version

from input_utilities import InputUtils
from output_utilities import OutputUtils


def get_python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_package_version(package_name: str) -> str:
    return version(package_name)


if __name__ == '__main__':
    print(f"Python version: {get_python_version()}")
    print(f"PyQt6 version: {get_package_version('pyqt6')}")

    OutputUtils.display_message("when in the course of human events", "title")

    val = InputUtils.get_whole_number("Enter a whole number", "title")
    OutputUtils.display_message(f"Thanks for entering {val}", "title")

    val: decimal = InputUtils.get_decimal_number("Enter a decimal number", "title")
    OutputUtils.display_message(f"Thanks for entering {val:.2f}", "title")

    yn: bool = InputUtils.get_yesno_response("Do you want a sandwich?", "Sandwich")
    print(f'yn={yn}')

    choices = ["Spring", "Summer", "Fall", "Winter"]
    choice = InputUtils.get_single_choice("Choose Season", "choose a season", choices)
    print(f'choice={choice}')
