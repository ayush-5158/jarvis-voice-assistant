# Jarvis Voice Assistant 🎙️

A Python-based voice assistant that performs basic automation tasks using voice commands.

## ✨ Features

* Wake word activation (`Jarvis`)
* Voice command recognition
* Open websites like Google & YouTube
* Play songs using voice commands
* Text-to-speech responses
* Noise adjustment for microphone
* Logging & exception handling

---

# 🛠️ Tech Stack

* Python
* SpeechRecognition
* pyttsx3
* PyAudio

---

# 📂 Project Structure

```bash
jarvis-voice-assistant/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ How It Works

1. Program continuously listens for the wake word:

   ```text
   Jarvis
   ```

2. Once activated, user can give commands like:

   ```text
   open google
   open youtube
   play sajde
   ```

3. Assistant processes the command and performs the action.

4. User can stop assistant using:

   ```text
   close
   ```

   or

   ```text
   exit
   ```

---

# 🎯 User Benefits

* Hands-free computer interaction
* Quick website access
* Instant music playback
* Beginner-friendly automation system
* Learn voice recognition & Python automation

---

# 🛠️ Customization

## 🎵 Add/Remove Songs

Modify the `SONGS` dictionary in `main.py`:

```python
SONGS = {
    "sajde": "youtube-link",
    "believer": "youtube-link"
}
```

Then say:

```text
play believer
```

---

## 🌐 Add New Website Commands

Inside `execute_command()`:

```python
elif "open github" in command_text:
    open_website("https://github.com")
```

---

## 🗣️ Change Wake Word

```python
WAKE_WORD = "jarvis"
```

Example:

```python
WAKE_WORD = "alexa"
```

---

## 🔊 Change Voice Settings

```python
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
```

---

# 💻 Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
```

## 2. Navigate to Project

```bash
cd jarvis-voice-assistant
```

## 3. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv
```

### Windows

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Program

### Mac/Linux

```bash
python3 main.py
```

### Windows

```bash
python main.py
```

---

# 🚀 Future Improvements

* AI integration
* Multi-language support

---

# ⚠️ Requirements

* Python 3.10+
* Internet connection
* Working microphone

---

# 👨‍💻 Author

Ayush Raj

Pushpanjali Kumari


GitHub: https://github.com/ayush-5158
