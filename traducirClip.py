#!/usr/bin/python3

'''
Documentación biblioteca
pip3 install pyperclip
https://pyperclip.readthedocs.io/en/latest/
Si da "Not implemented Error"

sudo apt-get install xsel #to install the xsel utility.
sudo apt-get install xclip #to install the xclip utility.
pip install gtk #to install the gtk Python module.
pip install PyQt4 #to install the PyQt4 Python modu

'''

import pyperclip as pc
import subprocess

import time
while True:
    tmp_value= pc.waitForNewPaste()
    time.sleep(0.1)
    #Obtenemos datos del portapapeles
    datos = pc.paste()
    cadena="./traducir.sh '"+datos.strip()+"'"
    print(cadena)
    traduccion = subprocess.check_output(cadena, shell=True).decode('utf-8')

    print(traduccion)
    pc.copy(traduccion)