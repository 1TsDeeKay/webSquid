import requests
from colorama import Fore, Back, Style





def mainSetup():
    global url
    global wordlist
    url = input("Target URL (https://) :")
    wordlist = input("your wordlist (path):")
    secondarySetup()



def secondarySetup():
    print("Your URL :" + url)
    print("Your Wordlist : " + wordlist)
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




mainSetup()