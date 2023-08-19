# PROJECT 10:-     VOICE ASSISTANT : "MARCH"

# Feautures of march:
# 1. Accessing Youtube 
# 2. Accessing Whatsapp
# 3. Accessing Google
# 4. Give accurate data and time
# 5. Playing querys
# 6. Get information about anything
# 7. Generate qr code of anything   
# 8. Accessing primevideos
# 9. Instagram birthday story handling

import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import datetime
import wikipedia
import qrcode
from supporter import *
from PIL import Image

import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Function: To convert speech into text..
def speechtotext():
    SR = sr.Recognizer()  # calling class "Recognizer" in object SR
    with sr.Microphone() as source:
        print("LISTENING...")

        SR.adjust_for_ambient_noise(source)  # To avoid noises
        audio = SR.listen(source, None, 10)  # Its like the variable whose listen as
        SR.pause_threshold = 1 
        try:
            print("recognizing..")
            # variable to stored whatever we say..
            data = SR.recognize_google(audio, language='en-US')
            return data
        except Exception as e:                # in case user don't say anything
            print("Sorry! Can you repeat please..")
            return "None"
    # stop_listening = SR.listen_in_background(sr.Microphone(),data)     # To listen the task in background
    # stop_listening()


# Function to convert the text into speech
def texttospeech(text):
    engine = pyttsx3.init('sapi5')
    # set voice of voice assistant
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0,1:female voice
    # rate of voice of voice assistant
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    # final step to make voice assistant to say something..
    engine.say(text)
    engine.runAndWait()

#Function: To generate qrcode
def qrcode_generataor():
    texttospeech("qrcode content sir")
    text=speechtotext().strip()
    gen_qr= qrcode.make(f"{text}")
    texttospeech("give me name to save qrcode sir")
    save=speechtotext().strip()
    texttospeech("saving  qrcode as"+ save +".png")
    gen_qr.save(f"{save}.png")
    texttospeech("Qrcode generated successfully")
    
#Function: To automate whatsapp tasks
def auto_whatsapp():
    texttospeech("want to send message? ")
    ans=speechtotext().lower()
    if ans == "yes":
        texttospeech("In a group sir?")
        ans_1=speechtotext().lower()
        if ans_1 == "yes":
            texttospeech("group name sir")
            group_name=speechtotext().lower()
            if "toli" in group_name:
                texttospeech("what message you want me to text? ")
                mesg=speechtotext()
                print(mesg)
                pywhatkit.sendwhatmsg_to_group_instantly(group_id="FoE5OZPBI7MCEwZ2S3RzwD",message=f"{mesg}",tab_close= True)
                texttospeech("message sent")
            else:
                texttospeech("Group not found")
    else:
        texttospeech("checking for messages in whatsapp for you")
        webbrowser.open("https://web.whatsapp.com/")
        texttospeech("is there anything you want me to do")

#Function accessing wikipedia
def wiki():
    texttospeech("what's your query sir?")
    query=speechtotext().lower()
    texttospeech("okay Searching"+ query)
    try:    
        if " who is " in query:
            query=query.replace("who is"," ")
            print(query)
            result=wikipedia.summary(query,sentences=2)
            print(result)
            texttospeech("According to wikipedia"+ result)
        elif "what is " in query:
            query=query.replace("what is"," ")
            print(query)
            result=wikipedia.summary(query,sentences=2)
            print(result)
            texttospeech("According to wikipedia"+ result)
        elif "where is " in query:
            query=query.replace("where is"," ")
            print(query)
            result=wikipedia.summary(query,sentences=2)
            print(result)
            texttospeech("According to wikipedia"+ result)
        else:
            result=wikipedia.summary(query,sentences=2)
            print(result)
            texttospeech("According to wikipedia"+ result)
    except :
        texttospeech("sorry sir, didn't found your query")

# Function: To comtrol google in chrome 
def chrome_automate(search):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--headlesss')
    chrome_options.add_experimental_option("detach", True)

    Path= "database\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(Path,options=chrome_options)
    driver.maximize_window()
    driver.get(search)



# command to perform tasks:
def task():
    
    while True:
    
        command = speechtotext()
        command = command.lower()
        print(command)

        # 0.Introduced March
        if "yourself" in command:
            texttospeech("helloo! My name is March. I am voice assistant and may be become your friend someday")
            texttospeech("what your name sir?")
            name = speechtotext().lower()
            name = name.replace("my name is", " ")
            texttospeech("Nice to meet you" + name)
            task()

        # 1.Accesssing youtube
        elif "youtube" in command:
            texttospeech("okay sir! Opening Youtube")
            texttospeech("what you want to search,sir?")
            query_1=speechtotext().lower()
            texttospeech("Searching your query")
            search=(f"https://www.youtube.com/results?search_query={query_1}")
            chrome_automate(search)
            texttospeech("video found")

        # 2.Accessing Google
        elif "google" in command:
            texttospeech("Opening google")
            search=("https://www.google.com/")
            chrome_automate(search)

        # 3.Asking to open whatsapp
        elif "whatsapp" in command:
            texttospeech("As you wish sir! Opening whatsapp")
            auto_whatsapp()

        # 4.Playing query or video in youtube
        elif "play" in command:
            query = command.replace("play", " ")
            texttospeech("Okay sir! Playing" + query)
            pywhatkit.playonyt(query)

        # 5.Asking time and date
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M:%p")  # %I: Hours, %M: Minutes, %p=am/pm
            texttospeech("Sir! Right now the time is" + time)

        # 6.Search query using wikipedia
        elif "wikipedia" in  command:
           texttospeech("Opening wikipedia for you")
           wiki()
        
        # 7.Anime :
        elif "anime" in command:
            texttospeech("Opening Anime")
            search="https://9animetv.to/"
            chrome_automate(search)


        # 8.Generate qrcode 
        elif "generate qr code" in command:
            texttospeech("Generate QR code for you sir")
            texttospeech("It might need your help sir")
            qrcode_generataor()

        # 9.Accessing primevideos
        elif "prime" in command:
            texttospeech("As you wish, opening amazon primevideos for you")
            texttospeech("which movie you want to see sir?")
            movie=speechtotext().lower()
            texttospeech("playing"+ movie + " for you ")
            search=(f"https://www.primevideo.com/search/ref=atv_sr_sug_7?phrase={movie}%20movie&ie=UTF8")
            chrome_automate(search)
         
        # 10.Handling instagram stories
        elif "story" in command:
            texttospeech("okay!")
            texttospeech("Collecting best instagram stories temmplate for you") 
            search=("https://designs.ai/designmaker/start/designs/64108abfaae134057cdbe9d9/edit?category=5d503d6df8ead94a97909bf9")
            chrome_automate(search)

        # 11.Exit
        else:
             if "exit" in command :
                 texttospeech("okay sir!")
                 texttospeech("I am leaving")
                 texttospeech("call me if you want anything")
                 break
             else:
                 command

#main function 
if __name__ == "__main__":

    A_command = speechtotext()
    # Activated voice assistant, 
    if 'March' in A_command:
        texttospeech("Activating voice assistant, March!")
        texttospeech("hello sir! how may i assist you? ")
        task()
