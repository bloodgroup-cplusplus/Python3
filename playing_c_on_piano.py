'''from scipy.io import wavfile
import matplotlib.pylot as plt 
plt.style.use('seaborn-dark')

# Load data from wav file

sample_rate,middle_c = wavfile.read('data/pian')
'''


import numpy as np 
from scipy.io import wavfile 
# how to calculate the note frequency and make a sound wave.
# code here is quite similar, just expanded to 88 keys instead of a single octave:


#this function returns  a dictionary that maps a note name to corresponding frequency
# in hertz. Now we want to make a wave of a middle C
def get_piano_notes():
    #white key are in uppercase and blackkeys(sharps) are in lowercase
    octave = ['C','c','D','d','E','F','f','G','g','A','a','B']
    base_freq = 440 # Frequency of note A 4
    keys = np.array([x+str(y) for y in range(0,9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0') [0][0]
    end = np.where(keys == 'C8') [0][0]
    keys = keys[start:end+1]
    note_freqs = dict(zip(keys,[2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
    note_freqs[''] = 0.0 # stopping node 
    return note_freqs

def get_sine_wave (frequency, duration, sample_rate = 44100, amplitude = 4096):
    # duration is in number of seconds,
    #sample_rate determines the quality of sound
    # amplitude determines the volume.
    # a sample rate of 44.1khz (44,100 sampls per second) is quite common for consumer audio

    t = np.linspace(0,duration, int(sample_rate*duration)) # Tiime axis
    wave = amplitude * np.sin(2*np.pi*frequency*t)
    return wave
# Get middle C Frequency

#note_freqs = get_piano_notes()

note_freqs = get_piano_notes()
#print(note_freqs['C4'])
frequency = [note_freqs['C4'],note_freqs['D4'], note_freqs['E4'], note_freqs['F4'], note_freqs['G4'],note_freqs['A4'], note_freqs['B4']]

# Pure sine wave 

#for notes in frequency:

for notes in frequency:
    sine_wave = get_sine_wave (notes,duration = 2, amplitude = 2048)

    wavfile.write('saregama.wav',rate = 44100, data = sine_wave.astype(np.int16))
