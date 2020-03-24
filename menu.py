import os
import time

os.system("tput setaf 1")
print("\t\tWelcome to TUI menu of Automation")
os.system("tput setaf 7")
print("\t\t---------------------------------")

def menu():
    print("""
        Press 1: to see date
        Press 2: to check cal
        Press 3: to check ip etc
        Press 4: to create user
        Press 5: conf web server
        Press 6: to exit
        """)
    
dic_local = {1:"date",2:"cal",3:"ifconfig",5:"yum install httpd"} # dictionary for local commands 
dic_remote = {1:"ssh {} date",2:"ssh {} cal",3:"ssh {} ifconfig",5:"ssh {} yum install httpd"} # dictionary for remote commands

location = input("Where to run script (local/remote): ")

if location == "local":

    menu()
    
    ch = int(input("Enter your choice : "))

    if ch==4:
        username = input("Input username: ")
        os.system("useradd {}".format(username)) # didn't change this cuz it's different from the others

    elif ch==6:
        exit() # cuz it's not a string but it's a function

    else:
        os.system(dic_local[ch]) # uses dic_local for reducing the redundant if statements 
        
elif location == "remote":
    
    IP = input("Input remote IP: ")

    menu()
    ch = int(input("Enter your choice : "))

    if ch==4:
        username = input("Input username: ")
        os.system("ssh {} useradd {}".format(IP,username)) # didn't change this cuz it's different from the others
    elif ch==6:
        exit()# cuz it's not a string but it's a function
    else:
        os.system(dic_remote[ch].format(IP)) # same thing as local

else:
    print("Invalid choice")
    cont = input("Want to continue (yes/no): ")
    if cont == "yes":
        os.system("python3 /root/project/menu.py")
    else:
        print("Exitting.....")
        time.sleep(0.5)
        exit()
