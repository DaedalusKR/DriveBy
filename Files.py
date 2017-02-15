import os


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):

    found_dirs = []
    drive = []
    directory_files = []
    for (paths, dirs, files) in os.walk(path):
        found_dirs.append(paths)

    for name in found_dirs:
        for file in os.listdir(os.path.join(paths, name)):
            if not file.startswith('.') and not file.startswith('~'):
                # appends dir path to filename
                file_size = get_file_stats(os.path.join(paths, name, file))

                # build dict for file and add to list
                file_data = {'fName': file, 'fSize': file_size, 'fDir': os.path.join(paths, name)}
                directory_files.append(file_data)
                directory_files_sorted_keys = sorted(directory_files, key=lambda k: k['fSize'], reverse = True)
                directory_files = directory_files_sorted_keys

        drive.append(directory_files)
        directory_files = []
    return drive


def get_file_stats(file):
    size = os.path.getsize(file)
    return size