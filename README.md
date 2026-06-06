# JARVIS AI Assistant 🎙️

A futuristic desktop voice assistant built with Python that can perform basic automation tasks using voice commands through a modern Jarvis-inspired interface.

---

# ✨ Features

* Wake-word based activation
* Real-time voice recognition
* Text-to-speech responses
* Modern Jarvis-style desktop UI
* Open websites using voice commands
* Play songs directly from voice input
* Live assistant status updates
* Multi-threaded responsive interface

---

# 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* PyAudio
* CustomTkinter

---

# 📂 Project Structure

```bash
jarvis/
│
├── main.py
├── assistant.py
├── commands.py
├── ui.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ How It Works

1. User launches the application
2. Jarvis UI opens
3. User clicks:

   ```text
   🎤 Start Jarvis
   ```
4. Assistant starts listening for commands
5. User gives voice command
6. Jarvis processes and executes the task
7. Response is shown on UI and spoken aloud

---

# 🎯 Supported Commands

```text
open google
open youtube
play sajde
close
```

---

# 🎵 Music Playback

Songs are stored inside the `SONGS` dictionary in `commands.py`.

Example:

```python
SONGS = {
    "sajde": "youtube-link",
    "believer": "youtube-link"
}
```

User can then say:

```text
play believer
```

---

# 🌐 Add Custom Commands

Inside `commands.py`:

```python
elif "open github" in command_text:
    open_website("https://github.com")
```

Now Jarvis can open GitHub using voice commands.

---

# 🗣️ Change Wake Word

Inside `assistant.py`:

```python
WAKE_WORD = "jarvis"
```

Example:

```python
WAKE_WORD = "alexa"
```

---

# 💻 Local Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
```

---

## Navigate to Project Folder

```bash
cd jarvis-ai-assistant
```

---

## Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

### Mac/Linux

```bash
python3 main.py
```

### Windows

```bash
python main.py
```

---

# 🖥️ UI Highlights

* Dark futuristic theme
* Jarvis-inspired desktop interface
* Live command output
* Real-time status updates
* Responsive multi-threaded UI

---

# 🚀 Future Improvements

* AI chatbot integration
* Voice waveform animation
* Weather updates
* System control automation
* Multi-language support

---

# ⚠️ Requirements

* Python 3.10+
* Working microphone
* Internet connection

---

# 👨‍💻 Author

**Ayush Raj (Code and implementation of logic)**

**Pushpanjali Kumari ( Designed UI )**

GitHub: https://github.com/ayush-5158
