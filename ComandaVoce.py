import time
import speech_recognition as sr
import subprocess
import pyttsx3 as p
import os
import webbrowser
import psutil

def VoiceCommand():
    timp = 33
    while True:
        r = sr.Recognizer()
        engine = p.init()
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[0].id)
        #while True:
        with sr.Microphone() as source:
            print("Recording...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                if "Open" or "open" in text:
                    print('aici merge')
                    if "in browser" or "on browser" in text:
                        print("aici? ",text)
                        split_text = text.split()
                        if split_text[split_text.index('open') + 1] == "in" or split_text[split_text.index('open') + 1] == "on":
                            text = split_text[split_text.index('browser') + 1]
                            engine.say("Open," + str(text))
                            print("https://www."+text+".com/")
                            webbrowser.open_new_tab("https://www."+text+".com/")
                            text = None
                            timp = 33
                            continue
                        text = split_text[split_text.index('open') + 1]
                        engine.say("Open," + str(text))
                        print("https://www."+text+".com/")
                        webbrowser.open_new_tab("https://www."+text+".com/")
                        text = None
                        timp = 33
                        continue
                    if 'browser' in text:
                        text = 'Opera'
                    if 'lol' in text:
                        text = 'League of Legends'
                    engine.say("Open," + str(text))
                    engine.runAndWait()
                    engine.stop()
                    text = text.lstrip() + str(".lnk")
                    text_first_letter = text[0]
                    text_upper_letter = text[0].upper()
                    text = text.replace(text_first_letter, text_upper_letter, 1)
                    print ('Open, ' + text)
                    for r,d,f in os.walk("C:\\"):
                        for files in f:
                            if files == text:
                                x = os.path.join(r,files)
                                os.startfile(x)
                    text = None
                    timp = 33
                    continue
                elif "Close" in text:
                    if 'League of Legends' in text:
                        engine.say("Closing," + str(text))
                        subprocess.call(["taskkill","/F","/IM","LeagueClient.exe"])
                    text = text + ".exe"
                    print("Closing", text)
                    engine.say("Closing," + str(text))
                    subprocess.call(["taskkill","/F","/IM",text])
                    text = None
                    timp = 33
                    continue
                else:
                    print('I don`t understand you :<')
                    text = None
                    timp = 33
                    continue
            except:
                print("I can`t hear you :<\n")
                text = None
                timp -= 1
                print(timp)
                continue
VoiceCommand()
