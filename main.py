import sys
import os

from PyQt6.QtWidgets import QApplication

from gui.widgets.main_window import MainWindows

if __name__ == '__main__':
    current_directory = os.getcwd()
    file_list = os.listdir(current_directory)

    app = QApplication(sys.argv)
    ex = MainWindows()
    ex.show()

    sys.exit(app.exec())
