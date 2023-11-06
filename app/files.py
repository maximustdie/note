import os
import shutil


def copy_file(src, dist):
    shutil.copy(src, dist)


def write_file(title, text, xls_path):
    try:
        os.mkdir(f"files/{title}")
    except:
        pass

    with open(f'files/{title}/{title}.txt', 'w') as opened_file:
        opened_file.write(text)
        try:
            delete_file_in_archive(title)
        except:
            pass


def write_file_in_archive(title, text, xls_path):
    try:
        os.mkdir(f"archive_files/{title}")
    except:
        pass

    with open(f'archive_files/{title}/{title}.txt', 'w') as opened_file:
        opened_file.write(text)
        try:
            delete_file(title)
        except:
            pass


def get_dir_names(dir_name):
    path = os.getcwd() + dir_name
    return os.listdir(path)


def get_list_notes(dir_name):
    return [name for name in get_dir_names(dir_name)]


def delete_file(name_file):
    path_file = os.getcwd() + f"/files/{name_file}/" + name_file + ".txt"
    os.remove(path_file)

    path_dir = os.getcwd() + f"/files/{name_file}/"
    os.rmdir(path_dir)


def delete_file_in_archive(name_file):
    path_file = os.getcwd() + f"/archive_files/{name_file}/" + name_file + ".txt"
    os.remove(path_file)

    path_dir = os.getcwd() + f"/archive_files/{name_file}/"
    os.rmdir(path_dir)


def read_file(name_file, dir="files"):
    path = os.getcwd() + f"/{dir}/{name_file}/" + name_file + ".txt"
    with open(path, 'r') as opened_file:
        return opened_file.read()
