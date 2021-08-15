import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
from googlesearch import search #pip install google
import random
import os
import webbrowser
urL='https://www.google.com'
chrome_path="C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good night")

    speak("hello rishi i am networm, how may i help youu")

def takeCommand():
    #take command from the user 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=10)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query
if __name__=='__main__':
    wishme()#logic to execute task based on query 
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("https://www.youtube.com")
            speak("Anything else sir?")
        elif 'open quora' in query:
            webbrowser.get('chrome').open("https://www.quora.com")
            speak("Anything else sir?")
        elif 'stackoverflow' in query:
            webbrowser.get('chrome').open("https://www.stackoverflow.com")
            speak("Anything else sir?")
        elif 'google' in query:
            query = query.replace("google","")
            for j in search(query,tld="co.in", num=1, stop=1, pause=3):
                webbrowser.get('chrome').open(j)
            speak("Anything else sir?")
        elif 'play music' in query:
            music_dir = 'D:\Music'
            songs=os.listdir(music_dir)
            print(songs)
            num_of_songs = len(songs)
            i = random.randint(0,num_of_songs-1)
            os.startfile(os.path.join(music_dir,songs[i]))
            speak("Anything else sir?")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir the time is{strTime}")
            speak("Anything else sir?")
            speak("Anything else sir?")
        elif 'open soup' in query:
            webbrowser.get('chrome').open("https://web.whatsapp.com/")
            speak("Anything else sir?")
       
        elif 'create folder' in query:
            speak("what is your folder name")
            directory = takeCommand()
            parent_dir = "D:\\Python Files"
            path = os.path.join(parent_dir, directory)
            os.makedirs(path)
            new_parent_dir = f"D:\\Python Files\\{directory}"
            speak("Anything else sir?")
        elif 'spotify' in query:
            webbrowser.get('chrome').open("https://open.spotify.com/")
            speak("Anything else sir?")
        elif 'stop' in query:
            exit()