import pyttsx3
import PySimpleGUI as sg
import wikipedia
from configs.gui import main

engine = pyttsx3.init("sapi5")

newVoiceRate = 100
engine.setProperty('rate',newVoiceRate)

def speak(text):
  engine.say(text)
  engine.runAndWait()

speak(main())