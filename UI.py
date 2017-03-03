from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Files import *
from PyQt5.QtCore import *


class main_view(QWidget):
    def __init__(self, path_selected):
        super().__init__()

        self.drive_view = QWidget()
        self.vbox = QVBoxLayout()
        self.tree_view = QTreeWidget(self)

        self.vbox.addWidget(self.tree_view)
        self.path_to_scan = path_selected
        self.setup_ui()
        self.plant_tree()
        self.setLayout(self.vbox)
        self.show()
        # falling out of scope, look at battle for idea round this

    def setup_ui(self):
        # create the tree view, num of columns and size
        self.tree_view.resize(600,800)
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


class drive_select_view(QWidget):
    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.window.resize(400, 250)

        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)

        self.drive_list = QListWidget()
        self.drive_list.setAlternatingRowColors(True)
        self.drive_list.setIconSize(QSize(50, 50))
        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button = QPushButton('Close', self)
        self.inst_label = QLabel('Select Drive or Directory to Scan:')

        self.vbox.addWidget(self.inst_label)
        self.vbox.addWidget(self.drive_list)
        self.hbox.addWidget(self.ok_button)
        self.hbox.addWidget(self.cancel_button)
        self.vbox.addLayout(self.hbox)

        mount_list = os.listdir('/Volumes')
        print(mount_list)
        for item in mount_list:
            item_widget = QListWidgetItem()
            item_widget.setText(item)
            item_widget.setIcon(QIcon('hdd.ico'))
            self.drive_list.addItem(item_widget)
        folder_widget = QListWidgetItem()
        folder_widget.setText('Select a Directory')
        folder_widget.setIcon(QIcon('folder.ico'))
        self.drive_list.addItem(folder_widget)


        self.window.setLayout(self.vbox)
        self.window.show()

    def ok_clicked(self):
        path_selected = '/Volumes/' + self.drive_list.currentItem().text() + '/Users/kenroberts/Downloads'
        self.window.close()
        self.file_scan = main_view(path_selected)

