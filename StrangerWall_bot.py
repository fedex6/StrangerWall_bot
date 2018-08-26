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
from string import ascii_uppercase
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
    if msg['from']['username'] == '':           ## Usuario que lo envia
        usuario = msg['from']['first_name']
    else:
        usuario = '@' + msg['from']['username']

    for letra in frase:
        if letra not in [' ', '.', '!', '?']:
            result = ascii_uppercase.index(letra) + 1  ## Toma el valor de la letra

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
