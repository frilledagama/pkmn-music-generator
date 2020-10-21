import music21 as m21
import pretty_midi as pm
import os
import glob
# os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\midi-input\\cleaned"
#         "-data\\no-drum")
os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\MIDI")
rootdir = "."


def rem_drum(song_file):
    curr_midi = pm.PrettyMIDI(song_file)

    # check all songs and get the index of the drum track
    drum_instruments_index = [i for i, inst in enumerate(curr_midi.instruments) if inst.is_drum]

    # remove all the drum tracks
    for i in sorted(drum_instruments_index, reverse=True):
        del curr_midi.instruments[i]
    # write new drum-less midi
    curr_midi.write('%s' % song_file)


for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            rem_drum(file)
