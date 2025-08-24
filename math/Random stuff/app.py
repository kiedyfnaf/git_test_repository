import wikipedia
import pyttsx3
import threading
import keyboard
import wolframalpha 
app_id = "JYXLQG-TL9X4P8AL4"
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
rate = engine.getProperty('rate') 
engine.setProperty('rate', 130) 
engine.setProperty('voice', voices[1].id) 
client = wolframalpha.Client(app_id)  
song = "None"
import PySimpleGUI as sg
sg.theme('DarkPurple')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text(f'Free v-bucks:{song}')],
            [sg.Text('Whats you question?: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Fortnite', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break

    res = client.query(values[0])
    try:
        wolfram_res = next(res.results).text
    except:
        wolfram_res = "None"
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
    except:
        wiki_res = "None"
    def onWord(name, location, length):
        print ('word', name, location, length)
    if keyboard.is_pressed("esc"):
       engine.stop()
    engine.connect('started-word', onWord)
    engine.say(wolfram_res)
    sg.PopupNonBlocking("Wolfram: "+wolfram_res,"Wikipedia: "+wiki_res)
    engine.runAndWait()
window.close()
