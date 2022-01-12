import pyttsx3
import speech_recognition as sr
import datetime
import os
# import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import instaloader 
import PyPDF2

# provides an engine for speech function which helps in text to vice convertion
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init('sapi5')  # defined an engine
voices = engine.getProperty('voices')  # defined voices to take properties from engine
engine.setProperty('voices', voices[0].id)


# Defining Speak Function - This Function will program your Jarvis to speak something.
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Defining Take command Function - This Function will allow your Jarvis to take microphone input from the user and
# returns a string output.
def takecommnad():
    r = sr.Recognizer()  # defined recognizer
    with sr.Microphone() as source:  # for microphone to work as a source
        print('Listning.....')
        r.pause_threshold = 1  # that if you pause for 1 sec it should not stop listening to you
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:  # to handle errors
        print('recognized...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

   
# Defining Wishme Function - This Function will make your Jarvis wish you according to system time.
def wishme():
    hour = int(datetime.datetime.now().hour)  # this give you the current time
    mint = int(datetime.datetime.now().minute)

    if 0 <= hour <= 12:
        speak(f"Good morning BOSS. It's {hour}:{mint} A.M.")
    elif 12 < hour <= 18:
        speak(f"Good afternoon BOSS. It's {hour}:{mint} P.M.")
    else:
        speak(f"Good evening BOSS. It's {hour}:{mint} P.M.")
    speak("I'm JARVIS, What can i do for you today?")


# send email function
def sendEmail(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sparsh0987654321@gmail.com", "T@sp23456")
    server.sendmail("sparsh0987654321@gmail.com", to, msg)
    server.close()


# fetching news from api function
def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=dcf65e7767b840e9ac05872481553980"
    # we request all data from main_url and then convert it into json format and storing it in a variable
    main_page = get(main_url).json()
    # getting articals from all data in main_page
    articals = main_page['articles']
    # an empty list where we append the titles of all the articals in the articals
    head = []
    days = ['first','second','third','fourth','fifth','sixth','seventh','eigth','ninth','tenth']
    # pushing all articals inside head list
    for artical in articals:
        head.append(artical['title'])
    # getting all titles from head and speaking it
    for i in range(len(days)):
        speak(f"todays {days[i]} news is {head[i]}")  


# reading pdf
def pdf_reader():
    # the file should be in the same folder as your program otherwise mention directory
    book = open('py3.pdf', 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"total no. of pages in teh book are{pages}")
    # since in programming indexing starts with 0 so we'll have to say teh number+1
    speak("Sir, please enter the page number that i have to read")
    pg = takecommnad().lower()
    page = pdfreader.getPage(pg)
    text = page.extractText()
    speak(text)


if __name__ == '__main__':
    wishme()
    # takecommnad()
    # speak('This is advanced Jarvis')

    # coding logic
    while True:
        # variable to store command given from teh user
        query = takecommnad().lower()

        # logic building
        # to open notepad
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        # to close notepad
        elif "close notepad" in query:
            speak("Okay Sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open microsoft teams" in query:
            npath = "C:\\Users\\Sony\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
            os.startfile(npath)

        # to  open cmd
        elif "open cmd" in query:
            os.system("start cmd")

        # to close cmd
        elif "close cmd" in query:
            os.system("taskkill /f /im cmd.exe")

        # opening camera with open cv
        # elif "open camera" in query:
        #     # Open the device at the ID 0
        #     cap = cv2.VideoCapture(1)
        #
        #     # Check whether user selected camera is opened successfully.
        #     if not (cap.isOpened()):
        #         print('Could not open video device')
        #
        #     while True:
        #         # capture image
        #         ret, img = cap.read()
        #         # Display the resulting image
        #         cv2.imshow('webcam', img)
        #         # Waits for a user input to quit the application
        #         k = cv2.waitKey(50)
        #         if k == 27:
        #             break
        #         # When everything done, release the capture
        #         cap.release()
        #         cv2.destroyAllWindows()

        # playing some music from your system
        elif "play some music" in query:
            music_dir = "D:\\8D"
            # all the music file will be conveted into list
            songs = os.listdir(music_dir)

            # for playing songs int teh list at random
            # rd = random.choice(songs)
            # os.startfile(os.path.join(music_dir, rd))

            # for  playing songs with a certain extension
            for song in songs:
                if song.endswith(".webm"):
                    os.startfile(os.path.join(music_dir, song))

        # defining online tasks

        # finding our ip address
        elif "ip address" in query:
            ip = get('https://api.ipify.org/').text
            speak(f"Sir, your IP is {ip}")

        # searching on wikipedia
        # the way you have to say to search on wikipedia """ what is python according to wikipedia """
        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            # taking query from user of what to search
            query = query.replace("wikipedia", "")
            # helps in searching teh part we said to search before wikipedia and sentences helps in telling us only
            # 2 sentences in the whole page
            result = wikipedia.summary(query, sentences=2)
            speak(f"according to wikipedia {result}")
            # print(result)

        # to open youtube on chrome
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        # to open facebook on chrome
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")

        # to open github on chrome
        elif "open github" in query:
            webbrowser.open("https://www.github.com/")

        # to open instagram on chrome
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")

        # to open STACKOVERFLOW on chrome
        elif "open stackoverflow" in query:
            webbrowser.open("https://www.stackoverflow.com/")

        # to open and search on Google on chrome
        elif "open google" in query:
            speak("Sir, what would you like to search?")
            new_query = takecommnad().lower()
            webbrowser.open(f"{new_query}")

        # sending message through whatsapp, the 00,57 was the time after 2 minutes from current time
        elif "send message" in query:
            kit.sendwhatmsg("+919458472843", "Testing message send by python", 00, 57)

        # playing songs on youtube
        elif "play songs on youtube" in query:
            speak("what do you want to play on youtube")
            # we use lower as what we say might be interpreted in all capitals or few capitals and few small so in order
            # to avoid problems in searching on browser we make it convert in lower case
            new_query = takecommnad().lower()
            kit.playonyt(f"{new_query}")

        # send email
        elif "send mail" in query:
            try:
                speak("what do you want to say?")
                msg = takecommnad().lower()
                to = "sparh.saxena2018@vitstudent.ac.in"
                # sender = "sparsh098765321@gmail.com"
                sendEmail(to, msg)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir, not able to send message")

        # to set an alarm
        elif "set alarm" in query:
            nm = int(datetime.datetime.now().hour)
            if nm == 22:
                music_dir = "D:\\8D"
                # all the music file will be conveted into list
                songs = os.listdir(music_dir)
                # for playing songs int the list at random
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

        # to find jokes
        elif "make me laugh" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # terminating the Ai
        elif "sleep" in query:
            speak("Ok sir, call me up again if you want anythng from me")
            sys.exit()

        # shutdown, restart the system
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        # elif "sleep the system":
        #     os.system("rundell32.exe powrprof.dll,SetSuspendedState 0,1,0")

        # to switch window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # to tell news headline
        elif "tell me news" in query:
            speak("Please wait sir, fetching news headlines")
            news()

        # # getting location 
        # elif "location" in query:
        #     speak("wait a moment sir, let me check!!")
        #     try:
        #         ipad = get('https://api.ipify.org/').text
        #         print(ipad)
        #         url = 'https://get.geojs.io/v1/ip/geo/'+ipad+'.json'
        #         # fetching data from teh abouve url regarding our location via ip address
        #         geo_requests = requests.get(url)
        #         # turning the data scrapped into a json fromat
        #         geodata = geo_requests.json()
        #         # print(geodata)
        #         # accessing the data by their keys as it's in the dictionary 
        #         city = geodata['city']
        #         country = geodata['country']
        #         speak(f"Sir, we're in {city} city of country {country}")
        #     except Exception as e:
        #         speak("sorry sir, due to network issues i'm not able to find our current location")

        # to check instagram profile
        elif "insta profile" in query:
            speak("Sir, please enter the username of the profile you want to check")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir, here is the instagram profile of username {name}")
            time.sleep(4)
            speak("Sir, would you like download the profile picture")
            condition = takecommnad().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("Sir the pic is downloaded")

        # to take screenshot
        elif "take a screenshot" in query:
            speak("Sir, please tell the name by which i should save this file")
            name = takecommnad().lower()
            speak("sir, please hold the screen for a minute")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Sir, Screenshot taken")

        # to read pdf
        elif "read pdf" in query:
            pdf_reader()

        # to hide and unhide folders
        elif "hide all folder" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("Sir, please tell do you want hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                speak("working on a private project sir, huh!")
                os.system("attrib +h /s /d") #os module
                speak("sir folder has been noW under hidden state")
            elif "visible" in condition:
                speak("Alright Sir, making it available for everyone, I hope you are aware what you are doing right now!!")
                os.system("attrib -h /s /d")
                speak("the folder in now visible")
            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")

    
        speak("Sir, do you have any other work")
