from analyze import find_onsets
from data_handling import *
from slicer import Slicer
from note import Note
import argparse

parser = argparse.ArgumentParser(description='arguments')
parser.add_argument("input", help="Source files directory", type=str)
parser.add_argument("output", help="Output files directory", type=str)
args = parser.parse_args()

print()

print('input - ', args.input)
print('output -', args.output)

print()

path_in = args.input
path_out = args.output

makedir(path_out)

files = get_files(path_in)

for file in files:
    onsets = find_onsets(file)
    note = Note(file)
    for onset in onsets:
        note.rewind_to(onset)
        postfix = str(note.detect_max())
        name = postfix + str(file)
        slicer = Slicer(file, onset)
        slicer.slice(onset, note.duration())
        print('onset = ', onset)
        print('duration = ', note.duration())
    note.close()
