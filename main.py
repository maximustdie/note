import sys
import os

from PyQt6.QtWidgets import QApplication

from gui.widgets.main_window import MainWindows

if __name__ == '__main__':
    current_directory = os.getcwd()
    file_list = os.listdir(current_directory)
    if not "files" in file_list:
        os.mkdir("files")
    if not "archive_files" in file_list:
        os.mkdir("archive_files")

    app = QApplication(sys.argv)
    ex = MainWindows()
    ex.show()

    sys.exit(app.exec())
