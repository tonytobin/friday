
from colorama.ansi import Style
import speech_recognition as sr
import time
import datetime
import playsound
import os
from os import kill
import random
from gtts import gTTS
import webbrowser
import wikipedia
import bs4 as bs
import lxml
import urllib.request
import certifi
import requests
import subprocess
import ssl
import pyttsx3
import serial

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

class person:
    name=''
    def setName(self,name):
        self.name=name

r = sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',200)



def jarvis(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def anger():
    status('q')
    print('\x1b[0;37;41m' + 'anger hormone triggered' + '\x1b[0m')
    friday_speak('do you have some problems hearing me')
    response=record()
    if 'no' in response:
        friday_speak('then why are you making me angry')
        friday_speak('say sorry or else i am not talking to you')
        response=record()
        while response != 'sorry':
            phrase=["i am not talking to you unless you say sorry","say sorry or we will not talk again","i don't want to hear any excuse"]
            friday_speak(random.choice(phrase))
            response=record()
        if 'sorry' in response:
            friday_speak('ok, but do not irritate me again')
            

    elif 'yes' in response:
        friday_speak('i think i am having problems with my speech synthesiser')
        friday_speak('shutting down for repairs')
        quit()        

def increment():
    global count    
    count+=1
    return count                
   
def status(colr):
    try:
        mcu=serial.Serial('/dev/cu.usbserial-0001',9600)
        colour=bytes(colr,'utf-8')
        mcu.write(colour)
        mcu.close()
    except serial.PortNotOpenError as led:
        print('port is busy')    
    except serial.SerialException as pmiss:
        print('status reporter missing')    
        

#def intro():
#   introd=subprocess.Popen("pymatrix-rain")
#   print(introd)
#   playsound.playsound('intro.mp3')
#   introd.kill()
#   os.system("clear")


    

def record(ask=False):
    status('l')
    with sr.Microphone() as source:
        if ask:
             friday_speak(ask) 
 #       r.adjust_for_ambient_noise(source)
        audio = r.listen(source,5,5)
        voice_data = ''
 #       status('y')
        try:          
            voice_data = r.recognize_google(audio)
            print(voice_data)
#            status('w')
        except sr.UnknownValueError:
            friday_speak('could you repeat')
#            status('r')
        except sr.RequestError:
            friday_speak('looks like i am offline')
 #           status('r')        
        return voice_data.lower()

def friday_speak(audio_string):
    status('s')
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    


def respond(voice_data):
    if there_exists(['what is your name','who are you']):
        try:

           databs=open("operator.txt","r")
           operatorname=databs.read()
           operator=operatorname.split("is")[-1].strip()
           person_obj.setName(operator)
           databs.close()
        except FileNotFoundError as dbmissing:
            databs=open("operator.txt","w") 

            databs.close()
        
        if person_obj.name:
             friday_speak('my name is friday')
        else:
            friday_speak('my name is friday, what is your name')
            voice_data=record()
            person_name=voice_data.split("is")[-1].strip()
            friday_speak('ok i will remeber your name ')
            friday_speak(person_name)
            person_obj.setName(person_name)
            database=open("operator.txt","+w")
            database.write("operator name is "+person_name)
            print("name added to database succefully")
            database.close()


    
    if'can i change your name' in voice_data:
        friday_speak('sorry that is not possible now')

    if'what is your real name' in voice_data:
        friday_speak('my name stands for female replacement intelligent digital assistant youth but you can call me friday')

    if there_exists(["what is my name"]):
        friday_speak("Your name must be " + person_obj.name)

    if there_exists(['hey','hi','hello','are you there']):
        trigger=increment()
        if trigger==4:
            global count
            count=1
            anger()
        else :    
           greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
           greet = greetings[random.randint(0,len(greetings)-1)]
           friday_speak(greet)
        
        

    if there_exists(["definition of"]):
        if there_exists([" an"]):
            definetext=voice_data.split("an")
        else:    
            definetext=voice_data.split(" of")
        tofind=definetext[1]
        definition=tofind
        try:
            definitions=wikipedia.summary(definition, 2)
            friday_speak('let me search my database for '+definition)
            friday_speak(definitions)
        except wikipedia.DisambiguationError as e:
            friday_speak('i am sorry i cannot find this in my database')
        
        
  
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        time = datetime.datetime.now().strftime('%I,%M ,%p')
        friday_speak('current time is'+time)
        
    
    if there_exists(["where am i"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=62351e81b2d4c0baa0ea9a6677aad67bf456e471e4e395c5a50d0a90').json()
        loc = Ip_info['region']
        continent=Ip_info['continent_name']
        country=Ip_info['country_name']
        lattitude=str(Ip_info['latitude'])
        longitude=str(Ip_info['longitude'])
        friday_speak('connecting to location services')
        friday_speak('location found, you are in '+loc)
        friday_speak('in '+country)    
        friday_speak('which is in '+continent)
        friday_speak('with lattitude of '+lattitude)
        friday_speak('and Longitude of'+longitude)

#    if there_exists(["my name is"]):
#       person_name = voice_data.split("is")[-1].strip()
#        friday_speak(f"okay, i will remember that {person_name}")
#        person_obj.setName(person_name)

    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        data = voice_data.split("is")
        eqn=data[1].split(" ")
        opr=eqn[2]
        firstnum=eqn[1]
        secondnum=eqn[3]
        if opr == '+':
            sum=str(float(firstnum) + float(secondnum))
            friday_speak('the sum of '+firstnum)
            friday_speak('and' +secondnum)
            friday_speak('is'+sum)
        elif opr == '-':
            sub=str(float(firstnum) - float(secondnum))
            friday_speak('the subtraction of '+secondnum)
            friday_speak(' from '+firstnum)
            friday_speak('is ' +sub)
        elif opr == '*':
            multy=str(float(firstnum) * float(secondnum))
            friday_speak('the multiplication of '+firstnum)
            friday_speak('and '+secondnum)
            friday_speak('is '+multy)
        elif opr == '/':
            division=str(float(firstnum) / float(secondnum))
            friday_speak('the division of '+firstnum)
            friday_speak('by '+secondnum)
            friday_speak('is '+division)

        
    if 'what can you do for me' in voice_data:
        friday_speak('for the time being, nothing')
    
    if 'send me nudes' in voice_data:
        friday_speak('ok smile please let me take your picture and i will ask fbi to bring some nudes for you')
 # just for fun  

    if there_exists(["how are you","how are you doing"]):
        friday_speak("I'm very well, thanks for asking " + person_obj.name)   

    if there_exists(["tell me about yourself"]):
        friday_speak('i work on 2 rules')
        friday_speak('the first rule is always listen to my boss')
        friday_speak('never harm any human beings and animals')
        
    elif 'tell me about your hardware' in voice_data:
        friday_speak('i have no idea where am i') 

    elif there_exists(['you can take rest','stanby for repairs','shut down','shutdown all system','sleep']):
        friday_speak('shutting down all systems')
        os.system("clear")
        status('q')
        exit()
    


time.sleep(1)
person_obj = person()
count=1
#intro()
#jarvis('sir,, i am initialising the last working instance of your new project friday')
friday_speak('all systems online sir')
err=1
while 1:
     voice_data = record()       
     respond(voice_data)