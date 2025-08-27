# automatic_print.py
#
# Changelog
# =========
# v2.0 (2025-08-27)
# - Reduced number of lines
# - Uses fewer processes
# - Cleaner and easier to maintain
#
# v1.0 (2025-08-20)
# - Initial version: print PDFs with Adobe and move them to 'procesados'




import os
import shutil
import time
import subprocess

CARPETA = r"C:\Users\tarmoa\Desktop\Impresion"
ADOBE = r"C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"

for archivo in os.listdir(CARPETA):
    if archivo.lower().endswith(".pdf"):
        print(f"Imprimiendo {archivo}…")
        try:
            subprocess.run([ADOBE, "/t", origen], check=True)
        except Exception as e:
            continue

        time.sleep(1)  
