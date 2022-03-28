# Telescope v1.0

#### Author: Andres Moraldo
#### Country: Argentina
#### Date: March 24th 2022

This proyect is a sequence to move goto mount AllView - mount with SynScan from skywatcher throught the serial port.

The telescope used is a Skywatcher Skymax 102/1300.

The main objective of this project was to photograph the ISS station.

It was writed in python.

Multiples instructions are allowed such us:

  send A: send command raw without response.

  pause: pause sequence. Use ENTER to continue.

  wait x:  wait x seg before continues (use "." to decimals)

  send_until A: send command goto and wait the same telescope position. The timeout is 20 seg

  read A: send the command get and print the return value

## Clone GIT repository

git clone https://github.com/amoraldo/Telescope.git
 
## Install packages

pip install -r requirements.txt

  
## Files

readme.md
requiremets.txt
sequence.seq
setting.ini
telescope.py


## Sequences

Use sequence.seq file to make a new sequence.
If you want change the name of the sequence file, use the setting in the setting.ini file


## Setting

Use setting.ini file to set the serial port configuration like

  Configuracion del puerto de comunicacion 
  serial: COM1
  serial: /dev/ttyUSB0
  baudrate: 9600
  timeout: 1

Also, this file contain the name of sequence file. Change it if you make diferents sequence files

Note that "//" is programming comments. Use this to take notes
