import os
from PyQt5.QtWidgets import *


B_to_GB = 1073741824
B_to_MB = 1048576
B_to_KB = 10254

# inspect directory, for each file: strip out temp files, add to treewidgetitem and get size
def get_dir(path):
    tree_structure = QTreeWidgetItem()  # top tree struct init as selected path - when complete return to caller
    top_path_size = 0  # top directory size tracker


    #  return the size of the top directory being parsed and add its contents to a child tree widget
    t_size = add_dirs_to_tree(path, tree_structure, top_path_size) + get_top_dir_size(path)
    tree_structure.setText(0, path)
    tree_structure.setText(1, str(t_size))

    return tree_structure


def get_file_stats(file):  # return size of parsed file
    size = os.path.getsize(file)

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


def get_top_dir_size(path):  # return suze of top directory parsed
    top_dir_contents = os.listdir(path)
    t_dir_size = 0
    for file in top_dir_contents:
        t_dir_size += get_file_stats(os.path.join(path, file))
    return t_dir_size


def add_dirs_to_tree(path, tree_structure, top_path_size):  # go through each directory and add treewidget for each dir and file
    dir_list = os.listdir(path)
    dir_size = 0

    for top_dir_file in dir_list:

        tree_structure_dir = QTreeWidgetItem()  # treewidget to be added to the top dir treewidget

        # search through top dir adding its files
        if not os.path.isdir(top_dir_file) \
                and not top_dir_file.startswith('.') \
                and not top_dir_file.startswith('~') \
                and not os.path.islink(os.path.join(path, top_dir_file)):

            print(os.path.join(path, top_dir_file))  # show file being parsed in the log

            tree_structure_dir.setText(0, top_dir_file)
            tree_structure_dir.setText(1, str(get_file_stats(os.path.join(path, top_dir_file))) + file_measure(os.path.join(path, top_dir_file)))
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

                    file_size = get_file_stats(os.path.join(path, top_dir_file, file))
                    dir_size += file_size
                    top_path_size += file_size
                    print(os.path.join(path, file))  # show file being parsed in the log

            size_to_show = get_size_to_show(dir_size)
            tree_structure_dir.setText(1, str(size_to_show))
            add_dirs_to_tree(os.path.join(path, top_dir_file), tree_structure_dir, top_path_size)
    return top_path_size


def get_size_to_show(dir_size):
    if dir_size >= B_to_GB:
        dir_size = str(dir_size/B_to_GB) + ' Gb'
    else:
        dir_size = str(dir_size/B_to_MB) + ' Mb'
    return dir_size