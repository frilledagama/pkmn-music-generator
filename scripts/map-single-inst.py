import music21 as m21
import pretty_midi as pm
import os
import mido
import glob

os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\midi-input\\cleaned-data-run2\\first-3-tracks")
rootdir = "."


def conv_to_piano(song_file):
    curr_score = m21.converter.parse(song_file)

    for el in curr_score.recurse():
        if 'Instrument' in el.classes:
            try:
                el.activeSite.replace(el, m21.instrument.Piano())
            except Exception as e:
                print(e)

    curr_score.write('midi', "%s" % song_file)


for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            print("Mapping %s" % file)
            conv_to_piano(file)
