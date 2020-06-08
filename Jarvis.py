
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

name='ELon Musk'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0)and(hour<12):
        print('Good Morning ' + name)
        speak('Good Morning' + name)
    elif (hour >= 12) and (hour < 18):
        print('Good Afternoon ' + name)
        speak('Good Afternoon' + name)
    else:
        speak('Good Evening' + name)
        print('Good Evening' + name)
    speak('I am Jarvis.How may i help you??')

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
        except:
            print('Sry cannot able to recognize your voice properly')
    return text

def main():
    print('Initializing Jarvis...')
    speak('Initializing Jarvis...')
    wishMe()
    query = takeCommand()
    print(query)

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        url = 'facebook.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play video song' in query.lower():
        video_dir = 'E:\\'
        videos = os.listdir('E:\\')
        os.startfile(os.path.join(video_dir, videos[0]))

    elif 'open youtube' in query.lower():
        url = 'youtube.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    elif 'time' in query.lower():
        strtime = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'{name} the time is {strtime}')
        speak(f'{name} the time is {strtime}')

    else:
        url = 'google.com'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

main()
