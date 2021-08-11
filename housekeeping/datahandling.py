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
    files = os.listdir(path)
    return map(os.path.join, itertools.repeat(path), files)
