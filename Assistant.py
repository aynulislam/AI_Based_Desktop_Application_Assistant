import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("good morning!")
        speak("i am jervis sir, my creator is tamjid! please tell me how may i help you.")  

    elif hour>=12 and hour<18:
        speak("good afternoon!")
        speak("i am jervis sir, my creator is tamjid! please tell me how may i help you.")  

    else:
        speak("good evening!")  
        speak("i am jervis sir, my creator is tamjid! please tell me how may i help you.")  
            
    
def takecommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: , {query}\n")

    except Exception as e:
        print(e)
        print("say that again please......")
        return "None"
    return query


def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Mail ID','Pass')
    server.sendmail('itamxeed7@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishme()
    #if 1:
    while True:
        query = takecommand().lower()


    
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")            
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")


        elif 'play music number 1' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play music number 2' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))


        elif 'play music number 3' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'play music number 4' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))  

        elif 'play music number 5' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[4]))         



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        

        elif 'please send mail' in query:
            try:
                speak('what should i say?')
                content = takecommand()
                to ='mahbubmounir@gmail.com'
                sendemail(to, content)
                speak('email has been sent!')
            except Exception as e:
                print(e)
                speak('sorry my dear friend, i am not able to send this e-mail')

            
            



        



    





