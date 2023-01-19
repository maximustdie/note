from PyQt6.QtWidgets import QMessageBox


class InfoMessageBox:
    def __init__(self, title, text):
        self.msg = QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setText(text)

    def show(self):
        self.msg.exec()
