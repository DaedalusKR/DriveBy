import os


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):
    directory_files = []
    drive = []
    file_paths = []
    list = []


    for (paths, dirs, files) in os.walk(path):

        # for name in dirs:
        #     print(os.path.join(paths, name))

        for name in files:
            list.append(os.path.join(paths, name))



        for file in list:
            if not file.startswith('.') and not file.startswith('~') and not os.path.isdir(file):
                # appends dir path to filename
                file_size = get_file_stats(file)

                # build dict for file and add to list
                file_data = {'fName': file, 'fSize': file_size, 'fDir': path}
                directory_files.append(file_data)
                directory_files_sorted_keys = sorted(directory_files, key=lambda k: k['fSize'], reverse = True)
                directory_files = directory_files_sorted_keys

        drive.append(directory_files)
        directory_files = []
    print(drive)
    return drive


def get_file_stats(file):
    size = os.path.getsize(file)
    return size