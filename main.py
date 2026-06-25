import pyttsx3
import datetime
import webbrowser
import os
import subprocess
import platform
import random
from urllib.parse import quote_plus

engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning. I am Jarvis.")
    elif hour < 18:
        speak("Good afternoon. I am Jarvis.")
    else:
        speak("Good evening. I am Jarvis.")

def show_help():
    print("""
--------- JARVIS COMMANDS ---------

hello
time
date

open youtube
open google
open linkedin
open notepad
open calculator
open vscode
open command prompt
open spotify

search <anything>

who is <person>
what is <topic>
tell me about <topic>

take note
show notes

tell me a joke
system info
clear
help
stop / exit / goodbye

-----------------------------------
""")

def open_wikipedia(query):
    if not query:
        speak("Please type a topic for Wikipedia.")
        return

    speak("Opening Wikipedia for " + query)

    # This searches Wikipedia safely, even if the page title has spaces.
    wikipedia_url = "https://en.wikipedia.org/w/index.php?search=" + quote_plus(query)
    webbrowser.open(wikipedia_url)

wish_user()
show_help()

while True:
    command = input("\nType a command: ").lower().strip()

    if "hello" in command:
        speak("Hello. How can I help you?")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    elif command == "date":
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc")

    elif "open vscode" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    elif "open command prompt" in command or "open cmd" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif "open spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")

    elif "take note" in command or "write note" in command:
        speak("Type your note in the terminal.")
        note = input("Write your note: ")

        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(note + "\n")

        speak("Your note has been saved.")

    elif "show notes" in command:
        try:
            with open("notes.txt", "r", encoding="utf-8") as file:
                notes = file.read()

            if notes.strip():
                print("\n--------- YOUR NOTES ---------")
                print(notes)
                print("--------------------------------")
                speak("Your notes are shown in the terminal.")
            else:
                speak("You have no saved notes.")

        except FileNotFoundError:
            speak("You have no saved notes yet.")

    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()

        if query:
            speak("Searching Google for " + query)
            google_url = "https://www.google.com/search?q=" + quote_plus(query)
            webbrowser.open(google_url)
        else:
            speak("Please type what you want to search.")

    elif command.startswith("who is "):
        query = command.replace("who is ", "", 1).strip()
        open_wikipedia(query)

    elif command.startswith("what is "):
        query = command.replace("what is ", "", 1).strip()
        open_wikipedia(query)

    elif command.startswith("tell me about "):
        query = command.replace("tell me about ", "", 1).strip()
        open_wikipedia(query)

    elif "tell me a joke" in command or command == "joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer go to the doctor? Because it caught a virus.",
            "Why was the computer cold? Because it left its Windows open."
        ]
        speak(random.choice(jokes))

    elif "system info" in command:
        info = (
            "Your system is " + platform.system() +
            ", version " + platform.release() +
            ", and architecture " + platform.machine()
        )
        print(info)
        speak(info)

    elif command == "clear":
        os.system("cls")
        show_help()

    elif command == "help":
        show_help()

    elif "stop" in command or "exit" in command or "goodbye" in command:
        speak("Goodbye. Have a nice day.")
        break

    else:
        speak("Sorry, I do not understand that command. Type help to see commands.")