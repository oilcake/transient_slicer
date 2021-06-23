class Slicer():
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
        # count = 0
        params = (source_file.getparams())


        for address in onsets:
            # note = Note(source_file, address)

            print('write onset count', count)
            ##         print(cunt)
            source_file.setpos(address)
            step_ahead = onsets.index(address) + 1
            if step_ahead == len(onsets):
                gap = source_file.getnframes() - address
            else:
                gap = onsets[step_ahead] - address
            # one_note = source_file.readframes(gap)


            note_frames = source_file.readframes(gap)

            # filename_temp = path_temp + file_in + '_tmp_' + str(count) + '.aif'

            name = "TODO"

            note = Note(note_frames, name, params)
            notes.append(note)
            note.tmp_persist() # writes itself in the filesystem



            #
            # filename_temp = path_temp + file_in + '_tmp_' + str(count) + '.aif'
            # if not os.path.isfile(filename_temp):
            #     with aifc.open(filename_temp ,'w') as bigdick:
            #         bigdick.setparams(params)
            #         bigdick.writeframes(one_note)
            # else:
            #     print('file exists')
            # count += 1
    print("temporary files are writen")
    # return params
    return notes
