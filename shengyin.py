from aip import AipSpeech
import pygame
import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

BtnPin = 19
Gpin = 5
Rpin = 6

APP_ID='16226519'
API_KEY='5KVxQVES4LSja0u2G4y8m1O9'
SECRET_KEY='KhaXYwGLSmQYgnwHkuXKpV9MO2ta0bQ8'


aipSpeech=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def robot_speech(content):
    result = aipSpeech.synthesis(text=content,options={'spd':2,'vol':5,'per':0})
    if not isinstance(result,dict):
        with open('voice.mp3','wb')as f:
            f.write(result)
    else:print(result)

    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/CLBROBOT/voice.mp3')
    pygame.mixer.music.play()
    
