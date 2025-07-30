# One of my biggest problems at work is when someone is doing a homeoffice day, we can´t be sure that what we´re printing correctly.
# So my solution whas very simple. I made a directory when I put all my .pdfs
# Later I discovered that I lost a lot of time printing files one by one. Then I made this script, when I run it we gain more time and have less troubles or problems with printers


import os
import shutil
import time
import subprocess

CARPETA = r"C:\Users\tarmoa\Desktop\Impresion"
DESTINO = os.path.join(os.path.dirname(CARPETA), "procesados")
os.makedirs(DESTINO, exist_ok=True)

ADOBE = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"

for archivo in os.listdir(CARPETA):
    if archivo.lower().endswith(".pdf"):
        origen = os.path.join(CARPETA, archivo)
        destino = os.path.join(DESTINO, archivo)

        print(f"Imprimiendo {archivo}…")
        try:
            subprocess.run([ADOBE, "/t", origen], check=True)
        except Exception as e:
            print(f"  ¡Se abre el reader!: {e}")
            print("  chequea la ruta!")
            continue

        time.sleep(1)  
        print(f"Moviendo {archivo} a 'procesados'…")
        shutil.move(origen, destino)

# Disclaimer!
#I was having trouble with Adobe, so I used GPT to automate the printing process (I didn't know the Adobe commands). 
#In the future, I plan to switch to a different PDF reader, since Adobe runs a bit slowly on my older work computer. It's useful, but unfortunately quite heavy for my current setup.

# This is one of my first contributions at work. I´m so proud of this, because is a little script that help us to have less fails in general at work. 
