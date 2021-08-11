import numpy
from aubio import source, onset, sink


class Note:

    def __init__(self, sample):
        samplerate = 0
        self.hop_size = 32
        self.sample = source(sample, samplerate, self.hop_size)

    def rewind_to(self, onset):
        self.onset = onset
        self.sample.seek(self.onset)

    def __rewind(self):
        self.sample.seek(self.onset)

    def duration(self):
        duration = 0
        silence = 0.0001
        while True:
            samples, read = self.sample()
            rms = numpy.sqrt(numpy.mean(samples**2))
            duration += read
            if rms < silence:
                break
            if read < self.hop_size:
                break
        return duration

    def detect_rms(self):
        pass

    def detect_max(self):
        if self.duration:
            self.__rewind()
            max = 0
            frames_total = 0
            while True:
                samples, read = self.sample()
                if max < numpy.amax(samples):
                    max = numpy.amax(samples)
                frames_total += read
                if frames_total > self.duration():
                    break
        return max

    def close(self):
        self.sample.close()
