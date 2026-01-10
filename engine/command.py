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
            rate="-25%",
            volume="-5%"
        )

        await communicate.save(temp_file)
        playsound(temp_file)   # sound off
        os.remove(temp_file)

    asyncio.run(_speak())


# -------- MAIN COMMAND FUNCTION (EXPOSED TO JS) --------
@eel.expose
def allCommands(message=1):

    if message==1:
        query = takecommand()
        print(query)

    else:
        query=message

    try:
        

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:   # play anything on youtube
            from engine.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            message = ""
            contact_no, name = findContact(query)

            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    speak("what message to send")
                    query = takecommand()

                elif "phone call" in query:
                    message = 'call'

                else:
                    message = 'video call'

                whatsApp(contact_no, query, message, name)

        else:
            print("not run")

    except:
        print("error")
