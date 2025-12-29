from playsound import playsound
import eel

#assistant sound function

@eel.expose  #we can acess this method via main.js

def playAssistantSound():
    music_dir="www\\audio\\aud1.wav"
    playsound(music_dir)