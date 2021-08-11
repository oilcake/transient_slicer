import aifc


class Slicer:

    def __init__(self, sample, startpoint):
        self.sample = aifc.open(sample, 'r')
        self.parameters = self.sample.getparams()
        self.onset = startpoint
        self.sample.setpos(self.onset)

    def slice(self, filename, duration):
        note = self.sample.readframes(duration)
        name = "TODO"
        return note

        
