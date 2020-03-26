import os


while True:
    os.system("tput setaf 1")
    print("\t\tWelcome to TUI menu of Automation")
    os.system("tput setaf 7")
    print("\t\t---------------------------------")

    def menu(): # main menu where tasks are written
      print("""
          Press 1: to see date
          Press 2: to check cal
          Press 3: to check ip etc
          Press 4: to create user
          Press 5: conf web server
          Press 6: to exit
          """)
    

    location = input("Where to run script (local/remote/exit): ")

    if location == "local":

        menu()
        ch = int(input("Enter your choice : "))

        if (ch) == 1:
            os.system("date")
        elif (ch) == 2:
            os.system("cal")
        elif (ch) == 3:
            os.system("ifconfig")
        elif (ch) == 4:
            username = input("Input username: ")
            os.system("useradd {}".format(username))
        elif (ch) == 5:
            os.system("yum install httpd")
        elif (ch) == 6:
            exit()
        else: 
            print("Invalid Choice")
            menu()
  

    elif location == "remote":
    
        IP = input("Input remote IP: ")
        # checkip(IP)

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
        elif ch==6:
            exit()
        else:
            print("Invalid choice")
            menu()
  
    elif location == "exit":
        exit()

    else:
        print("Invalid choice")


    cont = input("Press Y/y to continue...")
    if cont == "y" or cont == "Y":
        os.system("clear")
        continue
    else:
        exit()




'''def checkip(ip):
    print("checking ip/hostname: ")
    temp = ''
    os.system("ping {}".format(ip)).append(temp)
    print(temp)
    if temp == True:
       print("IP/hostname is good to go")
    else:
        print("wrong IP/hostname")
     '''
