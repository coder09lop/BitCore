import os
import subprocess


#requirements
def Requiments():
    print("Requirements:")
    #python 3.6 or higher
    os.system("sudo apt install python3")
    os.system("sudo apt install python3-pip")
    #jdk
    os.system("sudo apt install default jdk")
    subprocess.run(["sudo", "apt", "install", "openjdk-8-jdk"])