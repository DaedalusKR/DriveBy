from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class main_view(QWidget):
    def __init__(self, data):
        super().__init__()
        self.tree_view = QTreeWidget(self)

        self.setup_ui()
        self.plant_tree(data)
        self.show()

    def setup_ui(self):
        # create the tree view, num of columns and size
        self.tree_view.resize(600,600)
        self.tree_view.setColumnCount(2)
        self.tree_view.setColumnWidth(0,400)
        self.tree_view.setColumnWidth(1,200)

    def plant_tree(self, data):
        # tree view titles take a list for multiple columns so build this and pass it
        tree_labels = ['Files', 'Size']
        self.tree_view.setHeaderLabels(tree_labels)

        # -- Data structure key --
        # data[x] = the directory
        # data[x][y] = file data where x = dir and y = file.stats grabbed

        # unpack the data into an array called file_list for easier processing. format the file size value to int
        file_list = []
        for dir in range(len(data)):
            for file in range(len(data[dir])):
                file_name_to_add = data[dir][file]['fName']
                file_size_to_add = data[dir][file]['fSize']
                file_dir_to_add = data[dir][file]['fDir']
                file_data = [file_name_to_add, str(file_size_to_add), file_dir_to_add]
                file_list.append(file_data)

        # directory object for tree view - set directory name as text for A, X
        top_line = QTreeWidgetItem()
        top_line.setText(0, file_list[0][2])

        #calcualtes the size of the directory by summing file_list size data
        dir_size = 0
        for file in range(len(file_list[0])):
            dir_size += int(file_list[file][1])

        # Show file/dir sizes in B, X
        top_line.setText(1, str(dir_size))

        # use above to build the child object and add to directory object - a row for each file/dir -- (name + size)
        for x in range(len(file_list[0])):
            top_line_children = QTreeWidgetItem()
            top_line_children.setText(0, file_list[x][0])
            top_line_children.setText(1, file_list[x][1])
            top_line.addChild(top_line_children)
            self.tree_view.addTopLevelItem(top_line)