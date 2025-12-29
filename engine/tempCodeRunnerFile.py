import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('sapi5')
    engine.setProperty('voice', voices[1].id)  # female voice
    engine.setProperty('rate', 170)       

    engine.say(text)
    engine.runAndWait()

speak("I love you Mirchi")