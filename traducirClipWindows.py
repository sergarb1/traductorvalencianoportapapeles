#!/usr/bin/python3

'''
Documentación biblioteca
pip3 install pyperclip
https://pyperclip.readthedocs.io/en/latest/
Si da "Not implemented Error"
sudo apt-get install curl #to install curl
sudo apt-get install xsel #to install the xsel utility.
sudo apt-get install xclip #to install the xclip utility.
pip install gtk #to install the gtk Python module.
pip install PyQt4 #to install the PyQt4 Python modu

'''


import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
import sys
from platform import platform
import pyperclip as pc
import subprocess

import time
while True:
    tmp_value= pc.waitForNewPaste()
    time.sleep(0.1)
    #Obtenemos datos del portapapeles
    datos = pc.paste().strip()
    datos = strip_accents(datos)
    cadena="curl -F \"MAX_FILE_SIZE1=10000000\" -F \"ua_memories=true\" -F \"terminology_file=0\" -F \"cuadrotexto="+datos+"\" -F \"marcar=0\" -F \"direccion=spa-cat_valencia_uni\" https://apertium.ua.es/tradtexto.php"
    print(cadena)
    traduccion = subprocess.check_output(cadena, shell=True).decode(sys.stdout.encoding)

    print(traduccion)
    pc.copy(traduccion)
