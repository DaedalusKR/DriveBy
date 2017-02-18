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
        self.tree_view.setColumnWidth(0, 450)
        self.tree_view.setColumnWidth(1, 150)

    def plant_tree(self):
        # tree view titles take a list for multiple columns so build this and pass it
        tree_labels = ['Files', 'Size']
        self.tree_view.setHeaderLabels(tree_labels)

        # get data from scan function
        tree_data = get_dir(self.path_to_scan)
        self.tree_view.addTopLevelItem(tree_data)