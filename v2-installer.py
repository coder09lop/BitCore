import os






print("salve selezionare tipo di sistema")
print("1. Linux")
print("2. Windows")
print("3. macos")
print("4. exit")
print("selezionare 1-4")
tipo_sistema = input("inserisci il numero del sistema: ")
if tipo_sistema == "1":
    print("continuare con l'installazione?")
    installazione = input("inserisci s per continuare o n per annullare:")
    if installazione == "s":
        print("installazione avviata")
        os.system("sudo apt-get wine64")
        for numero in range (1000):
            print(numero)
        print("installazione completata")
    elif installazione == "n":
        print("installazione annullata")
    else:
        print("errore")
#elif2    
elif tipo_sistema == "2":
    print("continuare con l'installazione?")
    installazione = input("inserisci s per continuare o n per annullare:")
    if installazione == "s":
        os.system("sudo apt-get wine64")
        for numero in range (1000):
            print(numero)
        print("installazione completata")
    elif installazione == "n":
        print("installazione annullata")
    else:
        print("errore")
elif tipo_sistema == "3":
    print("continuare con l'installazione?")
    installazione = input("s/n:")
    if installazione == "s":
        os.system("sudo apt-get wine64")
        for numero in range (1000):
            print(numero)
        print("installzione completata")
elif tipo_sistema == "4":
    print("ciao")
else:
    print("errore")