#!/usr/bin/python3
import pyperclip as pc
import subprocess

import time

recent_value = ""
while (True):

    while True:
        tmp_value = pc.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            print("Value changed: %s" % str(recent_value)[:20])
            break
        time.sleep(0.1)
    #Obtenemos datos del portapapeles
    datos = pc.paste()
    cadena="./traducir.sh '"+datos.strip()+"'"
    print(cadena)
    traduccion = subprocess.check_output(cadena, shell=True).decode('utf-8')

    print(traduccion)
    pc.copy(traduccion)