import numpy as np 
from plotly.subplots import make_subplots 
import plotly.graph_objects as go
from scipy.io import wavfile 

fig = make_subplots(
    rows = 3, cols =2,
    subplot_titles = ("Spectrum of Middle C4 note",
                      "Spectrum of Middle G4 note",
                      "Spectrum of Middle A4 note",
                      "Spectrum of Middle F4 note",
                      "Spectrum of Middle E4 note",
                      "Spectrum of Middle D4 note"))

sample_rate_c,middle_c = wavfile.read('c4.wav')
sample_rate_g,middle_g = wavfile.read('g4.wav')
sample_rate_a, middle_a = wavfile.read('a4.wav')
sample_rate_f, middle_f = wavfile.read('f4.wav')
sample_rate_e , middle_e =  wavfile.read('e4.wav')
sample_rate_d, middle_d = wavfile.read('d4.wav')
t_c = np.arange(middle_c.shape[0])
t_g = np.arange(middle_g.shape[0]) 
t_a  = np.arange(middle_a.shape[0])
t_f = np.arange(middle_f.shape[0]) 
t_e = np.arange(middle_e.shape[0]) 
t_d = np.arange(middle_d.shape[0])

freq_c = np.fft.fftfreq(t_c.shape[-1])*sample_rate_c 
freq_g = np.fft.fftfreq(t_g.shape[-1]) * sample_rate_g 
freq_a = np.fft.fftfreq(t_a.shape[-1]) *sample_rate_a 
freq_f = np.fft.fftfreq(t_f.shape[-1]) * sample_rate_f 
freq_e = np.fft.fftfreq(t_f.shape[-1]) * sample_rate_e
freq_d = np.fft.fftfreq(t_e.shape[-1]) * sample_rate_d

sp_c = np.fft.fft(middle_c)
sp_d = np.fft.fft(middle_d)
sp_e = np.fft.fft(middle_e)
sp_f = np.fft.fft(middle_f)
sp_g = np.fft.fft(middle_g)
sp_a = np.fft.fft(middle_a)

fig.add_trace(go.Scatter(x=freq_c, y=abs(sp_c.real)),
              row=1, col=1)

fig.add_trace(go.Scatter(x=freq_g, y=abs(sp_g.real)),
              row=1, col=2)

fig.add_trace(go.Scatter(x = freq_a, y=abs(sp_a.real)),
              row=2, col=1)

fig.add_trace(go.Scatter(x=freq_f, y = abs(sp_f.real)),
              row=2, col=2)

fig.add_trace(go.Scatter(x=freq_e, y=abs(sp_e.real)),
              row=3, col=1)

fig.add_trace(go.Scatter(x= freq_d, y=abs(sp_d.real)),
              row=3, col=2)







fig.update_layout( height = 1500, width = 1500 , title_text = "Spectrum of all piano notes used in Twinkle Twinkle Little Star")

fig.update_yaxes(range = [0,34000])
fig.show()
