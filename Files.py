import os
from PyQt5.QtWidgets import *


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):
    tree_structure = QTreeWidgetItem()  # top tree struct init'd as selected path
    tree_structure.setText(0, path)
    tree_structure.setText(1, str(add_dirs_to_tree(path, tree_structure)))
    #add_dirs_to_tree(path, tree_structure)
    return tree_structure


def add_dirs_to_tree(path, tree_structure):
    dir_list = os.listdir(path)
    dir_total_size = 0

    for dir in dir_list:
        # get each directory, if complies with checks then setup tree line for  it
        dir_size = 0

        if os.path.isdir(os.path.join(path, dir)) and not dir.startswith('.') and not dir.startswith('~') and not os.path.islink(os.path.join(path, dir)):
            tree_structure_dir = QTreeWidgetItem()
            tree_structure_dir.setText(0, dir)
            dir_contents = os.listdir(os.path.join(path, dir))
            for file_data in dir_contents:
                size = os.path.getsize(os.path.join(path, dir, file_data))
                dir_size += size
            tree_structure_dir.setText(1, str(dir_size))
            dir_total_size += dir_size


            # get the contents of the dir being added
            for file in dir_contents:
                #print(os.path.join(path, file))  # see what file being parsed in the log

                # if file complies with checks and not an alias file (for OSX) then build the child
                if not file.startswith('.') and not file.startswith('~') and not os.path.isdir(os.path.join(path, dir, file)) and not os.path.islink(os.path.join(path, dir, file)):
                    file_size = get_file_stats(os.path.join(path, dir, file))

                    # create line for each file in tree and build dict for file and add to it
                    tree_structure_children = QTreeWidgetItem()
                    file_data = {'fName': file, 'fSize': file_size, 'fDir': os.path.join(path, file)}
                    tree_structure_children.setText(0, file_data['fName'])
                    tree_structure_children.setText(1, str(file_data['fSize']))
                    tree_structure_dir.addChild(tree_structure_children)
                    tree_structure.addChild(tree_structure_dir)

            # recurse using the last directory parsed - this is what maintains the file structure hierarchy
            add_dirs_to_tree(os.path.join(path, dir), tree_structure_dir)
    return dir_total_size


def get_file_stats(file):
    size = os.path.getsize(file)
    return size


