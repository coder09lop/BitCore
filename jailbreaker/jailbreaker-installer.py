import os
import random


def JailBreaker():
    print("Welcome to the jailbreaker mod!")
    print("NOTE. the jailbreaker mod is a mod 100% legal for linux this is created from us don't use it for illegal things")
    print("what you want to do?")
    print("1. jailbreak version in BITCORE")
    print("2. jailbreak linux os")
    print("3. jailbreak windows os")
    print("4. jailbreak MACOS(not working)")
    print("5. exit")
    print("1-5")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("BITCORE jailbreaker")
        os.system("sudo apt update")
        os.system("sudo apt install qemu")
        os.system("sudo apt install binfmt-support")
        os.system("sudo apt install libglib2.0-dev")
        os.system("sudo apt install libglib2.0-dev")
    elif choice == "2":
        os.system("sudo apt update")
        os.system("sudo apt install qemu")
        os.system("sudo apt install binfmt-support")
        os.system("sudo apt install libglib2.0-dev")
    elif choice == "3":
        os.system("sudo apt update")
        os.system("sudo apt install qemu")
        os.system("sudo apt install binfmt-support")
        os.system("sudo apt install libglib2.0-dev")
    elif choice == "4":
        print("MACOS jailbreaker")
    elif choice == "5":
        print("Exiting...")
    else:
        print("not a valid option")
    #finisch