import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import *
from Files import *


def get_scan_count(path):
    number_of_scans = 0
    for dirpath, dirnames, filenames in os.walk(path):
        number_of_scans += len(filenames)
    return number_of_scans


def main():
    app = QApplication(sys.argv)
    ui = drive_select_view()
    # main_view(path_selected)
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()

path_selected = "/Users/kenroberts/Downloads"
progress_count = get_scan_count(path_selected)