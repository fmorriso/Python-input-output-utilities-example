from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox


class OutputUtils(QDialog):


    @staticmethod
    def display_message(msg: str, title: str) -> None:
        QMessageBox.information(None, title, msg)
