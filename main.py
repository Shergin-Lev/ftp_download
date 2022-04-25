import os
from config_parser import Config

config = Config()

HOST = config['host']
SECRET = config['magic_word']
PORT = int(config['port'])

