squidLogo = """
                                                                                                                                                                                                                                                                                 
                                  ░░██████                            
                            ░░██████▒▒░░▒▒████                        
                          ██████░░░░░░░░░░░░██▓▓                      
                        ████▓▓░░░░░░░░░░░░░░▒▒████                    
                      ████▒▒░░░░░░░░░░░░░░░░░░▒▒████                  
                  ░░████░░░░░░░░░░░░░░░░░░░░░░░░▒▒████                
                  ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒████              
                ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒████            
              ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██░░          
            ████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████          
          ▒▒████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████        
          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒████      
        ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓████    
      ████▒▒░░░░░░░░░░░░▓▓██▓▓██▒▒░░░░░░░░░░████░░░░░░░░░░░░░░████    
      ████░░░░░░░░░░▒▒██        ░░▓▓██▓▓██░░      ██░░░░░░░░░░▒▒████  
    ████░░░░░░░░░░░░██  ░░████████  ▒▒██  ██████    ██░░░░░░░░░░▓▓██▒▒
  ░░████░░░░░░░░░░██    ████▓▓▓▓████      ██▓▓████  ░░▓▓░░░░░░░░░░████
  ████░░░░░░░░░░░░██    ████▓▓▓▓████      ██▓▓████    ██░░░░░░░░░░▒▒██
▒▒████░░░░░░░░░░░░██    ░░██████▓▓        ██████      ██░░░░░░░░░░░░██
██████░░░░░░░░░░░░██                                  ██░░░░░░░░░░░░██
░░██████░░░░░░░░░░██                  ░░            ▒▒██░░░░░░░░▒▒████
    ██████████████████              ████▓▓        ▒▒██▒▒████████████▒▒
                ██░░████████████████████████████████▒▒▒▒██            
                ██▒▒░░████████████▓▓▒▒░░▒▒████████▒▒░░████            
                ▒▒▓▓░░░░░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░░░██▒▒            
                  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒██              
                  ██▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒██              
                ████░░░░░░▒▒▒▒░░░░░░░░░░▒▒░░░░▒▒░░░░░░████            
                ██▓▓░░░░░░▒▒▒▒░░░░░░▒▒░░░░░░░░▒▒░░░░▒▒████            
                ██▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░░░░░▒▒▓▓██            
              ░░██▒▒░░░░░░▒▒░░░░░░▒▒▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒██            
                ██░░░░▒▒░░██▒▒▒▒▒▒░░░░▒▒░░▒▒░░██▒▒░░▒▒▓▓██            
                ████░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██░░▒▒░░██▒▒▒▒▒▒████            
                  ████▓▓██████▒▒▒▒░░████▒▒░░▒▒▓▓██▒▒████              
                  ▒▒██████  ████▓▓████▒▒██████  ██████     
                  
                  
 __      __      ___.     _________            .__    .___
/  \    /  \ ____\_ |__  /   _____/ ________ __|__| __| _/
\   \/\/   // __ \| __ \ \_____  \ / ____/  |  \  |/ __ | 
 \        /\  ___/| \_\ \/        < <_|  |  |  /  / /_/ | 
  \__/\  /  \___  >___  /_______  /\__   |____/|__\____ | 
       \/       \/    \/        \/    |__|             \/ 
       WORK IN PROGRESS
           
                                         
                                                                                                                                                                                         
"""













print(squidLogo)

























from typing import Set
import requests
from colorama import Fore, Back, Style
import time
#---------------------------------------Technologys-----------------------------------
wordpressFavicon = "F�BCF�BCF�BCF�BCF�BCF�BCF�BCF�BCF�BCF�BCF�BCF�BCFSCDF"
#-------------------------------------------------------------------------------------
#---------------------------------------Plugins---------------------------------------
pluginsWordPress = ["Rank Math SEO Plugin"]
#-------------------------------------------------------------------------------------
isWordPress = False
detectedService = "None"






def Setup():
    openServiceNow = open("slctedService.txt", "r")
    global setupSetting
    global selectService
    global selectedService
    global slctService

    print(Fore.LIGHTWHITE_EX, "<Setup>")
    
    if (isWordPress == True):
        print(Fore.YELLOW, "Detected Service:", "WordPress")
    else:
        print(Fore.YELLOW, "Detected Service:", detectedService)
    print(Fore.YELLOW, "Selected Service :", openServiceNow.read())
    print(Fore.LIGHTYELLOW_EX, "[1]selectService [2]GotoMainHub", Fore.LIGHTMAGENTA_EX)
    setupSetting = input(":")

    if (setupSetting == "1"):
        selectService = input("Set Service :")
        with open("slctedService.txt", "w") as serviceFile:
            serviceFile.write(selectService)
        Setup()
    elif (setupSetting == "2"):
        mainHub()
    else:
        print("Unknown Command")





def mainHub():
    openServiceNow2 = open("slctedService.txt", "r")
    global HubSetting  
    print(Fore.LIGHTWHITE_EX, "<MainHub>")
    if (isWordPress == True):
        print(Fore.YELLOW, "Detected Service:", "WordPress")
    else:
        print(Fore.YELLOW, "Detected Service:", detectedService)
    print(Fore.YELLOW, "Selected Service :", openServiceNow2.read())
    print(Fore.LIGHTYELLOW_EX, "[1]Service-Discovery [2]dirChecker [3]Setup [4]Plugin-Discovery", Fore.LIGHTMAGENTA_EX)
    HubSetting = input("What Setting you want ? :")   

    if (HubSetting == "1"):
        discoverySetup()
    elif (HubSetting == "2"):
        mainSetup()
    elif (HubSetting == "3"):
        Setup()
    elif (HubSetting == "4" and isWordPress == True or "WordPress" in openServiceNow2.read()):
        pluginDiscoverySetup()
    else:
        print("[1]Unknown Command or [2]no service selected.. CREATE ISSUE WHEN: (1)Service selected but this error[2] still occurs. (2)Right command but this error[1] still occurs") 
        mainHub()

def discoverySetup():
    print(Fore.LIGHTWHITE_EX, "<Discovery Setup>", Fore.LIGHTMAGENTA_EX)
    global discoveryUrl
    discoveryUrl = input("Discovery Target Url (https://) :")
    discovery()

def discovery():
    global isWordPress
    isWordPress = False
    discoveryRequest = requests.get(discoveryUrl + "favicon")
    if (wordpressFavicon in discoveryRequest.text):
        isWordPress = True
        print(Fore.GREEN, "wordpress Detected")
        mainHub()
    else:
        print(Fore.RED, "Sorry, did not find any Technology/Service, please wait for the next update or contribute to the github and add some check functions")
        mainHub()

def pluginDiscoverySetup():
    global openServiceNow4
    openServiceNow4 = open("slctedService.txt", "r")
    print(Fore.LIGHTWHITE_EX, "<Plugin-Discovery Setup>", Fore.LIGHTMAGENTA_EX)
    global pluginDiscoveryUrl
    pluginDiscoveryUrl = input("pluginDiscover Target Url (https://) :")
    pluginDiscovery()

def pluginDiscovery():
    pluginDiscoveryRequest = requests.get(pluginDiscoveryUrl + "sitemap.xml")
    if (isWordPress == True and pluginsWordPress[0] in pluginDiscoveryRequest.text or "WordPress" in openServiceNow4.read() and pluginsWordPress[0] in pluginDiscoveryRequest.text):
        print(Fore.GREEN, pluginsWordPress[0], "Detected", Fore.LIGHTMAGENTA_EX)
    else:
        print(Fore.RED, "Sorry, did not find any Plugins, please wait for the next update or contribute to the github and add some check functions")
        mainHub()



def mainSetup():
    global openServiceNow3
    openServiceNow3 = open("slctedService.txt", "r")
    global url
    global wordlist
    url = input("Target URL (https://) :")
    if (isWordPress == True or "WordPress" in openServiceNow3.read()):
        wordlist = "WordPressSample"
    else:
        print(Fore.RED, "Unknown Service")
        mainHub()
    secondarySetup()



def secondarySetup():
    print(Fore.LIGHTYELLOW_EX, "Your URL :" + url)
    print("Your Wordlist : " + wordlist, Fore.LIGHTMAGENTA_EX)
    checkOption = input("Are you sure you want to go with these Options (yes / no) :")
    if (checkOption == "y" or checkOption == "yes"):
        launchDirChecker()
    elif (checkOption == "n" or checkOption == "no"):
        mainSetup()
    else:
        print("Unknown Command")
        secondarySetup()




def launchDirChecker():

    with open(wordlist + ".txt") as wordlisttxt:
        data = wordlisttxt.read()
        lines = data.split("\n")
    for getWordlist in lines:
        r = requests.get(url + getWordlist)

        if (r.status_code == 200):
            print(Fore.GREEN + "[+]", r.url, "<-- URL FOUND", r.status_code)
        if (url == r.url):
            print(Fore.YELLOW + "[!]", r.url, "<-- INDEX REDIRECT DETECTED :", url,getWordlist)
        elif (getWordlist in r.url and r.status_code != 200 and "?redirect" in r.url):
            print(Fore.GREEN + "[+]", r.url, "<-- URL REDIRECT DETECTED :", url,getWordlist)
        if (r.status_code == 400):
            print(Fore.RED + "[-]", r.url, "<-- BAD REQUEST ", r.status_code)
        elif (r.status_code == 401):
            print(Fore.RED + "[-]", r.url, "<-- UNAUTHORIZED ", r.status_code)
        elif (r.status_code == 401):
            print(Fore.RED + "[-]", r.url, "<-- FORBIDDEN ", r.status_code)
        elif (r.status_code == 404):
            print(Fore.RED + "[-]", r.url, "<-- URL NOT FOUND ", r.status_code)
        elif (r.status_code == 500):
            print(Fore.RED + "[-]", r.url, "<-- INTERNAL SERVER ERROR", r.status_code)
        elif (r.status_code == 503):
            print(Fore.RED + "[-]", r.url, "<-- SERVICE UNAVAILABLE ", r.status_code)




mainHub()