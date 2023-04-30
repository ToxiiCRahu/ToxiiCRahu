import os

byellow="\033[1;33m"      # Yellow

while True:
    os.system("clear")
    print(byellow+"[1]Custom sms Seever 1\n[2]Custom sms Server 2\n[3]Sms Bombing3")
    opt=str(input("[®] Enter Your Option:- "))
    if opt=="1":
         os.system("python3 cmdsms.py")
    elif opt=="2":
        os.system("python3 cmdotpsms.py")
    if opt=="3":
         os.system("python3 bombinpin.py")