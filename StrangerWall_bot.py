#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   StrangerWall_bot
#   by @fedex6
#
#   AUN NO ESTA PROBADO
#
########################

## Imports
import time
import datetime
import telepot
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

## Bot data
token       =   '-- TOKEN --'
chat_owner  =   '-- # of chat owner --'
name_owner  =   '-- name without @ of owner --'

def handle(msg):
    chat_id = msg['chat']['id']                 ## Numero de Chat de quien recibe el mensaje
    mensaje = msg['text']                       ## Mensaje recibido
    frase = mensaje.upper()                     ## Pasa todo a MAYUSCULA
    letra = list(frase)                         ## Crea un array con las letras del mensaje
    if msg['from']['username'] == '':           ## Usuario que lo envia
        usuario = msg['from']['first_name']
    else:
        usuario = '@' + msg['from']['username']

    for l in range(0, len(frase)):
        x = letra[l]

        if x != ' ' and x != '.' and x != '!' and x != '?':
            letras = {
                'A': 1, 
                'B': 2, 
                'C': 3, 
                'D': 4, 
                'E': 5, 
                'F': 6, 
                'G': 7, 
                'H': 8, 
                'I': 9, 
                'J': 10,
                'K': 11, 
                'L': 12,
                'M': 13, 
                'N': 14, 
                'O': 15, 
                'P': 16, 
                'Q': 17, 
                'R': 18, 
                'S': 19, 
                'T': 20, 
                'U': 21, 
                'V': 22, 
                'W': 23, 
                'X': 24,
                'Y': 25, 
                'Z': 26
            }

            result = letras.get(x, ' ')         ## Toma el valor de la letra

            GPIO.setup(result, GPIO.OUT)        ## Usa el valor del GPIO que debe encender, definirlos arriba
            GPIO.output(result, True)           ## Enciende el Led
            time.sleep(1.5)                     ## 1.5s deja encendido el Led
            GPIO.output(result, False)          ## Apaga el Led
            time.sleep(0.1)                     ## Espera por la proxima letra

        else :
            time.sleep(1.5)                     ## Los espacios hace que espere 1.5 seg
    
    if frase != '':
        bot.sendMessage(chat_id, 'Will ya paso tu mensaje...')                  # Avisa que se mando correctamente
        bot.sendMessage(chat_owner, usuario + ': ' + frase)   # Le manda el mensaje y quien lo mando al dueño del bot


bot = telepot.Bot(token)                        ## Poner el Token arriba, en la variable
bot.message_loop(handle)

while 1:
    try:
        time.sleep(5)

    except KeyboardInterrupt:
        GPIO.cleanup()                          ## Limpieza
        exit()
