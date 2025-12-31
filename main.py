import os
import eel
from engine.features import *
from engine.command import *
  
def start():                #created for muoltithreading
    
    eel.init("www")

    playAssistantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start("index.html",mode=None,host="localhost",block=True)

