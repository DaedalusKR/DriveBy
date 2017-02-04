from Files import *

path = '/Users/kenroberts/Downloads'
directory = os.listdir(path)
files = get_dir(path)

for file in files:
    print(str(file['fName']) + " " + str(file['fSize']))