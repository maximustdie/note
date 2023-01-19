import os


def write_file(title, text):
    with open(f'files/{title}.txt', 'w') as opened_file:
        opened_file.write(text)
        try:
            delete_file_in_archive(title)
        except:
            pass


def write_file_in_archive(title, text):
    with open(f'archive_files/{title}.txt', 'w') as opened_file:
        opened_file.write(text)
        try:
            delete_file(title)
        except:
            pass


def get_file_names(dir_name):
    path = os.getcwd() + dir_name
    return os.listdir(path)


def get_list_notes(dir_name):
    return [name[:-4] for name in get_file_names(dir_name)]


def delete_file(name_file):
    path = os.getcwd() + "/files/" + name_file + ".txt"
    os.remove(path)


def delete_file_in_archive(name_file):
    path = os.getcwd() + "/archive_files/" + name_file + ".txt"
    os.remove(path)


def read_file(name_file, dir="files"):
    path = os.getcwd() + f"/{dir}/" + name_file + ".txt"
    with open(path, 'r') as opened_file:
        return opened_file.read()
