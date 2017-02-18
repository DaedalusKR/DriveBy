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

    for f in dir_list:

        if os.path.isdir(os.path.join(path, f)) and not f == 'Library' and not f.startswith('.'):
            tree_structure_dir = QTreeWidgetItem()
            tree_structure_dir.setText(0, f)
            y = os.listdir(os.path.join(path, f))

            for x in y:  # having to exclude Library because of alias files - need to think about how to do this
                if not x == 'RunningChromeVersion' and  not x.startswith('Singleton')  and not x.startswith('.') and not x.startswith('~') and not os.path.isdir(os.path.join(path, f, x)):
                    # appends dir path to filename
                    file_size = get_file_stats(os.path.join(path, f, x))

                    # create line for each file in tree and build dict for file and add to it
                    tree_structure_children = QTreeWidgetItem()
                    file_data = {'fName': x, 'fSize': file_size, 'fDir': os.path.join(path, x)}
                    tree_structure_children.setText(0, file_data['fName'])
                    tree_structure_children.setText(1, str(file_data['fSize']))
                    tree_structure_dir.addChild(tree_structure_children)

                tree_structure.addChild(tree_structure_dir)
            add_dirs_to_tree(os.path.join(path, f), tree_structure_dir)

    return
