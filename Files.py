import os


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):

    found_dirs = []
    for (paths, dirs, files) in os.walk(path):
        for dir in dirs:
            found_dirs.append(dir)

    print(found_dirs)
    drive = []
    directory_files = []
    dir_counter = 0

    for i in found_dirs:

        if dir_counter == 0:
            dir = os.listdir(path)
        else:
            dir = os.listdir(path+'/'+i)

        for file in dir:
            if not file.startswith('.') and not file.startswith('~'):
                # appends dir path to filename
                if dir_counter == 0:
                    file_size = get_file_stats(path+'/')
                else:
                    file_size = get_file_stats(path + '/' + i + '/' + file)

                # build dict for file and add to list
                file_data = {'fName': file, 'fSize': file_size, 'fDir': path + '/' + i}
                directory_files.append(file_data)
                directory_files_sorted_keys = sorted(directory_files, key=lambda k: k['fSize'], reverse = True)
                directory_files = directory_files_sorted_keys

        drive.append(directory_files)
        directory_files = []
    return drive


def get_file_stats(file):
    size = os.path.getsize(file)
    return size
