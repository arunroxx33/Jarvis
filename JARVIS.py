import subprocess
import webbrowser
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import time

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

def speak(inpu):
    engine.say(inpu)
    engine.runAndWait()



def wishme():
    hour=int(datetime.datetime.now().hour)
    # print(hour)
    if hour<12:
        engine.say("Good Morning!")
    elif hour<18:
        engine.say("Good Afternoon!")
    else:
        engine.say("Good Evening!")
    speak("What is going on with the world!!")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Getting there!")
        r.pause_threshold=1
        audio = r.listen(source)
    query=0

    try:
        print("Getting There!!")
        query = r.recognize_google(audio,language = "en-UK")
        print("Query said:",query)
    except:
        speak("Please say that clearly bruh!!")
        return "None"
    return query.lower()

def subprocesscall(x):
    subprocess.call(x,shell = True)

if __name__ == "__main__":
    wishme()
    while True:
        try:
            query=takecommand().lower()
            query.split()

            spotify_path = 'open -a /Applications/Spotify\ Spotify.app %s'
            if 'wikipedia'in query:
                speak("Just Wait A sec!")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query , sentences = 2)
                speak("According to Wikipedia" + results)
            elif 'youtube' in query and 'subscriptions' not in query:
                speak("Just Wait A sec!")
                query = query.replace("youtube ","https://www.youtube.com/results?search_query="+str(query.split()[1:]))
                webbrowser.get('chrome').open_new(query)
                time.sleep(2)
            elif 'youtube' in query and 'subscriptions' in query:
                speak("Just Wait a sec!")
                query = "https://www.youtube.com/feed/subscriptions/"
                webbrowser.get('chrome').open(query)
            elif 'spotify' in query:
                subprocesscall('spotify')
            elif 'visual' in query:
                subprocesscall('Visual Studio Code')
            elif 'exit' in query:
                exit()
        except KeyboardInterrupt:
            exit(0)