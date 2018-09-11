import speech_recognition as sr
from selenium import webdriver
import time

chrome_driver=webdriver.Chrome()
#print(os.path)

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything !")
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        #print("You said: {}".format(text))
        if text.lower()!='':
            print("You said: {}".format(text))
            chrome_driver=webdriver.Chrome()
            chrome_driver.get('https://www.'+text+'.com')
            #time.sleep(5)
            #chrome_driver.close()
        else:
            print("You said nothing")
            chrome_driver.close()
    except:
        print("Sorry could not recognize what you said!")