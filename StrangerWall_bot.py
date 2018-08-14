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
    chat_id = msg['chat']['id']             ## Numero de Chat de quien recibe el mensaje
    usuario = msg['from']['username']       ## Usuario que lo envia
    mensaje = msg['text']                   ## Mensaje recibido
    frase = mensaje.upper()                 ## Pasa todo a MAYUSCULA
    letra = list(frase)                     ## Crea un array con las letras del mensaje

    for l in range(0, len(frase)):
        x = letra[l]

        if x != ' ':
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

            result = letras.get(x, ' ')     ## Toma el valor de la letra

            ''' DESCOMENTAR LUEGO DE QUE ESTE MONTADO
            GPIO.setup(result, GPIO.OUT)    ## Usa el valor del GPIO que debe encender, definirlos arriba
            GPIO.output(result, True)       ## Enciende el Led
            time.sleep(1.5)                 ## 1.5s deja encendido el Led
            GPIO.output(result, False)      ## Apaga el Led
            time.sleep(0.3)                 ## Espera por la proxima letra
            GPIO.cleanup()                  ## Limpieza
            '''

            bot.sendMessage(chat_id, result)## Envia el Led que se encendio
            time.sleep(1.8)
        else :
            time.sleep(2.5)                   ## Los espacios hace que espere 3 seg
            bot.sendMessage(chat_id, '...')   ## Envia un mensaje vacio


bot = telepot.Bot(token)                    ## Poner el Token arriba, en la variable
bot.message_loop(handle)

while 1:
    try:
        time.sleep(5)

    except KeyboardInterrupt:
        exit()