# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()

#     voices = engine.getProperty('sapi5')
#     engine.setProperty('voice', voices[1].id)  # female voice
#     engine.setProperty('rate', 170)       

#     engine.say(text)
#     engine.runAndWait()

# speak("I love you Mirchi")



import asyncio
import edge_tts
from playsound import playsound

def speak(text):
    async def _speak():
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-IN-NeerjaNeural",  
            rate="-30%",               
            volume="-10%"               
        )
        await communicate.save("voice.mp3")
        playsound("voice.mp3")        

    asyncio.run(_speak())


speak("to ki kar rhi hai...")

