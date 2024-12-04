#!/usr/bin/python3
from pathlib import Path
import shutil
import os
import time
import threading

dossier_mtga_night = Path("/home/deck/Games/MTGA")
dossier_mtga_source = Path("/home/deck/.local/share/Steam/steamapps/common/MTGA")

taille_dossier_source = 0
for path, dirs, files in os.walk(dossier_mtga_source):
    for f in files:
        fp = os.path.join(path, f)
        taille_dossier_source += os.path.getsize(fp)

if os.path.exists(dossier_mtga_night):
    shutil.rmtree(dossier_mtga_night)

def copie_dossier():
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

def affichage_progression_copie():
    time.sleep(1)
    pourcentage2 = 0
    while True : 
        taille_dossier_destination = 0
        for path, dirs, files in os.walk(dossier_mtga_night):
            for f in files:
                fp = os.path.join(path, f)
                taille_dossier_destination += os.path.getsize(fp)

        if taille_dossier_destination == taille_dossier_source:
            print ("\nMise à jour terminée")
            break
        else :
            pourcentage = int((taille_dossier_destination / taille_dossier_source)*100)
            if pourcentage2 == pourcentage : 
                time.sleep(0.5)
            else:
                pourcentage2 = pourcentage
                print (f"Mise à jour : {pourcentage} %")
                time.sleep(0.5)
                continue

th1 = threading.Thread(target=copie_dossier)
th2 = threading.Thread(target=affichage_progression_copie)

th1.start()
th2.start()

th1.join()
th2.join()