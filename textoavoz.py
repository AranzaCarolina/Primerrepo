#escribir un programa que convierta texto a sonido
from gtts import gTTS
from playsound import playsound

from miscodigos import MiClaseGrupo21

texto = input("ingresa un texto")
tts = gTTS(texto,lang="es")
tts.save('texto.mp3')

playsound('texto.mp3')

x = MiClaseGrupo21