import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recognise

eel.init("www")
playAssistantSound()
@eel.expose
def init():
    eel.hideLoader()
    speak("ready for face authentication")
    flag=recognise.AuthenticateFace()
    if flag== 1:
        eel.hideFaceAuth()
        speak(" face authentication is sucessful")
    else:
        speak(" face authentication is failed")
        
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start("index.html",mode=None,host="localhost",block=True)

