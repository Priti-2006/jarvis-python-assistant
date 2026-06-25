# ─────────────────────────────────────────
# voice_jarvis.py — Voice Input for Jarvis
# ─────────────────────────────────────────

import speech_recognition as sr
import pyttsx3

# ── Initialize Text to Speech ──
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    """Convert text to speech"""
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone and return text"""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        recognizer.pause_threshold = 1.0
        recognizer.energy_threshold = 300

        try:
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=10
            )
            print("🔄 Processing...")
            text = recognizer.recognize_google(
                audio, language="en-IN"
            )
            print(f"You said: {text}")
            return text.lower()

        except sr.WaitTimeoutError:
            print("⏰ No speech detected.")
            return None

        except sr.UnknownValueError:
            print("❌ Could not understand.")
            return None

        except sr.RequestError:
            print("❌ No internet connection.")
            return None

        except Exception as e:
            print(f"❌ Microphone error: {e}")
            return None

def get_command(use_voice=True):
    """Get command from voice OR keyboard"""
    if use_voice:
        command = listen()
        if command:
            return command
        else:
            # Fallback to keyboard if voice fails
            print("💬 Voice failed — type your command:")
            typed = input("Type command: ").lower().strip()
            return typed if typed else None
    else:
        typed = input("\nType a command: ").lower().strip()
        return typed if typed else None