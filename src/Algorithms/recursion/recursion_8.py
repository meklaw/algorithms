import os


def find_all_files(path: str):
    dirs = []
    files = []
    return find_all_recursion(path, dirs, files)


def find_all_recursion(path: str, dirs: list, files: list):
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            files.append(item)
            continue
        dirs.append(os.path.join(path, item))
    if len(dirs) == 0:
        return files
    path = dirs.pop()
    return find_all_recursion(path, dirs, files)
