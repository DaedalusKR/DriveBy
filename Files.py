import os
from PyQt5.QtWidgets import *


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):

    found_dirs = []  # holds paths
    tree_structure = QTreeWidgetItem()  # top tree struct init as selected path
    tree_structure.setText(0, path)

    for (paths, dirs, files) in os.walk(path):  # loops x times where x = n paths. Add found paths to found_dirs list
        found_dirs.append(paths)

    for name in found_dirs:  # get each path name and create a tree for it, add it to top level ready for populating
        tree_structure_dir = QTreeWidgetItem()
        tree_structure_dir.setText(0, name)
        tree_structure.addChild(tree_structure_dir)

        for file in os.listdir(os.path.join(paths, name)):  # for each file check it complies and add to tree for path
            if not file.startswith('.') and not file.startswith('~'):
                # appends dir path to filename
                file_size = get_file_stats(os.path.join(paths, name, file))

                # create line for each file in tree and build dict for file and add to it
                tree_structure_children = QTreeWidgetItem()
                file_data = {'fName': file, 'fSize': file_size, 'fDir': os.path.join(paths, name)}
                tree_structure_children.setText(0, file_data['fName'])
                tree_structure_children.setText(1, str(file_data['fSize']))
                tree_structure_dir.addChild(tree_structure_children)

    return tree_structure  # return QTreeWidgetItem() directly into the UI creation functions


def get_file_stats(file):
    size = os.path.getsize(file)
    return size