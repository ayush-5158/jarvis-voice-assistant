import webbrowser

SONGS = {
    "alakh niranjan": "https://youtu.be/tkPAJPgWNr0",
    "bairan": "https://youtu.be/oafxkMv4xnc",
    "sajde": "https://youtu.be/k8bXbFBItgI"
}


def execute_command(command_text: str, speak):
    command_text = command_text.lower().strip()

    if "open google" in command_text:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command_text:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command_text.startswith("play"):
        song_name = command_text.replace("play", "", 1).strip()

        song_url = SONGS.get(song_name)

        if song_url:
            speak(f"Playing {song_name}")
            webbrowser.open(song_url)
        else:
            speak("Song not found")

    else:
        speak("Command not recognized")