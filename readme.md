# Telescope v1.0

#### Author: Andres Moraldo
#### Country: Argentina
#### Date: March 24th 2022

This proyect is a sequence to move goto mount AllView - mount with SynScan from skywatcher throught the serial port. <br>
The telescope used is a Skywatcher Skymax 102/1300.<br>
The main objective of this project was to photograph the ISS station.<br>
It was writed in python.<br>

Multiples instructions are allowed such us:

  send A: send command raw without response.<br>
  pause: pause sequence. Use ENTER to continue.<br>
  wait x:  wait x seg before continues (use "." to decimals)<br>
  send_until A: send command goto and wait the same telescope position. The timeout is 20 seg<br>
  read A: send the command get and print the return value<br>	

## Clone GIT repository

git clone https://github.com/amoraldo/Telescope.git
 
## Install packages

pip install -r requirements.txt

  
## Files

readme.md<br>
requiremets.txt<br>
sequence.seq<br>
setting.ini<br>
telescope.py<br>


## Sequences

Use sequence.seq file to make a new sequence.<br>
If you want change the name of the sequence file, use the setting in the setting.ini file<br>


## Setting

Use setting.ini file to set the serial port configuration like

//  Configuracion del puerto de comunicacion <br>
  serial: COM1<br>
  serial: /dev/ttyUSB0<br>
  baudrate: 9600<br>
  timeout: 1<br>

Also, this file contain the name of sequence file. Change it if you make diferents sequence files<br>

Note that "//" is programming comments. Use this to take notes
