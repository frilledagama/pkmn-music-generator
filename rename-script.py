import glob
import os

os.chdir("C:\\Users\\Maya\\Documents\\School\\U4\\F2020\\MAIS202\\Project\\data\\pkmn-midi-all\\FRLG")

for f in glob.glob('*.mid'):
    new_filename = f.replace("-hgss-rse.mid","-frlg.mid")
    #new_filename = "kml_" + new_filename
    os.rename(f,new_filename)