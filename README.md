# 🎙️ PyCommand: CLI-Based Desktop Voice Assistant

**PyCommand** is a fast and lightweight voice-controlled desktop assistant built entirely in Python. Unlike Cortana or other bulky assistants, PyCommand operates directly through your system’s command line to perform tasks like opening apps, files, or searching — all without any heavy pre-trained AI models.

---

## 🚀 Features

- 🎤 **Voice Command Execution**: Execute commands directly via voice input using your microphone.
- 🗂️ **Open Any File or App**: Launch files, folders, and applications just by saying their names.
- ⚡ **Faster than Cortana**: Lightweight execution makes it faster and more responsive.
- 💻 **Runs via Terminal**: No UI overhead — everything works from the CLI.
- 📦 **No Heavy AI Models**: Designed using native Python and speech libraries only.
- 🔊 **Text-to-Speech & Recognition**: Uses libraries like `speech_recognition` and `pyttsx3`.

---

## 🧠 Tech Stack

- **Programming Language**: Python
- **Voice Recognition**: `speech_recognition`, `pyttsx3`
- **OS Interaction**: `os`, `subprocess`, `platform`
- **Other Libraries**: `time`, `datetime`, `webbrowser`

---

## 🛠️ Getting Started

### 🔧 Requirements
Make sure Python is installed and run:
-pip install speechrecognition pyttsx3 pyaudio

# ▶️ Run the Assistant
- python pycommand.py
You’ll be prompted to speak your command — the assistant will then process and act accordingly.

## 🧪 Example Voice Commands
- "Open Chrome"
- "Play music"
- "Open project folder"
- "Search Python tutorial on YouTube"

## 📁 Folder Structure

pycommand/
- ├── pycommand.py
- ├── requirements.txt
- └── README.md
