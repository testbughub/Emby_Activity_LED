# Emby activity LED indicator

## Description
A simple script for Raspberry Pi to light an LED if any user
is currently using the service.

## Raspberry Pi setup
The script uses GPIO pin 17 for the LED. It can be changed if needed.
Make sure to use a resistor between the Pi and the LED, or you might damage your Pi.

## Running
First, you need to create a API key.
Go to the server dashboard > API Keys and create a new key.

Paste your API key next to API_KEY, the server IP next to SERVER_IP and the port emby uses next to PORT,
then run it with python.
Once an activity is detected, the LED will light up.

## Dependencies
RPi.GPIO (pip install RPi.GPIO)
