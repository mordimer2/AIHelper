import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['DEFAULT']['api_key']