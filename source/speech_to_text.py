import speech_recognition as sr
import time 

r = sr.Recognizer()
r.operation_timeout = 1.8
mic = sr.Microphone()


with mic as source:
    r.adjust_for_ambient_noise(source)

out=""
def callback(r, audio):
    try: 
        # with sr.Microphone() as source:
            # print("Słucham")
            # r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            # print("analizuję")
        out = r.recognize_google(audio)
        print(out)
    except sr.UnknownValueError: 
        print("Jeszcze raz, nie dosłyszałem.")
 
stop_listening = r.listen_in_background(mic, callback, phrase_time_limit=3)

time.sleep(100)