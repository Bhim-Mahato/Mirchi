
import asyncio
import os
import tempfile

import speech_recognition as sr
import edge_tts
from playsound import playsound


#  SPEECH TO TEXT 
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}")
        return query.lower()

    except Exception:
        print("Sorry, I didn't catch that.")
        return ""


#  TEXT TO SPEECH 
async def speak(text):
    if text == "":
        return

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        temp_file = f.name

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-IN-NeerjaNeural",
        rate="-30%",
        volume="-10%"
    )

    await communicate.save(temp_file)
    playsound(temp_file)
    os.remove(temp_file)  # auto delete


#  MAIN 
if __name__ == "__main__":
    text = takecommand()
    asyncio.run(speak(text))




