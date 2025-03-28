import speech_recognition as sr
import pyttsx3
import os
from langchain_groq import ChatGroq  # Corrected import
from langchain_core.messages import ChatMessage  # Use ChatMessage instead of SystemMessage

# Set up Groq API key (THIS WILL BE DELETED)
os.environ["GROQ_API_KEY"] = "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"

# Initialize Llama model via LangChain
llm = ChatGroq(model_name="llama3-8b", temperature=0.7)  # Ensure correct model name

# Speech recognizer setup
recognizer = sr.Recognizer()

# Text-to-Speech setup
engine = pyttsx3.init()

def listen():
    """Capture voice input and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand, please repeat.")
            return None
        except sr.RequestError:
            print("API unavailable.")
            return None

def chat_with_groq(user_input):
    """Send user input to Llama model and get response."""
    messages = [
        ChatMessage(role="system", content="You are a helpful AI assistant."),
        ChatMessage(role="user", content=user_input)
    ]
    response = llm.invoke(messages)  # Use `.invoke()`
    return response.content

def speak(response):
    """Convert text response to speech."""
    print(f"AI: {response}")
    engine.say(response)
    engine.runAndWait()

if __name__ == "__main__":
    print("Say 'exit' to quit.")
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() == "exit":
                speak("Goodbye!")
                break
            ai_response = chat_with_groq(user_input)
            speak(ai_response)
