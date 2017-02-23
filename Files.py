import os
from PyQt5.QtWidgets import *


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):
    tree_structure = QTreeWidgetItem()  # top tree struct init as selected path
    tree_structure.setText(0, path)
    add_dirs_to_tree(path, tree_structure)
    return tree_structure


def get_file_stats(file):
    size = os.path.getsize(file)
    return size


def add_dirs_to_tree(path, tree_structure):
    dir_list = os.listdir(path)

    for top_dir_file in dir_list:

        tree_structure_dir = QTreeWidgetItem()
        dir_size = 0  # for dir tree line file size

        # file for top dir
        if not os.path.isdir(top_dir_file) and not top_dir_file.startswith('.') and not top_dir_file.startswith('~') and not os.path.islink(top_dir_file):
            tree_structure_dir.setText(0, top_dir_file)
            tree_structure_dir.setText(1, str(get_file_stats(os.path.join(path, top_dir_file))))
            tree_structure.addChild(tree_structure_dir)
            top_dir_files = os.listdir(path)
            for file in top_dir_files:
                if not os.path.isdir(os.path.join(path, file)) and not file.startswith('.') and not file.startswith('~') and not os.path.islink(os.path.join(path, file)):
                    file_size = get_file_stats(os.path.join(path, file))

        dir_size = 0

        if os.path.isdir(os.path.join(path, top_dir_file)) and not top_dir_file.startswith('.') and not top_dir_file.startswith('~') and not os.path.islink(os.path.join(path, top_dir_file)):

            file_list = os.listdir(os.path.join(path, top_dir_file))

            for file in file_list:
                if not file.startswith('.') and not file.startswith('~') and not os.path.isdir(os.path.join(path, top_dir_file, file)) and not os.path.islink(os.path.join(path, top_dir_file, file)):
                    # appends dir path to filename
                    file_size = get_file_stats(os.path.join(path, top_dir_file, file))
                    dir_size += file_size

            tree_structure_dir.setText(1, str(dir_size))
            add_dirs_to_tree(os.path.join(path, top_dir_file), tree_structure_dir)
    return

