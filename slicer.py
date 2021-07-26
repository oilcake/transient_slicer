class Slicer():

    def __init__(self):
        pass

    def detect_duration(self):
        pass

    def detect_max(self):
        pass

    def slice(self):
        pass

def transient_slicer(filename, onsets, path, file_in):
    path_temp = os.path.join(path, temporary_postfix)
    if not os.path.exists(path_temp):
        os.mkdir(path_temp)
        print("Directory ", path_temp, " Created ")
    else:
        print("Directory ", path_temp, " already exists")


    notes = []

    with aifc.open(filename, 'r') as source_file:
        params = (source_file.getparams())
        for address in onsets:
            print('write onset count', count)
            source_file.setpos(address)
            step_ahead = onsets.index(address) + 1
            if step_ahead == len(onsets):
                gap = source_file.getnframes() - address
            else:
                gap = onsets[step_ahead] - address
            note_frames = source_file.readframes(gap)
            name = "TODO"
            note = Note(note_frames, name, params)
            notes.append(note)
            note.tmp_persist() # writes itself in the filesystem

    print("temporary files are writen")
    return notes
