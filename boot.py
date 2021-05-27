import os
import time
os.system("clear")
print("BIOS Revision KENT0")
time.sleep(0.5)
os.system("clear")
print("loading")
time.sleep(0.5)
os.system("clear")
print("GNU GRUB version k3n+0: ")
print("*KentOS")
print("   command prompt on dev/die-hard-keyboard-users")
choice = input("Enter first letter of your choice: ")
time.sleep(0.5)
os.system("clear")
print("Entering command line mode")
os.system("clear")
if choice == "c":
  while 1:
    cmd = input("")
    print(os.system(cmd))
elif choice == "k" or choice == "K":
    print("Welcome to KentOS!")
    
