import os
import sys



def remove_hidden(path):
    stripped_files = []
    for file in os.listdir(path):
        if not file.startswith('.') and not file.startswith('~'):
            file_size = get_file_stats(path+'/'+file)
            file_data = {'fName': file, 'fSize': file_size}
            stripped_files.append(file_data)


    return stripped_files

def get_file_stats(file):
     size = os.path.getsize(file)
     return size


path = '/Users/kenroberts/Downloads'

directory = os.listdir(path)
files = remove_hidden(path)



#filestats = os.stat(path)
#file_size = filestats.st_size

for file in files:
    print(str(file['fName']) + " " + str(file['fSize']))