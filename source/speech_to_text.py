import speech_recognition as sr

class SpeechRecognition():
    """ 
    Wrap speech recognition in a single class. Get the recognize_google response and send it to a chatGPT
    """
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)

    def callback(self, audio):
        try: 
            out = self.r.recognize_google(audio)
            return out
        except sr.UnknownValueError: 
            print("Jeszcze raz, nie dosłyszałem.")
        except TimeoutError:
            print("Wiadomość za długa na darmowe API, jeszcze raz")

    def listen(self, phrase_time_limit):
        with self.mic as s:
            audio =""
            while not audio:
                try:  # listen for 1 second, then check again if the stop function has been called
                    print("Słucham")
                    audio = self.r.listen(s, 1, phrase_time_limit)
                except sr.WaitTimeoutError:  # listening timed out, just try again
                    pass

            return self.callback( audio)
    
# srr = SpeechRecognition()
# srr.listen(10)
