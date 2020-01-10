import requests
import RPi.GPIO as GPIO
from time import sleep

pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin,GPIO.OUT)

API_KEY = ''
SERVER_IP = ''
PORT = ''

URL = 'http://' + SERVER_IP + ':' + PORT + '/emby/sessions?api_key=' + API_KEY

while True:
  sleep(10)
  data = requests.get(URL).json()
  active_users = 0
  for session in data:
    if 'NowPlayingItem' in session:
      active_users += 1

  if active_users >= 2:
    GPIO.output(pin,GPIO.HIGH)
  else:
    GPIO.output(pin,GPIO.LOW)
