import sys
from struct import *
from operator import *
from pydub import AudioSegment

m4a_in = AudioSegment.from_file(sys.argv[1])
wav_file = m4a_in.export(format = 'wav')
wav = AudioSegment.from_wav(wav_file)
samples = wav.get_array_of_samples()

freq = wav.frame_rate
ch = wav.channels

i = int(round(len(samples)/20))
while (samples[i] > -1*max(samples)/20):
	i = i + 1000

print i

k = len(samples)
while samples[k-1] > -max(samples)/5:
	k = k - 1000

print k

peaks = []

signal_length = k - i - 10
for l in range(0, signal_length):
	if (samples[i+l+1] - samples[i+l] < 0 and samples[i+l+2] - samples[i+l+1] > 0):
	peaks.append(samples[i+l])
	if (samples[i+l+1) - samples[i+l] > 0 and samples[i+l+2] - samples[i+l+2] - samples[i+l+1] < 0):
	peaks.append(samples[i+l])

print len(peaks)

m = int(round(len(peaks)/20))
if len(peaks) > 1200:
	while (peaks[m] > -1*max(peaks)/20):
		m = m + 100

print len(peaks) - m
