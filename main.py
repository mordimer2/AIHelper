import configparser
import source.GPT3Client as GPT3
import source.speech_to_text as stt
from source.text_to_speech import TextToSpeech
from source.save_conversation_history import ConversationHistory

config = configparser.ConfigParser()
config.read('config.ini')
logger = ConversationHistory('tmp_logging.txt')

api_key = config['DEFAULT']['api_key']

speech_recon = stt.SpeechRecognition()
task_todo = speech_recon.listen(17)

print(task_todo)
if str(task_todo) != "I can't understand you." and str(task_todo) != None and str(task_todo) != "" and str(task_todo) != "[]":
    gpt3 = GPT3.GPT3Client(api_key)
    response = gpt3.get_response(str(task_todo))
    TextToSpeech().text_to_speech(response)
    logger.append_to_file(task_todo, response)