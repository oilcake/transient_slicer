class Editor:

    def __init__(self, record):
        self.audio = record

    def rewind(self, time):
        self.audio.seek(time)

    def detect_duration(self):
        pass

    def detect_rms(self):
        pass

    def detect_max(self):
        pass