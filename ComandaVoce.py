import speech_recognition as sr
import subprocess
import pyttsx3 as p
import os
def VoiceCommand():
    r = sr.Recognizer()
    engine = p.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    with sr.Microphone() as source:
        print("Recording...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            if "system call" in text:
                print("System Call:")
                if "open" in text:
                    text = text.replace("system call open", "")
                    print (text)
                    engine.say("Open," + str(text))
                    engine.runAndWait()
                    text = text.replace(" ", "", 1) + str(".lnk")
                    text_first_letter = text[0]
                    text_upper_letter = text[0].upper()
                    text = text.replace(text_first_letter, text_upper_letter, 1)
                    print (text)
                    for r,d,f in os.walk("C:\\", "D:\\"):
                        for files in f:
                            if files == text:
                                x = os.path.join(r,files)
                                os.startfile(x)

            else:
                print("Sorry, you didn't call the system :<")
        except:
            print("I can`t hear you :<")