from PyQt5.QtWidgets import QListWidget, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QTextEdit

from app.files import get_list_notes, delete_file, read_file
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

        self.btn_add = QPushButton("Добавить заметку")
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.left_child_layout.addWidget(self.btn_add)

        self.btn_edit = QPushButton("Изменить заметку")
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.left_child_layout.addWidget(self.btn_edit)

        self.btn_del = QPushButton("Удалить Заметку")
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

    def btn_add_clicked(self):
        dialog = Form(self)
        dialog.exec_()
        self.update_list()

    def btn_del_clicked(self):
        item = self.list_widget.currentItem()

        if not item:
            msg = InfoMessageBox("Ошибка!", "Выберите заменку для удаления!")
            msg.show()
            return

        delete_file(item.text())
        self.text.clear()
        self.update_list()

    def btn_edit_clicked(self):
        item = self.list_widget.currentItem()

        if not item:
            msg = InfoMessageBox("Ошибка!", "Выберите заменку для изменения!")
            msg.show()
            return

        title = item.text()
        text = read_file(title)
        dialog = EditForm(title, text)
        dialog.exec_()
        self.update_list()
        self.text.clear()

    def list_widget_clicked(self):
        item = self.list_widget.currentItem()
        self.text.clear()
        text = read_file(item.text())
        self.text.insertPlainText(text)
