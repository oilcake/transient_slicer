import argparse

import matplotlib.pyplot as plt
import librosa
import librosa.display

from housekeeping.datahandling import makedir, get_files
from audiotools.analyze import find_onsets
from audiotools.note import Note
from audiotools.slicer import Slicer
from aubio import source

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
    onsets = find_onsets(file, threshold=1.5, window=1024)
    sample = source(file, samplerate=0, hop_size=64)
    x, sr = librosa.load(file)
    plt.figure(figsize=(18, 3))
    plt.suptitle(str(file), fontsize=16)
    librosa.display.waveplot(x, sr=sr)
    print()
    print('samplerate = ', sample.samplerate)
    for onset in onsets:
        onset_time = librosa.samples_to_time(onset, sr=sr*2) # converts onset time from samples to ms
        plt.plot(onset_time, 0.2, marker=9)
        note = Note(sample, onset)
        print(file, 'onset = ', onset)
        print('duration = ', note.duration)
        print('max value = ', note.max)
        duration_ms = librosa.samples_to_time(note.duration, sr=sr*2)
        plt.plot(onset_time + duration_ms, 0.2, marker=2)
    plt.show()
    sample.close()
