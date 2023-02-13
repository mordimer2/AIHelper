import pyttsx3

class TextToSpeech():
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.say(text)
        engine.runAndWait()

    def get_all_available_voices(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            print("Voice:")
            print(" - ID: %s" % voice.id)
            print(" - Name: %s" % voice.name)
            print(" - Languages: %s" % voice.languages)
            print(" - Gender: %s" % voice.gender)
            print(" - Age: %s" % voice.age)



# TextToSpeech().text_to_speech("Hello, this is a text to speech conversion.")
