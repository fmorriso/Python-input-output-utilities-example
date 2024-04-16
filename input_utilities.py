import decimal

from pyqtgraph import QtWidgets


class InputUtils:
    @staticmethod
    def get_whole_number(title: str, msg: str, parent=None) -> int:
        waitingForValidInput = True
        # trap user in dialog until they enter a valid value and click OK
        while(waitingForValidInput):
            # response will be a tuple of the form (value, True/False} where True
            # means the OK button was preseed and False means the Cancel button was pressed
            response = QtWidgets.QInputDialog.getInt(parent, msg, title)
            # print(f'{response}=')
            if(response[1]):
                waitingForValidInput = False


        n:int = response[0]

        return n

    @staticmethod
    def get_decimal_number(title: str, msg: str) -> decimal:
        pass