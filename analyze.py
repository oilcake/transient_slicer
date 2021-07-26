import os
from aubio import source, onset, sink


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
        samplerate = s.samplerate

        while True:
            samples, read = s()
            if o(samples):
                yield o.get_last()
            if read < hop_s: break


def detect_amplitude(filename):
    pass

def detect_duration(filename, onset):

    stop_point = 0
    samplerate = 0
    silence = 0.0001
    hop_s = 32
    position = onset

    with source(filename, samplerate, hop_s, position) as s:
        s.seek(position)
        max_volume = 0
        total_frames = 0
        for frames in s:
            total_frames += hop_s
            rms = np.sqrt(np.mean(s**2))
            if rms < silence:
                break
            if len(frames) < hop_s:
                break
        file_info = [max_volume, total_frames]
    return file_info
