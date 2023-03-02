
import subprocess

def handle_start(message):
    # запускаем первый скрипт
    subprocess.run(['python', '/Users/baichorovboris/Desktop/imageStitching/blizko2.py'])
    # запускаем второй скрипт после того, как первый закончится
    subprocess.run(['python', '/Users//Users/baichorovboris/Desktop/imageStitching/imageStitchingYT.py'])


