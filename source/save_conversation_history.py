import datetime 

class ConversationHistory():

    def __init__(self, fileNm) -> None:
        self.fileNm = fileNm

    def append_to_file(self, question, answer):
        now = datetime.datetime.now()
        with open(self.fileNm, 'a') as file:
            file.write("[{} Question]\n".format(now.strftime("%Y-%m-%d %H:%M:%S")))
            file.write(question + '\n\n')
            file.write("[Answer]")
            file.write(answer + '\n\n')

