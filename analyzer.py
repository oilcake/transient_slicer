def find_onsets(filename):
    win_s = 16  # fft size
    hop_s = win_s // 2  # hop size
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


# /path_in/A1.aif
# /path_in/A2.aif
