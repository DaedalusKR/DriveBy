from Files import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import *

path_selected = '/Users/kenroberts/Downloads'
found_dirs = get_dir(path_selected)
num_dirs = len(found_dirs)


def run():
    for dir_count in range(num_dirs):
        #testing the data structure
        num_files = len(found_dirs[dir_count])
        print('')
        print('----------------' + str(found_dirs[dir_count][0]['fDir']) + '------------')
        show_file_list(num_files, dir_count)
        print('')

def show_file_list(num_files, dir_count):

    for file_count in range(num_files):
        file_name = found_dirs[dir_count][file_count]['fName']
        file_size = found_dirs[dir_count][file_count]['fSize']
        print(file_name + " -- " + str(file_size))


def main():
    app = QApplication(sys.argv)
    ui = main_view(found_dirs)
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()