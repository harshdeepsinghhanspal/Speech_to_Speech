# 🎤 Voice-Powered AI Chatbot with Llama3 (Groq) 🚀

This project is a **voice-based AI chatbot** that listens to user input, processes it using **Groq's Llama3 model via LangChain**, and responds with synthesized speech. It leverages **speech recognition (Google API)** and **text-to-speech (pyttsx3)** for a seamless interactive experience. 🗣️🤖

## 📌 Features
- 🎙️ **Voice recognition** using `speech_recognition`
- 🧠 **AI-powered responses** with Groq's Llama3 via LangChain
- 🔊 **Text-to-Speech (TTS)** using `pyttsx3`
- 🔄 **Real-time conversation** loop until 'exit' is spoken

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/voice-chatbot-groq.git
   cd voice-chatbot-groq
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Groq API key** 🔑
   ```bash
   export GROQ_API_KEY="your-api-key-here"  # Linux/macOS
   set GROQ_API_KEY="your-api-key-here"     # Windows (cmd)
   ```
   **OR** set it inside the script before running.

## ▶️ Usage

Run the script:
```bash
python chatbot.py
```

### How It Works 🏗️
1. The program **listens** for voice input.
2. The input is **converted to text** using Google's Speech API.
3. The text is **sent to Groq's Llama3** model via LangChain.
4. The AI response is **spoken back** using `pyttsx3`.

Say **'exit'** to quit the chat.

## 📦 Dependencies
- `speech_recognition`
- `pyttsx3`
- `langchain`
- `langchain_groq`

## ⚠️ Notes
- Ensure your microphone is working.
- The Google Speech API requires an internet connection.
- Pyttsx3 works offline for TTS.
- You need a **valid Groq API key** to use the Llama3 model.
