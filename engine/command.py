import asyncio
import os
import tempfile
import eel
import speech_recognition as sr
import edge_tts
from playsound import playsound


# -------- SPEECH TO TEXT (INTERNAL FUNCTION) --------
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()

        return query.lower()

    except Exception as e:
        print("Error:", e)
        eel.DisplayMessage("Could not understand")
        return ""


# -------- TEXT TO SPEECH --------
def speak(text):
    if text == "":
        return 

    async def _speak():
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            temp_file = f.name

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-IN-NeerjaNeural",
            rate="-30%",
            volume="-10%"
        )

        await communicate.save(temp_file)
        playsound(temp_file)   # sound off
        os.remove(temp_file)

    asyncio.run(_speak())


# -------- MAIN COMMAND FUNCTION (EXPOSED TO JS) --------
@eel.expose
def allCommands():
    try:
        query=takecommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query) 

        elif "on youtube":                               #play anything in youtube
            from engine.features import PlayYoutube
            PlayYoutube(query)

        else:
            print("not run")

    except:
        print("error")