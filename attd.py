import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""
    

#@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    speak("Hello, I am your assistant. How can I help you?")    
    init=recognize_speech()

    if "mark attendance" in init:
        speak("please tell me name and roll number of the student")
        name=recognize_speech()
        roll=recognize_speech()
        speak("present or absent")
        status=recognize_speech()
        with open("data.json", "r") as f:
            data = json.load(f)
            new_student = {
            "name": name,
            "roll_no": int(roll),
            "status": status
        }
            data["student"].append(new_student)
        with open("data.json", "w") as f:
            json.dump(data, f)

    elif "exit" in init:
        speak("Goodbye")
        exit()
    
    # response = {"message": "Attendance marked successfully"}
    # return jsonify(response)

mark_attendance()

# if __name__ == '__main__':
#     app.run(debug=True , host='0.0.0.0')