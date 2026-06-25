import pyttsx3
import datetime
import webbrowser
import os
import subprocess
import platform
import random
from urllib.parse import quote_plus
import speech_recognition as sr

# ── Initialize Text to Speech ──
engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

# ── SPEAK + PRINT BOTH ──
def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# ── LISTEN TO MICROPHONE ──
def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\n🎤 Listening... speak now")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recognizer.pause_threshold = 1.0
            recognizer.energy_threshold = 150
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=12)
        print("🔄 Processing your speech...")
        command = recognizer.recognize_google(audio, language="en-IN")
        print("✅ You said:", command)
        return command.lower()
    except sr.WaitTimeoutError:
        print("⏰ No speech detected. Please try again.")
        return None
    except sr.UnknownValueError:
        print("❌ Could not understand. Please speak clearly.")
        speak("Sorry, I could not understand. Please try again.")
        return None
    except sr.RequestError:
        print("❌ Internet connection error.")
        speak("Internet connection is required for voice recognition.")
        return None
    except Exception as e:
        print("❌ Microphone error:", e)
        speak("There is a microphone problem. Please check your mic.")
        return None

# ── WISH USER ──
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! I am Jarvis. How can I help you today?")
    elif hour < 18:
        speak("Good afternoon! I am Jarvis. How can I help you today?")
    else:
        speak("Good evening! I am Jarvis. How can I help you today?")

# ── SHOW HELP ──
def show_help():
    print("""
========= JARVIS VOICE COMMANDS =========

  hello / hi jarvis
  time / date

  open youtube
  open google
  open linkedin
  open github
  open spotify
  open notepad
  open calculator
  open vscode
  open command prompt
  open file explorer

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
  stop / exit / goodbye / bye

=========================================
""")

# ── WIKIPEDIA ──
def open_wikipedia(query):
    if not query:
        speak("Please say a topic to search on Wikipedia.")
        return
    speak("Okay! I am searching Wikipedia for " + query)
    print("🌐 Opening Wikipedia for:", query)
    webbrowser.open("https://en.wikipedia.org/w/index.php?search=" + quote_plus(query))

# ══════════════════════════════════════
#           START JARVIS
# ══════════════════════════════════════
print("\n========= JARVIS IS STARTING =========\n")
wish_user()
show_help()
speak("Voice mode is active. I am ready. You can speak your commands now.")

# ══════════════════════════════════════
#           MAIN LOOP
# ══════════════════════════════════════
while True:

    # ── Listen to microphone ──
    command = listen()

    # ── If voice failed, ask to type ──
    if not command:
        print("\n💬 Voice failed — please type your command:")
        command = input(">>> ").lower().strip()

    if not command:
        continue

    # ══ HELLO ══
    if "hello" in command or "hi jarvis" in command or "hey jarvis" in command:
        speak("Hello! I am Jarvis. How can I help you today?")

    # ══ TIME ══
    elif "time" in command:
        t = datetime.datetime.now().strftime("%I:%M %p")
        print("🕐 Current Time:", t)
        speak("The current time is " + t)

    # ══ DATE ══
    elif "date" in command:
        d = datetime.datetime.now().strftime("%d %B %Y")
        print("📅 Today's Date:", d)
        speak("Today's date is " + d)

    # ══ OPEN YOUTUBE ══
    elif "open youtube" in command:
        print("▶️  Opening YouTube...")
        speak("Okay! I am opening YouTube for you.")
        webbrowser.open("https://www.youtube.com")

    # ══ OPEN GOOGLE ══
    elif "open google" in command:
        print("🔍 Opening Google...")
        speak("Okay! I am opening Google for you.")
        webbrowser.open("https://www.google.com")

    # ══ OPEN LINKEDIN ══
    elif "open linkedin" in command:
        print("💼 Opening LinkedIn...")
        speak("Okay! I am opening LinkedIn for you.")
        webbrowser.open("https://www.linkedin.com")

    # ══ OPEN GITHUB ══
    elif "open github" in command:
        print("🐙 Opening GitHub...")
        speak("Okay! I am opening GitHub for you.")
        webbrowser.open("https://www.github.com")

    # ══ OPEN SPOTIFY ══
    elif "open spotify" in command:
        print("🎵 Opening Spotify...")
        speak("Okay! I am opening Spotify for you.")
        webbrowser.open("https://open.spotify.com")

    # ══ OPEN NOTEPAD ══
    elif "open notepad" in command:
        print("📝 Opening Notepad...")
        speak("Okay! I am opening Notepad for you.")
        os.system("notepad")

    # ══ OPEN CALCULATOR ══
    elif "open calculator" in command:
        print("🔢 Opening Calculator...")
        speak("Okay! I am opening Calculator for you.")
        subprocess.Popen("calc")

    # ══ OPEN VSCODE ══
    elif "open vscode" in command or "open visual studio" in command:
        print("💻 Opening Visual Studio Code...")
        speak("Okay! I am opening Visual Studio Code for you.")
        os.system("code")

    # ══ OPEN CMD ══
    elif "open command prompt" in command or "open cmd" in command:
        print("⌨️  Opening Command Prompt...")
        speak("Okay! I am opening Command Prompt for you.")
        os.system("start cmd")

    # ══ OPEN FILE EXPLORER ══
    elif "open file explorer" in command:
        print("📁 Opening File Explorer...")
        speak("Okay! I am opening File Explorer for you.")
        os.system("explorer")

    # ══ TAKE NOTE ══
    elif "take note" in command or "write note" in command:
        print("📝 Note mode activated...")
        speak("Sure! Please say your note now. I am listening.")
        note = listen()
        if note:
            with open("notes.txt", "a", encoding="utf-8") as f:
                timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
                f.write(f"[{timestamp}] {note}\n")
            print("✅ Note saved:", note)
            speak("Done! Your note has been saved successfully.")
        else:
            speak("Sorry, no note was saved. Please try again.")

    # ══ SHOW NOTES ══
    elif "show notes" in command or "read notes" in command:
        try:
            with open("notes.txt", "r", encoding="utf-8") as f:
                notes = f.read()
            if notes.strip():
                print("\n========= YOUR SAVED NOTES =========")
                print(notes)
                print("=====================================")
                speak("Here are your saved notes. They are shown on the screen.")
            else:
                speak("You have no saved notes at the moment.")
        except FileNotFoundError:
            speak("You have no saved notes yet. Say take note to add one.")

    # ══ SEARCH ══
    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        if query:
            print("🔍 Searching Google for:", query)
            speak("Okay! I am searching Google for " + query)
            webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))
        else:
            speak("Please say what you want to search after the word search.")

    # ══ WHO IS ══
    elif command.startswith("who is "):
        open_wikipedia(command.replace("who is ", "", 1).strip())

    # ══ WHAT IS ══
    elif command.startswith("what is "):
        open_wikipedia(command.replace("what is ", "", 1).strip())

    # ══ TELL ME ABOUT ══
    elif command.startswith("tell me about "):
        open_wikipedia(command.replace("tell me about ", "", 1).strip())

    # ══ JOKE ══
    elif "joke" in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer go to the doctor? Because it caught a virus.",
            "Why was the computer cold? Because it left its Windows open.",
            "Why do Java developers wear glasses? Because they do not C sharp.",
            "A SQL query walks into a bar and asks two tables, can I join you?",
            "Why did the programmer quit his job? Because he did not get arrays.",
            "How do you comfort a JavaScript bug? You console it."
        ]
        joke = random.choice(jokes)
        print("😂 Joke:", joke)
        speak(joke)

    # ══ SYSTEM INFO ══
    elif "system info" in command:
        info = (
            "System: " + platform.system() +
            " | Version: " + platform.release() +
            " | Architecture: " + platform.machine() +
            " | Processor: " + platform.processor()
        )
        print("\n💻 System Info:")
        print(info)
        speak("Here is your system information. " + info)

    # ══ CLEAR ══
    elif "clear" in command:
        os.system("cls" if os.name == "nt" else "clear")
        speak("Screen cleared. Ready for your next command.")

    # ══ HELP ══
    elif "help" in command:
        show_help()
        speak("The full command list is now shown on the screen.")

    # ══ STOP / EXIT ══
    elif "stop" in command or "exit" in command or "goodbye" in command or "bye" in command:
        print("\n========= JARVIS SHUTTING DOWN =========")
        print("JARVIS: Goodbye! It was great talking to you.")
        print("JARVIS: See you soon. Have a wonderful day!")
        print("JARVIS: Bye bye!")
        print("=========================================\n")
        speak("Goodbye! It was great talking to you. See you soon. Have a wonderful day. Bye bye!")
        break

    # ══ UNKNOWN ══
    else:
        print("❓ Unknown command:", command)
        speak("Sorry, I do not understand that command. Say help to see all available commands.")