#crash file
import os
import sys
import time
import datetime




if os.path.exists('crash.txt'):
    with open('crash.txt', 'r') as f:
        print(f.read())
        
else:
    print("No crash file found")
    def FileNotFound():
        print("File not found")
        time.sleep(1)
        print("crash registered at code 1")
