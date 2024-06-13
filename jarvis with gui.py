import pyttsx3 #text to speech conversion library
import speech_recognition as sr #recognizing speech input 
import datetime #current time
import wikipedia #wikipedia  data search 
import webbrowser #opening webpages
import pywhatkit as wk #for youtube 
import os #interacting with operationg system
import random #random selection
import tkinter as tk #gui
from tkinter import scrolledtext, PhotoImage #gui

engine = pyttsx3.init('sapi5') #initialize text to speech engine. sapi5(microsoft speech api)
voices = engine.getProperty('voices') #This method retrieves the list of available voices on the system. Each voice in the list contains attributes such as id
engine.setProperty('voice', voices[1].id) #set the voice of first available option ..for male put[0]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
   hour = datetime.datetime.now().hour
   if hour >= 0 and hour < 12:
      speak("Good Morning!")
   elif hour >= 12 and hour < 18:
      speak("Good Afternoon!")
   else:
      speak("Good Evening!")
   
   speak("I am Jarvis Ma'am. Please tell me how may I help you?")
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:  # opens a microphone for audio input
        status_text.set("Listening...")  # updates the status text in the GUI to indicate that the program is listening for audio input.
        window.update()
        recognizer.pause_threshold = 0.8  # it takes gap for 0.8 if it is more than it consider phrase complete
        recognizer.adjust_for_ambient_noise(source, duration=1)  # dynamically adjust to ambient noise
        audio = recognizer.listen(source)  # captures the audio from microphone
    try:
        status_text.set("Recognizing...")  # update status that program is recognizing speech
        window.update()
        query = recognizer.recognize_google(audio, language='en-PK')  # uses the Google Web Speech API to recognize the speech in the captured audio.
        status_text.set(f"User said: {query}")
        text_area.insert(tk.END, f"User said: {query}\n")  # Corrected line
        return query.lower()
    except sr.UnknownValueError:
        status_text.set("Sorry, I didn't catch that. Can you repeat?")
        return "None"


def executeCommand(query):
    if 'jarvis' in query:
        speak("yes mam")
    elif 'who are you' in query:
        speak("My name is jarvis")
        speak("I can do everything that my creator programmed me to do")
    elif 'just open youtube' in query: 
        webbrowser.open("https://www.youtube.com")
    elif 'open youtube' in query: 
        speak("what you will like to watch?")
        qrry=takeCommand().lower()
        wk.playonyt(f"{qrry}")
    elif 'search on youtube' in query: 
        query=query.replace('search on youtube', "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif 'what is' in query: 
        speak("Searching Wikipedia...")
        query = query.replace("what is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        text_area.insert(tk.END, results + '\n')
    elif 'who is' in query: 
        speak("Searching Wikipedia...")
        query = query.replace("who is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        text_area.insert(tk.END, results + '\n')
    elif 'just open google' in query: 
        webbrowser.open("https://www.google.com")
        text_area.insert(tk.END, "Google opened\n")
    elif 'open google' in query: 
        speak("what should I search?")
        qry=takeCommand().lower()
        webbrowser.open(f"https://www.google.com/search?q={qry}")
        result=wikipedia.summary(qry, sentences=2)
        speak(result)
        text_area.insert(tk.END, result + '\n')
    elif 'open google playstore' in query: 
        webbrowser.open("https://play.google.com")
        text_area.insert(tk.END, "Google Play Store opened\n")
    elif 'play music' in query: 
        music_dir='c:\\Users\\CZ 3\\Desktop\\Music'
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,random.choice(songs)))
    elif 'the time' in query: 
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
    elif 'open vs code' in query: 
        codepath='c:\\Users\\CZ 3\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
        os.startfile(codepath)
    elif 'open adobe illustrator' in query:
        adobe_ill='c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Illustrator 2019.lnk'
        os.startfile(adobe_ill)
    elif 'open adobe photoshop' in query:
        adobe_photo='c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Photoshop CC 2019.lnk'
        os.startfile(adobe_photo)
    elif 'open word' in query:
        word='c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk'
        os.startfile(word)
    elif 'open powerpoint' in query:
        powerpoint='c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016.lnk'
        os.startfile(powerpoint)
    elif 'open powerpoint' in query:
        paint="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk"
        os.startfile(paint)
    elif 'open notepad' in query:
        notepad="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
        os.startfile(notepad)
    elif 'open command prompt' in query:
        cmdprompt="C:\\Users\\CZ 3\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
        os.startfile(cmdprompt)
    elif 'open excel' in query:
        excel='c:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2016.lnk'
        os.startfile(excel)


def startAssistant():
    wishMe()
    while True:
        query = takeCommand()
        if query != "None":
            executeCommand(query)

def stopAssistant():
    status_text.set("Assistant stopped.")
    window.quit()

# GUI setup
window = tk.Tk()
window.title("JARVIS")
window.geometry("700x500") #Sets the initial size of the window to be 700 pixels wide and 500 pixels tall.
window.configure(bg="#2c3e50")
#icon
image_icon = PhotoImage(file="speak.png")
window.iconphoto(False, image_icon)

status_text = tk.StringVar()
status_text.set("Click 'Start' to activate JARVIS")

# Top frame for logo and status
top_frame = tk.Frame(window, bg="#34495e")
top_frame.pack(side=tk.TOP, fill=tk.X)

logo = PhotoImage(file="icons8-voice-assistant-64.png")  # Add your logo file path here
logo_label = tk.Label(top_frame, image=logo, bg="#34495e")
logo_label.pack(side=tk.LEFT, padx=10, pady=10)

status_label = tk.Label(top_frame, textvariable=status_text, font=("Arial", 14), fg="white", bg="#34495e")
status_label.pack(side=tk.LEFT, padx=10, pady=10)

# Middle frame for text area
middle_frame = tk.Frame(window, bg="#2c3e50")
middle_frame.pack(expand=True, fill=tk.BOTH)

text_area = scrolledtext.ScrolledText(middle_frame, wrap=tk.WORD, width=60, height=15, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Bottom frame for buttons
bottom_frame = tk.Frame(window, bg="#34495e")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

start_button = tk.Button(bottom_frame, text="Start", command=startAssistant, font=("Arial", 14), bg="#27ae60", fg="white")
start_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = tk.Button(bottom_frame, text="Stop", command=stopAssistant, font=("Arial", 14), bg="#c0392b", fg="white")
stop_button.pack(side=tk.RIGHT, padx=10, pady=10)

window.mainloop()


