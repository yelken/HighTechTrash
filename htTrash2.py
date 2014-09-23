import RPi.GPIO as GPIO
import time
import random
import pygame
from TKinter import *

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

pontuacao_geral = 0
distancia_anterior = 25.6

try:

	while True:
		GPIO.output(GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(GPIO_TRIGGER, False)
		start = time.time()

		while GPIO.input(GPIO_ECHO)==0:
			start = time.time()

		while GPIO.input(GPIO_ECHO)==1:
			stop = time.time()			

		elapsed = stop-start
		distance = elapsed * 34300

		distance = distance / 2

		if distance < 25 and distancia_anterior >=25.5:
			print "Lixo detectado!"
			pygame.mixer.init()
			pygame.mixer.music.load(str(random.randrange(1,19))+".wav")	
			pygame.mixer.music.play()
			time.sleep(3)
			pontuacao_geral = pontuacao_geral + random.randrange(1,1000+1)
			print "Pontos gerais: " + str(pontuacao_geral)

		distancia_anterior = distance

		time.sleep(0.3)

except KeyboardInterrupt:
	print " Sair "
	GPIO.cleanup()











