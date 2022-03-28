__version = 1.0

import serial
import csv
import os, sys
import time

print()
print ('Ing. Andres Moraldo. 24 Marzo 2022')
print ('Telescope Ver. ' + str(__version))
print()

# Abro configuraciones: setting.ini
f_setting = open(os.path.join("setting.ini"), 'r')
reader = csv.reader(f_setting)
comando={}
for index, row in enumerate(reader):
  if row != []:
    if row[0][:len("//")] == "//": continue
    comando[row[0].split(":")[0].replace(" ","")] = row[0].split(":")[1].replace(" ","")
print("Settings: ", comando)
f_setting.close()

# Abro Secuencia: sequence.seq
f_sequence = open(os.path.join(comando["sequence"]), 'r')
#reader = csv.reader(f_sequence)
reader = f_sequence.read().splitlines()
secuencia={}
for row in reader:
  if row != "":
    if row[:len("//")] == "//": continue
    if row[:len("[")] == "[":
      function = row.replace(" ", "")[1:-1]
      secuencia[function] = []
      continue
    secuencia[function].append(row)
print("Secuencia: ", secuencia)
f_sequence.close()

print()
# Abro puerto serial
ser = serial.Serial(comando["serial"], int(comando["baudrate"]), timeout = int(comando["timeout"]))
#print(ser)
if (ser.is_open ==False): 
  print("no se pudo abrir puerto:")
  exit()
# Ejecuto secuencia Main
if not ("Main" in secuencia): print ("No existe funcion Main en la secuencia")
for linea in secuencia["Main"]:
  if linea[:len('pause')] == 'pause':
    input("Presione Enter para continuar...")
    continue
  if linea[:len('wait')] == 'wait':
    tiempo = linea.replace(" ", "").replace("wait","")
    print("Esperando " + str(tiempo) + " seg")
    time.sleep(float(tiempo))
    continue
  if linea[:len('send_until')] == 'send_until':
    print(linea)
    cmd_telescope = linea.replace(" ","").replace("send_until","")
    ser.write(cmd_telescope.encode(encoding = 'UTF-8'))
    for i in range(20):
      ser.write(cmd_telescope[0].replace("R","E").replace("r","r").replace("B","Z").replace("b","z").encode(encoding = 'UTF-8'))
      lectura = ser.readline()
      print("  lectura: ", lectura)
      if(lectura[:-2]==cmd_telescope[1:-1].encode(encoding = 'UTF-8')):break
    continue
  if linea[:len('send')] == 'send':
    print(linea)
    ser.write(linea.replace(" ","").replace("send","").encode(encoding = 'UTF-8'))
    continue
  if linea[:len('read')] == 'read':
    print(linea)
    ser.write(linea.replace(" ","").replace("read","").encode(encoding = 'UTF-8'))
    lectura = ser.readline()
    print("  lectura: ", lectura)


    continue
  print("no reconozco el comando, lo ignoro y continuo")
ser.close() 
print ("Fin de la secuencia")
