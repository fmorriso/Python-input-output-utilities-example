import decimal
import sys
from decimal import Decimal

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication


class InputUtils:
    @staticmethod
    def get_whole_number(title: str, msg: str, parent=None) -> int:
        app = QApplication(sys.argv)
        waitingForValidInput = True
        # trap user in dialog until they enter a valid value and click OK
        while waitingForValidInput:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was preseed and False means the Cancel button was pressed
            response = QtWidgets.QInputDialog.getInt(parent, msg, title)
            # print(f'{response}=')
            if response[1]:
                waitingForValidInput = False

        n: int = response[0]
        app.closeAllWindows()
        app.exit()

        return n

    @staticmethod
    def get_decimal_number(title: str, msg: str, parent=None) -> decimal:
        app = QApplication(sys.argv)
        waitingForValidInput = True
        # trap user in dialog until they enter a valid value and click OK
        while waitingForValidInput:
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was preseed and False means the Cancel button was pressed
            min = 0
            max = decimal.MAX_EMAX
            decimals = sys.float_info.dig
            response = QtWidgets.QInputDialog.getDouble(parent, msg, title, 0, min, max, decimals)            # print(f'{response}=')
            if response[1]:
                waitingForValidInput = False

        n: decimal = Decimal(response[0])
        app.closeAllWindows()
        app.exit()
        return n
