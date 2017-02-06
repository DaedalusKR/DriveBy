from Files import *

path_selected = '/Users/kenroberts/Downloads'
found_dirs = get_dir(path_selected)

for dirs in found_dirs:
    print(dirs)