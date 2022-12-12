from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QHBoxLayout, QTextEdit, QPushButton, QCheckBox

from app.files import write_file, write_file_in_archive
from gui.widgets.info import InfoMessageBox


class LabelLineEdit:
    def __init__(self, name_label: str):
        self.label = QLabel(name_label)
        self.line_edit = QLineEdit()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)

    def get_item(self):
        return self.layout


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.vertical_layout = QVBoxLayout(self)
        self.setWindowTitle("Добавить заметку")

        self.note_title = LabelLineEdit("Заголовок")
        self.vertical_layout.addLayout(self.note_title.get_item())

        self.vertical_layout.addWidget(QLabel("Описание"))

        self.text = QTextEdit()
        self.vertical_layout.addWidget(self.text)

        self.is_archive = QCheckBox("Отправить в архив")
        self.is_archive.hide()
        self.vertical_layout.addWidget(self.is_archive)

        self.btn_save = QPushButton("Сохранить")
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.vertical_layout.addWidget(self.btn_save)

        self.btn_exit = QPushButton("Выход")
        self.btn_exit.clicked.connect(self.btn_exit_clicked)
        self.vertical_layout.addWidget(self.btn_exit)

    def btn_save_clicked(self):
        title = self.note_title.line_edit.text()
        text = self.text.toPlainText()

        if not title:
            msg = InfoMessageBox("Ошибка!", "Необходимо добавить заголовок!")
            msg.show()
            return

        if not text:
            msg = InfoMessageBox("Ошибка!", "Необходимо добавить описание заметки!")
            msg.show()
            return

        write_file(title, text)
        self.close()

    def btn_exit_clicked(self):
        self.close()


class EditForm(Form):
    def __init__(self, title, text, arc=False):
        super(EditForm, self).__init__()

        self.setWindowTitle("Изменить заметку")
        self.note_title.line_edit.setText(title)
        self.note_title.line_edit.setReadOnly(True)
        self.text.setText(text)

        self.is_archive.show()
        if arc:
            self.is_archive.setChecked(True)

    def btn_save_clicked(self):
        title = self.note_title.line_edit.text()
        text = self.text.toPlainText()

        if not text:
            msg = InfoMessageBox("Ошибка!", "Необходимо добавить описание заметки!")
            msg.show()
            return

        if self.is_archive.isChecked():
            write_file_in_archive(title, text)
            self.close()

        else:
            write_file(title, text)
            self.close()
