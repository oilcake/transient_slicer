
import os, aifc
import numpy as np
from aubio import source, onset, sink
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input-dir", dest="input_dir", help="Source files directory")
parser.add_option("-o", "--output-dir", dest="output_dir", help="Output files directory")
(options, args) = parser.parse_args()

path_in = options.input_dir
path_out = options.output_dir

temporary_postfix = 'temporary/'
global WIN_S_OUT
global HOP_S_OUT
global one_note_out
one_note_out = []

WIN_S_OUT = 16384  # fft size
HOP_S_OUT = WIN_S_OUT // 2  # hop size

def find_onsets(filename):
    win_s = 16  # fft size
    hop_s = win_s // 2  # hop size
    # nonlocal samplerate
    samplerate = 0
    o = onset("default", win_s, hop_s, samplerate)

    o.set_threshold(2.1)

    # list of onsets, in samples
    global onsets
    onsets = []

    with source(filename, samplerate, hop_s) as s:
        samplerate = s.samplerate

        while True:
            samples, read = s()
            if o(samples):
                onsets.append(o.get_last())
            if read < hop_s: break
        del s
        print('number of onsets = ', len(onsets))

    return onsets
def transient_slicer(filename, onsets, path, file_in):
    path_temp = path + temporary_postfix
    if not os.path.exists(path_temp):
        os.mkdir(path_temp)
        print("Directory ", path_temp, " Created ")
    else:
        print("Directory ", path_temp, " already exists")



    with aifc.open(filename, 'r') as source_file:
        count = 0
        params = (source_file.getparams())
        for address in onsets:
            print('write onset count', count)
            ##         print(cunt)
            source_file.setpos(address)
            step_ahead = onsets.index(address) + 1
            if step_ahead == len(onsets):
                gap = source_file.getnframes() - address
            else:
                gap = onsets[step_ahead] - address
            one_note = source_file.readframes(gap)

            filename_temp = path_temp + file_in + '_tmp_' + str(count) + '.aif'
            if not os.path.isfile(filename_temp):
                with aifc.open(filename_temp ,'w') as bigdick:
                    bigdick.setparams(params)
                    bigdick.writeframes(one_note)
            else:
                print('file exists')
            count += 1
    print("temporary files are writen")
    return params
def find_biggest_dick_and_stop_point(filename_given):

    stop_point = 0
    samplerate = 0
    silence = 0.0001


    with source(filename_given, samplerate, HOP_S_OUT) as s_out:
        biggest_dick = 0
        total_frames = 0
        for frames in s_out:
            total_frames += HOP_S_OUT
            stop_point = total_frames
            balls = 0
            one_note_out.extend(frames)

            ##            print('FRAMES' + str(total_frames))
            for sample_value in frames:
                shmabs = abs(sample_value)
                balls += shmabs
                if biggest_dick < shmabs:
                    biggest_dick = shmabs
            square_balls = balls / HOP_S_OUT
#            print('FRAMES-' + str(total_frames))
            if square_balls < silence:
                break
            if len(frames) < HOP_S_OUT:
                break
        file_info = [biggest_dick, stop_point]
    return file_info

def file_out(params, path, file_info, file_name_mask):
    filename_out = path + '/' + file_name_mask + str(file_info[0])[:7] + '.aif'
    if not os.path.isfile(filename_out):
        with aubio.sink(filename_out, 48000, 2) as src:
            src(fvec(one_note_out))
        print("zapisal")
    else:
        print('ooo shiiit it is already taken')



def find_or_create_directory_for(filename):
    # TODO: should we really rely on note names?
    # Add --prefix-separator parameter
    if file_in[4] == '#':
        note_prefix = file_in[0:6]
    else:
        note_prefix = file_in[0:5]

    note_prefix += '_'

    path = path_out + note_prefix + '/'

    print('out path is', path)
    # Create target Directory if doesn't exist
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory ", path, " Created ")
    else:
        print("Directory ", path, " already exists")

    return path


# TODO: add wav functionality
def audio_files_within(path):
    all_files = os.listdir(path)
    return filter(lambda file : file[-4:] == '.aif', all_files)

for file_in in audio_files_within(path_in):
    filename = path_in + '/' + file_in

    path = find_or_create_directory_for(filename)

    find_onsets(filename)
    params = transient_slicer(filename, onsets, path, file_in)

for folder in os.listdir(path_out):
    print(folder)
    if folder[:4] == '.DS_':
        continue
    path_inside = path_out + folder + '/' + temporary_postfix
    for sliced_stuff in os.listdir(path_inside):
        print(sliced_stuff)
        if sliced_stuff[-4:] != '.aif':
            print("ooohhh shhiiitt it is not audio")
            continue

        file_info = find_biggest_dick_and_stop_point(path_inside + sliced_stuff)

        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', file_info)
        if file_info[0] < 0.01:
            print('dick is too small')
            continue
        else:
            print('dick is ok')
        if file_info[1] < 8000:
            print('too short')
            continue

print('Egooooooooooooooooor, value for value')
