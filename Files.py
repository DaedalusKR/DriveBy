import os
from PyQt5.QtWidgets import *

#B_to_GB = 1073741824
B_to_GB = 1000000000
B_to_MB = 1048576
B_to_KB = 10254


# inspect directory, for each file: strip out temp files, add to treewidgetitem and get size
def get_dir(path):

    tree_structure = QTreeWidgetItem()  # top tree struct init as selected path - when complete return to caller
    top_path_size = 0  # top directory size tracker

    #  return the size of the top directory being parsed and add its contents to a child tree widget
    add_dirs_to_tree(path, tree_structure, top_path_size) #+ get_top_dir_size(path)
    tree_structure.setText(0, path)
    tree_structure.setText(1, str(convert_from_bytes(get_dir_size(path))) + dir_measure(get_dir_size(path)))# str(convert_from_bytes(t_size)) + dir_measure(t_size))

    return tree_structure

def add_dirs_to_tree(path, tree_structure, top_path_size):  # go through each directory and add treewidget for each dir and file

    dir_list = os.listdir(path)

    for top_dir_file in dir_list:

        tree_structure_dir = QTreeWidgetItem()  # treewidget to be added to the top dir treewidget

        # search through top dir adding its files
        if not os.path.isdir(top_dir_file) \
                and not top_dir_file.startswith('.') \
                and not top_dir_file.startswith('~') \
                and not os.path.islink(os.path.join(path, top_dir_file)):

            # print(os.path.join(path, top_dir_file))  # show file being parsed in the log
            tree_structure_dir.setText(0, top_dir_file)
            tree_structure_dir.setText(1, str(convert_from_bytes(os.path.getsize(os.path.join(path, top_dir_file)))) + file_measure(os.path.join(path, top_dir_file)))
            tree_structure.addChild(tree_structure_dir)

        # when find a directory add its contents to the tree
        if os.path.isdir(os.path.join(path, top_dir_file)) \
                and not top_dir_file.startswith('.') \
                and not top_dir_file.startswith('~') \
                and not os.path.islink(os.path.join(path, top_dir_file)):

            file_list = os.listdir(os.path.join(path, top_dir_file))
            for file in file_list:
                if not file.startswith('.') \
                        and not file.startswith('~') \
                        and not os.path.isdir(os.path.join(path, top_dir_file, file)) \
                        and not os.path.islink(os.path.join(path, top_dir_file, file)):

                    file_size = os.path.getsize(os.path.join(path, top_dir_file, file))
                    top_path_size += file_size
                    # print(os.path.join(path, file))  # show file being parsed in the log
                    tree_structure_dir.setText(1, str(convert_from_bytes(get_dir_size(os.path.join(path, top_dir_file)))) + dir_measure(get_dir_size(os.path.join(path, top_dir_file))))
            add_dirs_to_tree(os.path.join(path, top_dir_file), tree_structure_dir, top_path_size)
    return


def get_top_dir_size(path):  # return size of top directory parsed
    top_dir_contents = os.listdir(path)
    t_dir_size = 0
    for file in top_dir_contents:
        t_dir_size += get_file_stats(os.path.join(path, file))
    return t_dir_size


def convert_from_bytes(size):
    if size >= B_to_GB:
        size = size/B_to_GB
    elif size >= B_to_MB:
        size = size/B_to_MB
    elif size > 0:
        size = round(size/B_to_KB*10)
        return size

    return round(size, 2)


def file_measure(file):
    size = os.path.getsize(file)
    measure = ''
    if size >= B_to_GB:
        measure = ' GB'
    elif size >= B_to_MB:
        measure = ' MB'
    elif size > 0:
        measure = ' KB'

    return measure


def dir_measure(size):
    measure = ''
    if size >= B_to_GB:
        measure = ' GB'
    elif size >= B_to_MB:
        measure = ' MB'
    elif size > 0:
        measure = ' KB'
    return measure


def get_dir_size(path):
    size_of_dir = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if not os.path.islink(os.path.join(dirpath, f)):
                fp = os.path.join(dirpath, f)
                size_of_dir += os.path.getsize(fp)
    return size_of_dir
