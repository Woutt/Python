import urllib.request
import requests
import pyperclip
import os




def menu():
    
    print ("███████╗██╗     ██╗   ██╗██████╗ ███████╗██╗  ██╗      ██████╗ ██████╗  █████╗ ██╗  ██╗██╗   ██╗██╗ ██████╗")
    print ("██╔════╝██║     ██║   ██║██╔══██╗██╔════╝╚██╗██╔╝      ██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗ ██╔╝╚█║██╔════╝")
    print ("█████╗  ██║     ██║   ██║██║  ██║█████╗   ╚███╔╝ █████╗██████╔╝██████╔╝██║  ██║ ╚███╔╝  ╚████╔╝  ╚╝╚█████╗ ")
    print ("██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗ ╚════╝██╔═══╝ ██╔══██╗██║  ██║ ██╔██╗   ╚██╔╝      ╚═══██╗")
    print ("██║     ███████╗╚██████╔╝██████╔╝███████╗██╔╝╚██╗      ██║     ██║  ██║╚█████╔╝██╔╝╚██╗   ██║      ██████╔╝")
    print ("╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═╝     ╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝      ╚═════╝ ")
    print ("Made By Fludex#0767")
    print ("https://github.com/Code-Fludex")
    print ("")
    print("[1] = HTTP")
    print("[2] = HTTPS")
    print("[3] = SOCKS4")
    print("[4] = SOCKS5")
    print("[5] = All Proxys")
print("")

menu()
option = input()


if option == "1": #HTTP
    f = open("HTTP.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()
    f = open("HTTP.txt", "a")
    url = 'https://www.proxy-list.download/api/v1/get?type=http&anon=elite' 
    r = requests.get(url) 
    content = r.text 
    pyperclip.copy(content)
    pyperclip.paste()
    print(content)
    print(type(content))
    f.write(content)
    f.close()
    f = open("HTTP.txt", "a")
    url = 'https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous' 
    r = requests.get(url) 
    content = r.text 
    pyperclip.copy(content)
    pyperclip.paste()
    print(content)
    print(type(content))
    f.write(content)
    f.close()    
    f = open("HTTP.txt", "a")
    url = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=http' 
    r = requests.get(url) 
    content = r.text 
    pyperclip.copy(content)
    pyperclip.paste()
    print(content)
    print(type(content))
    f.write(content)
    f.close()    
    def fileExists(file):
        try:
            f = open(file,'r')
            f.close()
        except FileNotFoundError:
            return False
        return True
    def isLineEmpty(line):
        return len(line.strip()) < 1
    def removeEmptyLines(file):
        lines = []
        if not fileExists(file):
            print ("{} does not exist ".format(file))
            return
        out = open(file,'r')
        lines = out.readlines()
        out.close()
        out = open(file,'w')
        t=[]
        for line in lines:
            if line.strip():
                t.append(line)
        out.writelines(t)   
        out.close()
#fileExists("HTTP.txt")
isLineEmpty("HTTP.txt")
removeEmptyLines("HTTP.txt")


if option == "2": #HTTPS
    f = open("HTTPS.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()

if option == "3": #socks4
    f = open("SOCKS4.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()

if option == "4": #socks5
    f = open("SOCKS5.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()

if option == "5": #socks5
    f = open("ALL_PROXYS.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()

    f = open("ALL_PROXYS.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()
    f = open("ALL_PROXYS.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()
    f = open("ALL_PROXYS.txt", "a")
    texto = urllib.request.urlopen('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt')
    for line in texto:
        #print(line.decode().strip())
        lijntext = line.decode().strip() + "\n"
        print(lijntext)
        f.write(lijntext)
    f.close()





    f.close()


