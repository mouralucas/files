import os, sys


def list_files(filepath):
    infos = {
        'file_name': [],
        'file_path': [],
        'dir_name': [],
        'dir_path': [],
        'complete_path': [],
    }

    with os.scandir(filepath) as lstdir:
        for e in lstdir:
            if e.is_file():
                infos['file_name'].append(e.name)
                infos['file_path'].append(e.path)
            elif e.is_dir:
                infos['dir_name'].append(e.name)
                infos['dir_path'].append(e.path)

    return infos


def listdir(d):
    if not os.path.isdir(d):
        # print(d)
        pass
    else:
        print(d)
        for item in os.listdir(d):
            # print(item)
            listdir(item)


def list_files_recursive(path):
    file_list = []
    dir_list = []

    for root, directories, filenames in os.walk(path):
        for directory in directories:
            # print(os.path.join(root, directory))
            dir_list.append(os.path.join(root, directory))

        for filename in filenames:
            # print(os.path.join(root, filename))
            file_list.append(os.path.join(root, filename))

    return file_list, dir_list
