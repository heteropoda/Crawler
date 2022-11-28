
import os


def check_dir(path):
    return os.path.isdir(path)

def check_dir_create(path):
    if not check_dir(path):
        os.makedirs(path)
    return path