import sys

from PyQt5.QtWidgets import QApplication

from gui.widgets.main_window import MainWindows

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindows()
    ex.show()

    sys.exit(app.exec_())
