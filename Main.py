from Files import *

path_selected = '/Users/kenroberts/Downloads'
directory = os.listdir(path_selected)
files = get_dir(path_selected)

# for path in paths:

#
#     for dirs in directorys:
#          print(dirs)

#
for file in files:
    print(str(file['fName']) + " " + str(file['fSize']))