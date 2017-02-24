from Files import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import *


path_selected = '/Users/kenroberts/Downloads'



def main():
    app = QApplication(sys.argv)
    ui = main_view(path_selected)
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()