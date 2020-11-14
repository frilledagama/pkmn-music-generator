import music21 as m21
import pretty_midi as pm
import os
import mido
import glob

os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\midi-input\\cleaned-data-run2\\first-3-tracks")
rootdir = "."


def conv_n_first_tracks_to_piano_m21(song_file, n):
    curr_score = m21.converter.parse(song_file)
    track = 0
    for el in curr_score.recurse():
        if 'Instrument' in el.classes:
            if track < n:
                try:
                    el.activeSite.replace(el, m21.instrument.Piano())
                except Exception as e:
                    print(e)
                track = track + 1
            else:
                del el.activeSite

    curr_score.write('midi', "%s" % song_file)


def keep_first_n_tracks(song_file,n):
    curr_midi = pm.PrettyMIDI(song_file)
    track = 0
    inst_idx = [i for i, inst in enumerate(curr_midi.instruments)]
    for i in sorted(inst_idx, reverse=True):
        if track > n:
            try:
                del curr_midi.instruments[i]
            except Exception as e:
                print(e)
        track = track + 1
    curr_midi.write('%s' % song_file)


# keep_first_n_tracks("BW\\A New Adventure!.mid", 3)

for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            print("Deleting tracks > 3 %s" % file)
            keep_first_n_tracks(file, 3)
