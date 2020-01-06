import requests
import RPi.GPIO as GPIO
from time import sleep

pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)

API_KEY = ''
SERVER_IP = ''
PORT = ''

URL = 'http://' + SERVER_IP + ':' + PORT + '/emby/sessions?api_key=' + API_KEY

while True:
  r = requests.get(URL)
  r.status_code
  sleep(10)
  if 'NowPlayingItem' in r.content:
    print('Activity = 1')
    GPIO.output(pin,GPIO.HIGH)
  else:
    print('Activity = 0')
    GPIO.output(pin,GPIO.LOW)
