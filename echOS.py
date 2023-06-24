import os
import time
import requests

#Variables
location = os.getcwd()
link="https://raw.githubusercontent.com/T0F1Q2007/echOS/main/echOS.py"

def help():
    print("""
    exit - stop the system
    newpk _directory_ - make a new directory
    allist - show all objects in the folder
    dela - delete everything on the screen
    help - view this message
    delobj _file.txt_ - delete a file
    delpk _directory_ - delete a directory
    rid _file.txt_ - read a file
    riname _file.txt_ - change the name of the file
    update - update to a new version
    space _file.txt_ - show a file's size
    """)

def spaceoffile(file: str):
    if ((int(os.path.getsize(file)))/1024)/1024 <= 1:
        if ((int(os.path.getsize(file)))/1024) <=1:
            print((int(os.path.getsize(file)))," byte")
        else:
            print(((int(os.path.getsize(file)))/1024)," kilobyte")
    else:
        print(((int(os.path.getsize(file)))/1024)/1024,"mb")

def update_offline():
    os.system("echOS.py")
    exit()

def update_online():
    path=os.path.join(location,"echOS.py")
    echOs_py = requests.get(link)
    if echOs_py.status_code == 200:
        with open(path, 'wb') as file:
            file.write(echOs_py.content)
        print("Update downloaded successfully.")
    else:
        print("Failed to download the update file.")
    os.system("echOS.py")

def riname(file: str,new: str):
    os.rename(os.path.join(location,file),new)

def ridfile(file: str):
    ridF = open(os.path.join(location,file),'r')
    print(ridF.read())

def newpk(directory: str):
    path = os.path.join(location,directory)
    os.mkdir(path)

def delobj(file: str):
    path = os.path.join(location,file)
    os.remove(path)

def delpk(directory: str):
    path = os.path.join(location,directory)
    path_files = os.listdir(os.path.join(location,directory))
    if len(path_files)==0:
        os.rmdir(path)
    else:
        for i in range(0,len(path_files)):
            print(f"Deleting {path_files[i]}")
            os.remove(os.path.join(location,path_files[i]))
        os.rmdir(path)

def coms(com: str):
    if com=="exit":
        dots="."
        for i in range(3):
            print(dots)
            dots+=" ."
            time.sleep(0.1)
        exit()
    elif "newpk " in com:
        com=com.replace("newpk ","")
        newpk(com)
    elif com=="allist":
        print(os.listdir())
    elif com=="dela":
        os.system("clear")
    elif "delpk " in com:
        com=com.replace("delpk ","")
        delpk(com)
    elif "delobj " in com:
        com=com.replace("delobj ","")
        delobj(com)
    elif "rid " in com:
        com=com.replace("rid ","")
        ridfile(com)
    elif "riname " in com:
        com=com.replace("riname ","")
        new=input("Enter the new name: ")
        riname(com,new)
    elif "update " in com:
        com=com.replace("update ","")
        if com=="offline":
            update_offline()
        elif com=="online":
            update_online()
    elif "space " in com:
        com=com.replace("space ","")
        spaceoffile(com)
    elif com=="help":
        help()
    elif com=="duolingo":
        try:
            os.system(os.path.join(location,"Duolingo.url"))
        except:
            print("Not available!")
    elif "pk " in com:
        com=com.replace("pk ","")
        os.chdir(com)

def home():
    port=""
    while port!="exit":
        exit=input(f"{location}/:>")
        coms(exit)

#Start the system
print("""ECH OS version 0.15p (beta).
All rights reserved©.""")
home()
#Original version