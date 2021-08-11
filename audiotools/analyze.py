import os
from aubio import source, onset


def find_onsets(filename):

    print()

    if os.path.isfile(filename):
        print('looking for onsets in', filename)
    else:
        print("Can't find your file")

    print()

    win_s = 16  # fft size
    hop_s = win_s // 2  # hop size
    samplerate = 0
    o = onset("default", win_s, hop_s, samplerate)

    o.set_threshold(2.1)

    with source(filename, samplerate, hop_s) as s:
        while True:
            samples, read = s()
            if o(samples):
                yield o.get_last()
            if read < hop_s:
                break
