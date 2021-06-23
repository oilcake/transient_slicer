import os
from aubio import source, onset, sink


def find_onsets(filename):

    print()
    print(filename)

    if os.path.isfile(filename):
        print('I DO EXIST')
    else:
        print('SORRY BRO')

    print()

    win_s = 16  # fft size
    hop_s = win_s // 2  # hop size
    samplerate = 0
    o = onset("default", win_s, hop_s, samplerate)

    o.set_threshold(2.1)

    # list of onsets, in samples
    # global onsets
    onsets = []

    with source(filename, samplerate, hop_s) as s:
        samplerate = s.samplerate

        while True:
            samples, read = s()
            if o(samples):
                onsets.append(o.get_last())
            if read < hop_s: break
        # del s
        print('number of onsets = ', len(onsets))
    print(onsets)
    return onsets


def find_biggest_dick_and_stop_point(filename_given):

    stop_point = 0
    samplerate = 0
    silence = 0.0001


    with source(filename_given, samplerate, hop_s) as s:
        biggest_dick = 0
        total_frames = 0
        for frames in s:
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
