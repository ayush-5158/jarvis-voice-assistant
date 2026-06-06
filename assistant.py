import speech_recognition as sr
import pyttsx3

from commands import execute_command

recognizer = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text: str):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        text = recognizer.recognize_google(audio)

        return text.lower()

    except Exception:
        return None


def run_assistant(update_ui):

    speak("Jarvis online")

    while True:

        update_ui("🎤 Listening...")

        query = listen()

        if not query:
            continue

        update_ui(f"You said: {query}")

        if "close" in query:
            update_ui("Assistant stopped")
            speak("Shutting down")
            break

        execute_command(query, speak)