from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Files import *

class main_view(QWidget):
    def __init__(self, path_selected):
        super().__init__()
        self.tree_view = QTreeWidget(self)
        self.path_to_scan = path_selected

        self.setup_ui()
        self.plant_tree()
        self.show()

    def setup_ui(self):
        # create the tree view, num of columns and size
        self.tree_view.resize(600,600)
        self.tree_view.setColumnCount(2)
        self.tree_view.setColumnWidth(0,450)
        self.tree_view.setColumnWidth(1,150)

    def plant_tree(self):
        # tree view titles take a list for multiple columns so build this and pass it
        tree_labels = ['Files', 'Size']
        self.tree_view.setHeaderLabels(tree_labels)

        # -- Data structure key --
        # data[x] = the directory
        # data[x][y] = the file
        # data[x][y][z] = files os.stats()

        #for dir in range(len(data)):

        # calcualtes the size of the directory by summing file_list size data
        # dir_size = 0
        # for file in range(len(data[dir])):
        #     dir_size += int(data[dir][file]['fSize'])
        #
        # # directory object for tree view
        # # set file name as text for A, X and file/dir sizes in B, X
        # top_line = QTreeWidgetItem()
        # top_line.setText(0, data[dir][0]['fDir'])
        # top_line.setText(1, str(dir_size))
        #
        # # use above to build the child object and add to directory object - a row for each file/dir -- (name + size)
        # for x in range(len(data[dir])):
        #     top_line_children = QTreeWidgetItem()
        #     top_line_children.setText(0, data[dir][x]['fName'])
        #     top_line_children.setText(1, str(data[dir][x]['fSize']))
        #     top_line.addChild(top_line_children)
        #     self.tree_view.addTopLevelItem(top_line)

        tree_data = get_dir(self.path_to_scan)
        self.tree_view.addTopLevelItem(tree_data)