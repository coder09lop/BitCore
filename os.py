import os
import subprocess
import sys

#start code
def OSI():
    print("welcome to the os installer! select the os version you want to install")
    print("1. windows 10")
    print("2. ubuntu 20.04")
    print("3. windows 11")
    print("4. Macos Sonoma")
    print("5. Exit")
    print("1-5")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("installing windows 10")
        subprocess.run('sudo', 'apt', 'update')
        os.system("whoami")
        os.system("sudo apt-get install -y windows10-iso")
        os.system("sudo reboot now")
    elif choice == "2":
        print("installing ubuntu 20.04")
        subprocess.run('sudo', 'apt', 'update')
        os.system("whoami")
        os.system("sudo apt-get install -y ubuntu20.04-iso")
        os.system("sudo reboot now")
    elif choice == "3":
        print("installing win11")
        subprocess.run('sudo', 'apt', 'update')
        os.system("whoami")
        os.system("sudo apt-get install -y windows11-iso")
        os.system("sudo reboot now")
    elif choice == "4":
        print("installing macos sonoma")
        subprocess.run('sudo', 'apt', 'update')
        os.system("whoami")
        os.system("sudo apt-get install -y macos-sonoma-iso")
        os.system("sudo reboot now")
    elif choice == "5":
        print("Exiting the os installer")
    else:
        print("Invalid choice. Please choose a valid option.")
        