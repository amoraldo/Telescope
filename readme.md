# Telescope

This proyect is a sequence to move goto mount AllView-mount of SynScan from skywatcher throught the serial port.
The telescope used is a Skywatcher Skymax 102/1300
The main objective of this project was to photograph the ISS station

Multiples instructions are allowed such us:

//    send A: envia el comando A por puerto
//    pause: ejecuta una pausa hasta que se presiona enter
//    wait x:  espera x segundos (utiliza . para decimales)
//    send_until A: lee telescopio leyendo el comando get en el telescopio
//    read A: envia comando get y devuelve valor
 

Install packages

pip install -r requirements.txt

 
Sequences

Use sequence.seq file to make a new sequence.
If you want change the name of the sequence file, use the setting in the setting.ini file

Setting

Use setting.ini file to set the serial port configuration like

// Configuracion del puerto de comunicacion 
// serial: COM1 // windows
// serial: /dev/ttyUSB0 // linux
// baudrate: 9600
// timeout: 1

Also, this file contain the name of sequence file. Change it if you make diferents sequence files

Note that "//" is programming comments. Use this to take notes
