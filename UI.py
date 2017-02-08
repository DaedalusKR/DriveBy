from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

class main_view(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.show()


    def setup_ui(self):
        print('run setup')
        layout = QVBoxLayout()
        self.tree_view = QTreeWidget()
        self.tree_view.setColumnCount(2)
        tree_labels = ['Files', 'Size']
        self.tree_view.setHeaderLabels(tree_labels)
        layout.addWidget(self.tree_view)
        self.setLayout(layout)




