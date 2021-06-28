input
import os, aifc
import numpy as np
from analyze import *
from data_handling import *
from aubio import source, onset, sink
from optparse import OptionParser
from slicer import *
import argparse

def process_file(file):
    onsets = find_onsets(file)
    transients = map()

# parser = OptionParser()
# parser.add_option("-i", "--input-dir", dest="input_dir", help="Source files directory")
# parser.add_option("-o", "--output-dir", dest="output_dir", help="Output files directory")
# (options, args) = parser.parse_args()

parser = argparse.ArgumentParser(description='arguments')
# parser.add_argument("--i", '--input-dir', type=str, help='Source files directory')
# parser.add_argument("--o", "--output-dir", type=str, help="Output files directory")
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

# print()
# print()

#
# for file in files:
    # onsets = find_onsets(file)
    # print(file)
    # print(onsets)

# print()
# print()

onset_maps = map(find_onsets, files)

for map in onset_maps:
    for onset in map:
        print(onset)



# itr = map(find_onsets, files)
#
# print()
# print()
#
# print(list(itr))
# temporary_postfix = 'temporary'

# global WIN_S_OUT
# global HOP_S_OUT
# global one_note_out
# one_note_out = []

# WIN_S_OUT = 16384  # fft size
# HOP_S_OUT = WIN_S_OUT // 2  # hop size


# class Note:
#     def __init__(self, name, frames, file_params):
#         self.name = name
#         self.frames = frames
#         self.file_params = file_params
#
#     def tmp_persist(self):
#         if not os.path.isfile(self.filename_temp):
#             with aifc.open(self.filename_temp, 'w') as output:
#                 output.setparams(self.file_params)
#                 output.writeframes(self.frames)
#         else:
#             print('file exists')
#         # count += 1
#
#     def final_persist(self):
#         pass
#     def good_enough(self):
#         pass
#
#     def filename_temp(self):
#         # TODO: count?
#         # path_temp?
#         return path_temp + self.name + '_tmp_' + '.aif'
#

# source_file: /path_in/A1.aif
# def extract_notes_from(source_file):
#     onsets = find_onsets(source_file)
#     notes = []
#
#     for address in onsets:
#         source_file.setpos(address)
#         step_ahead = onsets.index(address) + 1
#         if step_ahead == len(onsets):
#             gap = source_file.getnframes() - address
#         else:
#             gap = onsets[step_ahead] - address
#
#         note_frames = source_file.readframes(gap)
#
#         name = "A1" # extracted from file  name
#         note = Note(name, note_frames, params)
#         notes.append(note)
#         note.tmp_persist()  # writes note to the filesystem
#
#     return notes



# for note in extract_notes_from(source_file):
#     if note.good_enough():
#         note.final_persist()





# def file_out(params, path, file_info, file_name_mask):
#     filename_out = path + '/' + file_name_mask + str(file_info[0])[:7] + '.aif'
#     if not os.path.isfile(filename_out):
#         with aubio.sink(filename_out, 48000, 2) as src:
#             src(fvec(one_note_out))
#         print("zapisal")
#     else:
#         print('ooo shiiit it is already taken')
#


# def find_or_create_directory_for(filename):
#     # TODO: should we really rely on note names?
#     # Add --prefix-separator parameter
#     if file_in[4] == '#':
#         note_prefix = file_in[0:6]
#     else:
#         note_prefix = file_in[0:5]
#
#     note_prefix += '_'
#
#     path = path_out + note_prefix + '/'
#
#     print('out path is', path)






# TODO: add wav functionality
# def audio_files_within(path):

# for file_in in audio_files_within(path_in):
#     file = os.path.join(path_in, file_in)
#
#     path = find_or_create_directory_for(file)
#
#     # find_onsets(filename)
#     params = transient_slicer(file, onsets, path, file_in)
#
# for folder in os.listdir(path_out):
#     print(folder)
#     if folder[:4] == '.DS_':
#         continue
#     path_inside = path_out + folder + '/' + temporary_postfix
#     for sliced_stuff in os.listdir(path_inside):
#         print(sliced_stuff)
#         if sliced_stuff[-4:] != '.aif':
#             print("ooohhh shhiiitt it is not audio")
#             continue
#
#         file_info = find_biggest_dick_and_stop_point(path_inside + sliced_stuff)
#
#         print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', file_info)
#         if file_info[0] < 0.01:
#             print('dick is too small')
#             continue
#         else:
#             print('dick is ok')
#         if file_info[1] < 8000:
#             print('too short')
#             continue

print()
print('Egooooooooooooooooor, value for value')
