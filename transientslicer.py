from housekeeping.datahandling import makedir, get_files
from audiotools.analyze import find_onsets
from audiotools.note import Note
from audiotools.slicer import Slicer
# from aubio import source
import aubio
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
    sample = aubio.source(file, samplerate=0, hop_size=64)
    for onset in onsets:
        note = Note(sample, onset)
        print(file, 'onset = ', onset)
        print('duration = ', note.duration)
        print('max value = ', note.max)
    sample.close()
