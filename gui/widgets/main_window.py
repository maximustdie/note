from PyQt5.QtWidgets import QListWidget, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTextEdit, QRadioButton

from app.files import get_list_notes, delete_file, read_file, delete_file_in_archive
from gui.widgets.form import Form, EditForm
from gui.widgets.info import InfoMessageBox


class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")

        self.main_layout = QHBoxLayout(self)

        # левая половина
        self.left_child_layout = QVBoxLayout()
        self.main_layout.addLayout(self.left_child_layout)

        self.left_child_layout.addWidget(QLabel("Список заметок"))

        self.list_widget = QListWidget()
        self.list_widget.addItems(get_list_notes("\\files"))
        self.list_widget.clicked.connect(self.list_widget_clicked)
        self.left_child_layout.addWidget(self.list_widget)

        self.radio1 = QRadioButton("Показать текущие заметки")
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radio_state_no_archive)
        self.left_child_layout.addWidget(self.radio1)

        self.radio2 = QRadioButton("Показать заметки в архиве")
        self.radio2.clicked.connect(self.radio_state_archive)
        self.left_child_layout.addWidget(self.radio2)

        self.btn_add = QPushButton("Добавить заметку")
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.left_child_layout.addWidget(self.btn_add)

        self.btn_edit = QPushButton("Изменить заметку")
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.left_child_layout.addWidget(self.btn_edit)

        self.btn_del = QPushButton("Удалить заметку")
        self.btn_del.clicked.connect(self.btn_del_clicked)
        self.left_child_layout.addWidget(self.btn_del)

        # правая половина
        self.right_child_layout = QVBoxLayout()
        self.main_layout.addLayout(self.right_child_layout)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.right_child_layout.addWidget(self.text)

    def update_list(self):
        self.list_widget.clear()
        self.list_widget.addItems(get_list_notes("\\files"))

    def update_list_arc(self):
        self.list_widget.clear()
        self.list_widget.addItems(get_list_notes("\\archive_files"))

    def btn_add_clicked(self):
        dialog = Form(self)
        dialog.exec_()
        if self.radio1.isChecked():
            self.update_list()
        else:
            self.update_list_arc()

    def btn_del_clicked(self):
        item = self.list_widget.currentItem()

        if not item:
            msg = InfoMessageBox("Ошибка!", "Выберите заменку для удаления!")
            msg.show()
            return

        if self.radio1.isChecked():
            delete_file(item.text())
            self.update_list()
        else:
            delete_file_in_archive(item.text())
            self.update_list_arc()
        self.text.clear()


    def btn_edit_clicked(self):
        item = self.list_widget.currentItem()

        if not item:
            msg = InfoMessageBox("Ошибка!", "Выберите заменку для изменения!")
            msg.show()
            return

        title = item.text()

        if self.radio1.isChecked():
            text = read_file(title)
            dialog = EditForm(title, text)
            dialog.exec_()
            self.update_list()
        else:
            dir_f = "archive_files"
            text = read_file(title, dir_f)
            dialog = EditForm(title, text, True)
            dialog.exec_()
            self.update_list_arc()

        self.text.clear()

    def list_widget_clicked(self):
        item = self.list_widget.currentItem()
        self.text.clear()

        if self.radio1.isChecked():
            text = read_file(item.text())
        else:
            dir_f = "archive_files"
            text = read_file(item.text(), dir_f)

        self.text.insertPlainText(text)

    def radio_state_no_archive(self):
        self.text.clear()
        self.update_list()

    def radio_state_archive(self):
        self.text.clear()
        self.update_list_arc()

