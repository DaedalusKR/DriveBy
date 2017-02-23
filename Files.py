import os
from PyQt5.QtWidgets import *


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):
    tree_structure = QTreeWidgetItem()  # top tree struct init as selected path

    top_path_size = 0
    t_size = add_dirs_to_tree(path, tree_structure, top_path_size) + get_top_dir_size(path)
    tree_structure.setText(0, path)
    tree_structure.setText(1, str(t_size))
    return tree_structure


def get_file_stats(file):
    size = os.path.getsize(file)
    return size


def get_top_dir_size(path):
    top_dir_contents = os.listdir(path)
    t_dir_size = 0
    for file in top_dir_contents:
        t_dir_size += get_file_stats(os.path.join(path, file))
    return t_dir_size


def add_dirs_to_tree(path, tree_structure, top_path_size):
    dir_list = os.listdir(path)

    top_path_size = 0


    for top_dir_file in dir_list:

        tree_structure_dir = QTreeWidgetItem()

        # file for top dir
        if not os.path.isdir(top_dir_file) and not top_dir_file.startswith('.') and not top_dir_file.startswith('~') and not os.path.islink(top_dir_file):
            tree_structure_dir.setText(0, top_dir_file)
            tree_structure_dir.setText(1, str(get_file_stats(os.path.join(path, top_dir_file))))
            tree_structure.addChild(tree_structure_dir)
            #top_path_size += get_file_stats(os.path.join(path, top_dir_file))

        dir_size = 0
        if os.path.isdir(os.path.join(path, top_dir_file)) and not top_dir_file.startswith('.') and not top_dir_file.startswith('~') and not os.path.islink(os.path.join(path, top_dir_file)):

            file_list = os.listdir(os.path.join(path, top_dir_file))

            for file in file_list:
                if not file.startswith('.') and not file.startswith('~') and not os.path.isdir(os.path.join(path, top_dir_file, file)) and not os.path.islink(os.path.join(path, top_dir_file, file)):
                    # appends dir path to filename
                    file_size = get_file_stats(os.path.join(path, top_dir_file, file))
                    dir_size += file_size
                    top_path_size += file_size

            tree_structure_dir.setText(1, str(dir_size))
            add_dirs_to_tree(os.path.join(path, top_dir_file), tree_structure_dir, top_path_size)
    return top_path_size

