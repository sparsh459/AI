import pyttsx3
import speech_recognition as sr
import datetime
import os
# import cv2
# import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

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

    if 0 <= hour <= 12:
        speak("Good morning BOSS")
    elif 12 < hour <= 18:
        speak("Good afternoon BOSS")
    else:
        speak("Good evening BOSS")
    speak("I'm JARVIS, What can i do for you today?")


# send email function
def sendEmail(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sparsh0987654321@gmail.com", "T@sp23456")
    server.sendmail("sparsh0987654321@gmail.com", to, msg)
    server.close()


if __name__ == '__main__':
    wishme()
    # takecommnad()
    # speak('This is advanced Jarvis')

    # coding logic
    while True:
        # variable to store command given from teh user
        query = takecommnad().lower()

        # logic building
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open microsoft teams" in query:
            npath = "C:\\Users\\Sony\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
            os.startfile(npath)

        elif "open cmd" in query:
            os.system("start cmd")

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

        # terminating the Ai
        elif "no thanks" in query:
            speak("Ok sir, call me up again if you want naythng from me")
            sys.exit()

        speak("Sir, do you have any other work")
