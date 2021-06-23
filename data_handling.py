import os
import itertools


def makedir(path):
    # Create target Directory if doesn't exist
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory ", path, " Created ")
    else:
        print("Directory ", path, " already exists")

    return path

def get_files(path):
    def full_path(file, path):
        return os.path.join(path, file)
    files = os.listdir(path)
    return map(full_path, files, itertools.repeat(path))
