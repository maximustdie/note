import os


def write_file(title, text):
    with open(f'files/{title}.txt', 'w') as opened_file:
        opened_file.write(text)


def get_file_names(dir_name):
    path = os.getcwd() + dir_name
    return os.listdir(path)


def delete_file(name_file):
    path = os.getcwd() + "\\files\\" + name_file
    os.remove(path)


def read_file(name_file):
    path = os.getcwd() + "\\files\\" + name_file
    with open(path, 'r') as opened_file:
        return opened_file.read()
