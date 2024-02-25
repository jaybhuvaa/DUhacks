import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3
import json


name='Jay'
roll=10

status=True
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