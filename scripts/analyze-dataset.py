import music21 as m21
import mido
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\midi-input\\cleaned-data\\all-piano")
os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\pkmn-music-generator\\run1_misc\\output\\midiprimer\\bw-rt2spr")
rootdir = "."


def get_instruments(midi):
    part_stream = midi.parts.stream()
    print("List of instruments found on MIDI file:")
    for p in part_stream:
        aux = p
        print(p.partName)


def get_key(midi):
    # get key signature
    midi_score = m21.converter.parse(midi)
    key = midi_score.analyze('key')
    print(key)
    # get instruments


def get_time_sig(midi):
    #s_midi = m21.converter.parse(midi)
    # midi_part = s_midi.getElementsByClass(m21.stream.Measure)
    # time_sig = m21.meter.TimeSignature(midi_part)
    # print(time_sig)
    time_signature = midi.getTimeSignatures()[0]
    music_analysis = midi.analyze('key')
    time_signature_str = "Music time signature: {0}/{1}".format(time_signature.beatCount, time_signature.denominator)
    # return time_signature_str
    # print("Music time signature: {0}/{1}".format(time_signature.beatCount, time_signature.denominator))
    print("Expected music key: {0}".format(music_analysis))
    print("Music key confidence: {0}".format(music_analysis.correlationCoefficient))
    print("Other music key alternatives:")
    for analysis in music_analysis.alternateInterpretations:
        if analysis.correlationCoefficient > 0.5:
            print(analysis)


def extract_notes(midi_part):
    parent_element = []
    ret = []
    for nt in midi_part.flat.notes:
        if isinstance(nt, m21.note.Note):
            ret.append(max(0.0, nt.pitch.ps))
            parent_element.append(nt)
        elif isinstance(nt, m21.chord.Chord):
            for pitch in nt.pitches:
                ret.append(max(0.0, pitch.ps))
                parent_element.append(nt)

    return ret, parent_element


def print_parts_contour(midi):
    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(1, 1, 1)
    minPitch = m21.pitch.Pitch('C10').ps
    maxPitch = 0
    xMax = 0

    # Drawing notes.
    for i in range(len(midi.parts)):
        top = midi.parts[i].flat.notes
        y, parent_element = extract_notes(top)
        if (len(y) < 1): continue

        x = [n.offset for n in parent_element]
        ax.scatter(x, y, alpha=0.6, s=7)

        aux = min(y)
        if (aux < minPitch): minPitch = aux

        aux = max(y)
        if (aux > maxPitch): maxPitch = aux

        aux = max(x)
        if (aux > xMax): xMax = aux

    for i in range(1, 10):
        linePitch = m21.pitch.Pitch('C{0}'.format(i)).ps
        if (linePitch > minPitch and linePitch < maxPitch):
            ax.add_line(mlines.Line2D([0, xMax], [linePitch, linePitch], color='red', alpha=0.1))

    plt.ylabel("Note index (each octave has 12 notes)")
    plt.xlabel("Number of quarter notes (beats)")
    plt.title('Voices motion approximation, each color is a different MIDI channel, red lines show each octave')
    plt.savefig('bw-rt2spr-p-4 - Voices motion.png')
    plt.show()



# Focusing only on 6 first measures to make it easier to understand.
# mid = m21.converter.parse("2020-10-20_013334_4.mid")
mid = m21.converter.parse("2020-10-20_013334_4.mid")
# print_parts_contour(mid.measures(0, 6))
#mid.plot('histogram', 'pitchClass', 'count')
get_time_sig(mid)
# list_instruments(mid)

# get_key("Route 1.mid")
# get_time_sig("Route 1.mid")