import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import urllib.request
import json
import time
from google import genai

# pip install pocketsphinx

recognizer = sr.Recognizer()
newsapi = "YOUR_NEWS_API"

def speak(text):
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.5)

def aiProcess(Conversation):
    client = genai.Client(api_key="YOUR_API_KEY")  

    response = client.models.generate_content(
        model="gemini-2.5-Pro",
        contents=f"""
                You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud {Conversation}
                """
    )

    return response.text



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open x" in c.lower():
        webbrowser.open("https://x.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
            category = "general"
            url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=us&max=10&apikey={newsapi}"

            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode("utf-8"))
                articles = data["articles"]

                for i in range(len(articles)):
                    # articles[i].title
                    print(f"Title: {articles[i]['title']}")
                    # articles[i].description
                    speak(f"Description: {articles[i]['description']}")
    
    else:
        Output=aiProcess(c)
        speak(Output)





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                time.sleep(1)
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))