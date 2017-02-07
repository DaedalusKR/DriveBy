from Files import *

path_selected = '/Users/kenroberts/Downloads'
found_dirs = get_dir(path_selected)


num_dirs = len(found_dirs)

for dir_count in range(num_dirs):
    #testing the data structure
    num_files = len(found_dirs[dir_count])
    print('')
    print('----------------' + str(found_dirs[dir_count][0]['fDir']) + '------------')
    print('')
    for file_count in range(num_files):

        file_name = found_dirs[dir_count][file_count]['fName']
        file_size = found_dirs[dir_count][file_count]['fSize']
        print(file_name + " -- " + str(file_size))

