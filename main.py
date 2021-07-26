import os, aifc
from analyze import find_onsets
from data_handling import *
from aubio import source, onset, sink
from slicer import *
import argparse

def process_file(file):
    onsets = find_onsets(file)
    data = Source()
    transients = map()

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
    editor = 
    ln = get_duration(onsets)
    slices = slice(onsets, ln)
    power = get_power(slice)
    for onset in onsets:
        print(onset)
