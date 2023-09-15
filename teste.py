import sounddevice
from scipy.io.wavfile import write

fs = 44100
seconds = int(input("Quantos segundos deseja gravar? "))

print("\nGravando.......\n")

record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
sounddevice.wait()
 
file_name = "gravacao.wav"  # Nome do arquivo com extensão .wav
write(file_name, fs, record_voice)
print("\nGravação Finalizada.......\n")

