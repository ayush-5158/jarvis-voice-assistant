import logging
import webbrowser
from typing import Dict

import pyttsx3
import speech_recognition as sr

# CONFIGURATION

SONGS: Dict[str, str] = {
    "alakh niranjan": "https://youtu.be/tkPAJPgWNr0?si=ke8ZIUVQYxBpjsBj",
    "bairan": "https://youtu.be/oafxkMv4xnc?si=OTSPV0dn7DfB9l8H",
    "sajde": "https://youtu.be/k8bXbFBItgI?si=SrDpa_pp58LJ6es3",
}

WAKE_WORD = "jarvis"


# LOGGING SETUP

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# TEXT TO SPEECH ENGINE

engine = pyttsx3.init()

#TUNING VOICE SETTING FOR BETTER SOUND QUALITY

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


# SPEECH RECOGNITION INITIALIZER

recognizer = sr.Recognizer()


# UTILITY FUNCTIONS

def speak(text: str) -> None:
    """
    Convert text to speech.
    """
    logger.info(f"Assistant: {text}")

    engine.say(text)
    engine.runAndWait()


def open_website(url: str) -> None:
    """
    Open a website in browser.
    """
    webbrowser.open(url)


def play_song(song_name: str) -> None:
    """
    Search and play a song from predefined dictionary.
    """
    song_url = SONGS.get(song_name)

    if not song_url:
        speak(f"Sorry, I could not find {song_name}")
        return

    speak(f"Playing {song_name}")
    open_website(song_url)


def execute_command(command_text: str) -> None:
    """
    Process user commands.
    """
    command_text = command_text.lower().strip()

    logger.info(f"Executing command: {command_text}")

    if "open google" in command_text:
        speak("Opening Google")
        open_website("https://www.google.com")

    elif "open youtube" in command_text:
        speak("Opening YouTube")
        open_website("https://www.youtube.com")

    elif command_text.startswith("play"):
        song_name = command_text.replace("play", "", 1).strip()

        if not song_name:
            speak("Please tell me the song name")
            return

        play_song(song_name)

    else:
        speak("Sorry, I don't understand that command")


def listen(timeout: int = 5, phrase_time_limit: int = 8) -> str | None:
    """
    Listen to microphone input and return recognized text.
    """
    try:
        with sr.Microphone() as source:
            logger.info("Listening...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        text = recognizer.recognize_google(audio)

        logger.info(f"User said: {text}")

        return text.lower()

    except sr.WaitTimeoutError:
        logger.warning("Listening timeout")
        return None

    except sr.UnknownValueError:
        logger.warning("Could not understand audio")
        return None

    except sr.RequestError as e:
        logger.error(f"Speech recognition API error: {e}")
        return None

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        return None


# MAIN APPLICATION

def activate_assistant() -> None:
    """
    Start assistant after wake word detection.
    """
    speak("Jarvis activated. How can I help you Ayush sir?")

    while True:
        query = listen()

        if not query:
            continue

        if "close" in query or "exit" in query:
            speak("Closing assistant")
            break

        execute_command(query)


def main() -> None:
    """
    Main application loop.
    """
    logger.info("Voice assistant started")

    while True:
        text = listen()

        if not text:
            continue

        if WAKE_WORD in text:
            logger.info("Wake word detected")
            activate_assistant()


# ENTRY POINT

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting assistant...")