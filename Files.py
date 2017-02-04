import os


# inspect directory, for each file: strip out temp files and get size
def get_dir(path):
    directory_files = []
    for file in os.listdir(path):
        if not file.startswith('.') and not file.startswith('~'):
            # appends dir path to filename
            file_size = get_file_stats(path+'/'+file)

            # build dict for file and add to list
            file_data = {'fName': file, 'fSize': file_size}
            directory_files.append(file_data)

        directory_files_sorted_keys = sorted(directory_files, key=lambda k: k['fSize'], reverse = True)
        directory_files = directory_files_sorted_keys
    return directory_files

# show results
def get_file_stats(file):
     size = os.path.getsize(file)
     return size
