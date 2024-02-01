# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import win32com.client as wincom

import requests
while True:
    city = input("Enter the name of city : ")
    url =f"http://api.weatherapi.com/v1/current.json?key=308aab834825445c902123219243101&q={city}"
    r = requests.get(url)
    speak = wincom.Dispatch("SAPI.SpVoice")
    # print(r.text)
    dic = json.loads(r.text)
    # print(dic["current"]["temp_c"])
    w = dic["current"]["temp_c"]
    text = f"The current weather is {city} is {w } degrees"
    speak.Speak(text)
    print(f"The current weather is {city} is {w } degrees")