from Files import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import *


path_selected = '/Users/kenroberts'

print(os.path.islink('/Users/kenroberts/Library/Application Support/Google/Chrome/RunningChromeVersion'))

# #found_dirs = get_dir(path_selected)
#
# print(os.path.isfile('/Users/kenroberts/Library/Application Support/Google/Chrome/RunningChromeVersion'))
#
# file_test = open('/Users/kenroberts/Library/Application Support/Google/Chrome/RunningChromeVersion', 'r')
# bytes = file_test.read(150)
# print(bytes)




def main():
    app = QApplication(sys.argv)
    ui = main_view(path_selected)
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = main()
    app.run()