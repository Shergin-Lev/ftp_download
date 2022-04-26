import os
import paramiko
from config_parser import Config
from ui import Window
from threading import Thread
from time import sleep


window = Window('Start')
window.update()
config = Config()


def create_local_folder():
    pass


def copy_file():
    while True:
        if not window.STATUS:
            break
        sleep(config.refresh_rate_seconds)
        text = 'Copy files...'
        print(text)
        window.set_text(text)


def show_window():
    while True:
        if window.STATUS:
            window.update()
        else:
            break


thread_copy = Thread(target=copy_file)
thread_copy.start()
show_window()
thread_copy.join()

