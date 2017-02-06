from Files import *

path_selected = '/Users/kenroberts/Downloads'
found_dirs = get_dir(path_selected)

i = len(found_dirs)

for x in range(i):
    file_name = found_dirs[x][0]['fName']
    file_size = found_dirs[x][0]['fSize']
    print(file_name + " -- " + str(file_size))

