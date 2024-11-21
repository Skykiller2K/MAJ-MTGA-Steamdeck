#!/usr/bin/python3
from pathlib import Path
import shutil
import os
import time
dossier_mtga_night = Path("/home/deck/Games/MTGA")
dossier_mtga_source = Path("/home/deck/.local/share/Steam/steamapps/common/MTGA")
if os.path.exists(dossier_mtga_night):
    shutil.rmtree(dossier_mtga_night)
while True:
    if os.path.exists(dossier_mtga_night):
        time.sleep(1)
        continue
    else:
        if os.path.exists(dossier_mtga_source):
            shutil.copytree(dossier_mtga_source, dossier_mtga_night)
            break
        else:
            break 
while True : 
    if os.path.getsize(dossier_mtga_night) == os.path.getsize(dossier_mtga_source):
        print ("Mise à jour effectuée")
        break
    else :
        pourcentage = (os.path.getsize(dossier_mtga_night)/os.path.getsize(dossier_mtga_source))*100
        print ("%s %" %(pourcentage))
        time.sleep(1)
        continue