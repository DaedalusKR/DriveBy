from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class main_view(QWidget):
    def __init__(self, data):
        super().__init__()

        self.setup_ui(data)
        self.show()

    def setup_ui(self, data):
        self.tree_view = QTreeWidget(self)
        self.tree_view.resize(600,600)
        self.tree_view.setColumnCount(2)
        tree_labels = ['Files', 'Size']
        self.tree_view.setHeaderLabels(tree_labels)

        # data[x] = the directory
        # data[x][y] = file data where x = dir and y = file.stats grabbed

        file_list = []

        for dir in range(len(data)):
            for file in range(len(data[dir])):
                file_name_to_add = data[dir][file]['fName']
                file_size_to_add = data[dir][file]['fSize']
                file_dir_to_add = data[dir][file]['fDir']
                file_data = [file_name_to_add, file_size_to_add, file_dir_to_add]
                file_list.append(file_data)

        top_line = QTreeWidgetItem()
        top_line.setText(0, str(file_list[0][2]))

        file_names = []
        for i in range(len(file_list)):
           file_names.append(file_list[i][0])

        for i in range(3):
            top_line_children = QTreeWidgetItem([file_names[i]])
            top_line.addChild(top_line_children)

        self.tree_view.addTopLevelItem(top_line)