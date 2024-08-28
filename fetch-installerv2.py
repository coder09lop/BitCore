import os
import pip
import subprocess
import sys
import time




def FetchInstaller():
    print("benvenuto nell installer v2")
    print("questo installer e' stato creato da: https://github.com/Coder09lop")
    print("nell installer installerai il BootLoader")
    print("per favore, assicurati di avere installato python e pip")
    print("se non hai installato python e pip, puoi farlo seguendo questi passi")
    #passaggi
    print("1. vai su https://www.python.org/downloads/")
    print("2. clicca su download")
    print("3. seleziona la versione di python che desideri installare")
    print("4. clicca su download")
    print("5. segui le istruzioni per installare python")
    print("6. vai su https://pip.pypa.io/en/stable/installation/")
    print("7. clicca su download")
    print("8. seleziona la versione di pip che desideri installare")
    print("9. clicca su download")
    print("10. segui le istruzioni per installare pip")
    print("11. torna a questo script e premi enter per continuare")
    #installazione
    print("installazione in corso...")
    print("installazione del BootLoader...")
    os.system("sudo apt-get qemu tools-y")
    os.system("sudo apt-get install grub-pc grub-pc-bin grub-efi grub")
    os.system("sudo grub-install --target=x86_64-efi --efi-directory")
    os.system("sudo grub-mkconfig -o /boot/grub/grub.cfg")
    print("installazione completata!")
    print("il BootLoader e' stato installato con successo!")
    print("per favore, riavvia il tuo computer per applicare le modifiche")
    os.system("sudo reboot now")
    print("installazione completata!")
    print("il BootLoader e' stato installato con successo!")
    print("per favore, riavvia il tuo computer per applicare le modifiche")