import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvic' in command:
                command = command.replace('jarvic', '')
                print(command)
    except:
      pass
    return command

def run_jarvic():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with Vishal')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'priyanshu' in command:
        talk('Bestfriend and best partaner')
    elif 'sorry' in command:
        talk('sorry priyanshu + give me a kiss')
    elif 'vijay' in command:
        talk('sorry i have not say any thing off this person because this is totaly made gay ')
    elif 'mohit' in command:
        talk('mohit a very small boy sorry not boy this is a men')

    else:
        talk('please say the command again,')


while True:
    run_jarvic()

