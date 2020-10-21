import music21 as m21
import os
import pandas as pd
from mido import MidiFile

# os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\midi-input\\cleaned-data\\all-piano")
# os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\run1_misc\\output"
#         "\\midiprimer\\bw-rt2spr")

# midi files dir

os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\MIDI\\BW")

rootdir = "."
# midi_csv = "C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\run1\\data\\data"-anal\\pkmn-midi.csv "


# function to add name data to entry
def add_name(csv_list, midi):
    name = os.path.splitext(midi)[0]
    csv_list.append(name)
    return csv_list


# function to add instrument data to entry
def add_instruments(csv_list, midi):
    part_stream = midi.parts.stream()
    instruments_str = []
    for p in part_stream:
        aux = p
        # instr = str(p.partName)
        instruments_str.append(p.partName)

    csv_list.append(instruments_str)
    return csv_list


def add_key(csv_list, midi):
    # get key signature
    # midi_score = m21.converter.parse(midi)
    key_analy = midi.analyze('key')
    key_conf = key_analy.correlationCoefficient

    csv_list.append(key_analy)
    csv_list.append(key_conf)
    return csv_list


def add_time_sig(csv_list, midi):
    # s_midi = m21.converter.parse(midi)
    # midi_part = s_midi.getElementsByClass(m21.stream.Measure)
    # time_sig = m21.meter.TimeSignature(midi_part)
    # print(time_sig)
    time_signature = midi.getTimeSignatures()[0]
    time_signature_str = "{0}/{1}".format(time_signature.beatCount, time_signature.denominator)
    csv_list.append(time_signature_str)
    return csv_list


# Focusing only on 6 first measures to make it easier to understand.
# mid = m21.converter.parse("2020-10-20_013334_4.mid")
# midi_file = "2020-10-20_013334_4.mid"
#midi_file = "Route 2 [Spring].mid"


# print_parts_contour(mid.measures(0, 6))
# mid.plot('histogram', 'pitchClass', 'count')
# list_instruments(mid)

# get_key("Route 1.mid")
# get_time_sig("Route 1.mid")
def add_duration(csv_list, midi):
    mid = MidiFile(midi)
    csv_list.append(mid.length)
    return csv_list


def create_row_entry(midi_file, game):
    mid = m21.converter.parse(midi_file)
    midi_row = []
    midi_row = add_name(midi_row, midi_file)
    midi_row = add_key(midi_row, mid)
    midi_row = add_time_sig(midi_row, mid)
    midi_row = add_instruments(midi_row, mid)
    midi_row = add_duration(midi_row, midi_file)

    return midi_row


# print(*midi_row, sep="; ")

all_rows = []

# BW
for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            try:
                all_rows.append(create_row_entry(file, "BW"))
                print("Added " + file + " to df")
            except Exception as e:
                print(e)
                continue

# DPPt
os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\MIDI\\DPPt")
for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            try:
                all_rows.append(create_row_entry(file, "DPPt"))
                print("Added " + file + " to df")
            except Exception as e:
                print(e)
                continue

# FRLG
os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\MIDI\\FRLG")
for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            try:
                all_rows.append(create_row_entry(file, "FRLG"))
                print("Added " + file + " to df")
            except Exception as e:
                print(e)
                continue

# HGSS
os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\MIDI\\HGSS")
for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            try:
                all_rows.append(create_row_entry(file, "HGSS"))
                print("Added " + file + " to df")
            except Exception as e:
                print(e)
                continue

# RSE
os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\MIDI\\RSE")
for subdirs, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".mid"):
            try:
                all_rows.append(create_row_entry(file, "RSE"))
                print("Added " + file + " to df")
            except Exception as e:
                print(e)
                continue

# create dataframe

df = pd.DataFrame(all_rows, columns=["Name", "Game", "Key Signature", "Time Signature", "Instruments", "Length"])

# convert to csv
# midi_csv = "C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\run1\\data\\data-anal\\pkmn-midi.csv"

df.to_csv("pkmn-midi.csv")

df.head()

# convert it to a csv
