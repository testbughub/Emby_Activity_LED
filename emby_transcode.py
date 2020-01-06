import requests
import RPi.GPIO as GPIO
from time import sleep

pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)

API_KEY = ''
SERVER_IP = ''
PORT = ''

URL = 'http://' + SERVER_IP + ':' + PORT + '/emby/sessions?api_key=' + API_KEY

while True:
  sleep(10)
  r = requests.get(URL)
  r.status_code
  if 'Transcode' in r.content:
    print('Transcoding = 1')
    GPIO.output(pin,GPIO.HIGH)
  else:
    print('Transcoding = 0')
    GPIO.output(pin,GPIO.LOW)
