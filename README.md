# Emby activity LED indicator

## Description
A simple script for Raspberry Pi to light an LED if any user
is currently using the service.

#### emby_activity.py
Lights up the LED if anyone is currently using the service.

#### emby_transcode.py
Lights up the LED if transcoding is in use.

#### emby_active_users.py
Lights up the LED if more than one is using the service.  
I'm planning on expanding this to use a 7-segment display to display how many users is using the service.

## Raspberry Pi GPIO setup
Activity LED = 17  
Transcode LED = 27  
Active Users = 22  
Make sure to use a resistor between the Pi and the LED(s), or you might damage your Pi.

## Running
First, you need to create a API key.  
Go to the server dashboard > API Keys and create a new key.

Paste your API key next to API_KEY, the server IP next to SERVER_IP and the port  
emby uses next to PORT, then run it with python.  
Once an activity is detected, the LED(s) will light up.

## Dependencies
RPi.GPIO (pip install RPi.GPIO)

## Autostart
I personally prefer using pm2, but a cronjob works just as well.
### pm2
```
npm install pm2 -g
pm2 start emby_activity.py
pm2 start emby_transcode.py
pm2 start emby_active_users.py
pm2 save
```
### cron
```
crontab -e
@reboot /path/to/script.py
```

## Special Thanks
K900_ @ reddit for helping me with the emby_active_users script.
