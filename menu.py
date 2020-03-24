import os

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
    

location = input("Where to run script (local/remote): ")

if location == "local":

    menu()
    ch = int(input("Enter your choice : "))

    if ch==1:
        os.system("date")
    elif ch==2:
        os.system("cal")
    elif ch==3:
        os.system("ifconfig")
    elif ch==4:
        username = input("Input username: ")
        os.system("useradd {}".format(username))
    elif ch==5:
        os.system("yum install httpd")
    else:
        exit()

elif location == "remote":
    
    IP = input("Input remote IP: ")

    menu()
    ch = int(input("Enter your choice : "))

    if ch==1:
        os.system("ssh {} date".format(IP))
    elif ch==2:
        os.system("ssh {} cal".format(IP))
    elif ch==3:
        os.system("ssh {} ifconfig".format(IP))
    elif ch==4:
        username = input("Input username: ")
        os.system("ssh {} useradd {}".format(IP,username))
    elif ch==5:
        os.system("ssh {} yum install httpd".format(IP))
    else:
        exit()

else:
    print("Invalid choice")
    cont = input("Want to continue (yes/no): ")
    if cont == "yes":
        os.system("python3 /root/project/menu.py")
    else:
        print("Exitting.....")
        exit()
