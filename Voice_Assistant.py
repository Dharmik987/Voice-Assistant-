import speech_recognition as sr
from gtts import gTTS
import os

def speak(text):
    # Convert text to speech and play it
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("termux-media-player play response.mp3")  # On Termux
    # For non-Termux users, use the default media player
    # os.system("mpv response.mp3")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, there was an issue with the service.")
        except sr.WaitTimeoutError:
            speak("You were silent for too long.")
        return ""

def main():
    speak("Hello Dharmik! How can I assist you today?")
    while True:
        command = listen_command()
        if "hello" in command:
            speak("Hello! How are you?")
        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")
        elif "your name" in command:
            speak("I am your voice assistant.")
        elif "exit" in command or "stop" in command:
            speak("Goodbye Dharmik! Have a nice day.")
            break
        else:
            speak("I'm sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()