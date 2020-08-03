
import os, aifc
import numpy as np
from aubio import source, onset, sink

path_in = '/Volumes/STUFF/[SAMPLES]/Xylophone/TUNED_mono'
path_out = "/Volumes/STUFF/[SAMPLES]/Xylophone/script_check/OUT/"
temporary_postfix = 'temporary/'
# global file_info
# file_info = []
# global onsets
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


    #    print('slicing file', str(filename))

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
                # print('this is the end of file')
            else:
                gap = onsets[step_ahead] - address
            one_note = source_file.readframes(gap)
            # for list_value in range(0, gap, 10000):
            #     print(list_value)

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

#    print('kokoko')
#     win_s_out = 16384                # fft size
#     hop_s_out = win_s_out // 2       # hop size
    stop_point = 0
    samplerate = 0
    silence = 0.0001
    # global file_info


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
    # with aubio.source(filename, 0, HOP_S_OUT) as tmpr_file:
        # for frames in tmpr_file:

            # tmpr_file.rewind()
            # print('prochital')
            # tmpr_file.setpos(0)
            # one_note_out = np.array(tmpr_file.readframes(file_info[1]))
    # print('otkryl skopiroval i zakryl')
    filename_out = path + '/' + file_name_mask + str(file_info[0])[:7] + '.aif'
    if not os.path.isfile(filename_out):
        with aubio.sink(filename_out, 48000, 2) as src:
            src(fvec(one_note_out))
            # out_now.setparams(params)
            # print(bytes(one_note_out))
            # out_now.writeframes(bytes(one_note_out))
        print("zapisal")
    else:
        print('ooo shiiit it is already taken')
    # print('result length', len(one_note_out))
    return


for file_in in os.listdir(path_in):
    filename = path_in + '/' + file_in
    if file_in[-4:] != '.aif':
        print("ooohhh shhiiitt it is not audio")
        continue
    if file_in[4] == '#':
        note_prefix = file_in[0:6]
    else:
        note_prefix = file_in[0:5]

    note_prefix += '_'

    path = path_out + note_prefix + '/'

    print('out path is', path)
    # Create target Directory if don't exist
    if not os.path.exists(path):
        os.mkdir(path)
        print("Directory ", path, " Created ")
    else:
        print("Directory ", path, " already exists")
    find_onsets(filename)

    params = transient_slicer(filename, onsets, path, file_in)
# print('files are sliced')

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
        # file_out(params, path_out + folder, file_info, folder)

print('Egooooooooooooooooor, value for value')
