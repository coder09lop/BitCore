import os
import subprocess
import sys

#inizio
def main():
    #main
    print("Inizio")
    #creo il file
    with open("file.txt", "w") as file:
        file.write("Test passed!")
        #apro il file
        with open("file.txt", "r") as file:
            #leggo il file
            print(file.read())
            #chiudo il file
            file.close()
    print("1/3")
    os.system("whoami")
    print("2/3")
    #apro il file
    with open("image-loader.sh", "r") as file:
        #leggo il file
        print(file.read())
        file.close()
    print("3/3")
    #fin
    
#chiudo il file