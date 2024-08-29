import os
import random
import subprocess
#inizia
def JailBreaker():
    print("Welcome to the jailbreaker mod!")
    print("NOTE. the jailbreaker mod is a mod 100% legal for linux this is created from us don't use it for illegal things")
    print("what to jailbreak?")
    print("1. the bitcore")
    print("2. exit")
    print("1-2")
    jailbreak = input("choose a number: ")
    if jailbreak == "1":
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "visual-studio-code"])
        subprocess.run(["sudo", "apt", "install", "git"])
        subprocess.run(["sudo", "apt", "install", "python3"])
        subprocess.run(["sudo", "apt", "install", "python3-pip"])
        subprocess.run(["sudo", "pip3", "install", "pyautogui"])
        #jdk
        subprocess.run(["sudo", "apt", "install", "default-jdk"])
        #node
        subprocess.run(["sudo", "apt", "install", "nodejs"])
        #npm
        subprocess.run(["sudo", "apt", "install", "npm"])
        #java
        subprocess.run(["sudo", "apt", "install", "openjdk-8-jdk"])
    elif jailbreak == "2":
        print("goodbye!")
    else:
        print("invalid choice!")
