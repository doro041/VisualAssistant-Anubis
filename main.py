import pyttsx3 as pytt
import speech_recognition as sr
import webbrowser as wb
from time import sleep
from datetime import datetime
import pyaudio

#if __name__ = "__main_=":
#speaker.say("Hello Doro and Nikita. I am a time traveller. I came on this planet yesterday.")
#speaker.runAndWait()
#filename = "ENG_M.wav"

# open the file
# with sr.AudioFile(filename) as source:
#     # listen for the data load ausio to memory
#     audio_data = r.record(source)
#
#     # recognise from speech to text
#     text = r.recognize_google(audio_data)
#     print(text)
#     speaker.say(str(text))
#     speaker.runAndWait()

# FCN to recognize our voice and return the text_version of it
def recognise_voice():
    text = ''

    # create an instance of the Microphone class
    with sr.Microphone(device_index=8) as source:
        # adjust for ambient noise
        r.adjust_for_ambient_noise(source)

        # capture the voice
        voice = r.listen(source)

        # let's recognize it
        try:
            text = r.recognize_google(voice)
        except sr.RequestError:
            speak("Sorry, the I can't access the Google API...")
        except sr.UnknownValueError:
            speak("Sorry, Unable to recognize your speech...")
    return text.lower()


# FCN for VA to respond back
def reply(text_version):
    # name
    if "name" in text_version:
        speak("My name is Anubis")

    # how are you?
    if "how are you" in text_version:
        speak("I am fine...")
    # date
    if "date" in text_version:
        # get today's date and format it - 9 November 2020
        date = datetime.now().strftime("%d %m %Y")
        speak(date)
    # time
    if "time" in text_version:
        # get current time and format it like - 02 28
        time = datetime.now().time().strftime("%H %M")
        speak("The time is " + time)

    # search google
    if "search" in text_version:
        speak("What do you want me to search for?")
        keyword = recognise_voice()
        # if "keyword" is not empty
        if keyword != '':
            url = "https://google.com/search?q=" + keyword
            # webbrowser module to work with the webbrowser
            speak("Here are the search results for " + keyword)
            wb.open(url)
            sleep(3)

    # quit/exit
    if "quit" in text_version or "exit" in text_version:
        speak("Ok, I am going to take a nap...")
        exit()

# FCN for VA to speak
def speak(text):
  speaker.say(text)
  speaker.runAndWait()


# initialise the recogniser
r = sr.Recognizer()
speaker = pytt.init()

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(str(index) + " - " + str(name))

sr.Re
"""
# wait a second for adjust_for_ambient_noise() to do its thing
sleep(1)

while True:
    speak("Start speaking...")

    # listen for voice and convert it into text format
    text_version = recognise_voice()
    # give "text_version" to reply() fn
    reply(text_version)
    #print(text_version)

#speaker.say("Hello Doro and Nikita. I am a time traveller. I came on this planet yesterday.")
#speaker.runAndWait()
"""