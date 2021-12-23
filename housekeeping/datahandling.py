import os
import itertools

SUPPORTED = ('.wav', '.aiff', '.aif')


def makedir(path):
    # Create target Directory if doesn't exist
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory ", path, " Created ")
    else:
        print("Directory ", path, " already exists")
    return path


def supported(filename):
    return os.path.splitext(filename)[1] in SUPPORTED


def get_files(path):
    files = filter(supported, os.listdir(path))
    return map(os.path.join, itertools.repeat(path), files)
