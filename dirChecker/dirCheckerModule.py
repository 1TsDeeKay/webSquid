import requests 





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

    a_file = open(wordlist + ".txt")

    lines = a_file.readlines()
    for getWordlist in lines:
        r = requests.get(url + getWordlist)

        if (r.status_code == 200):
            print(r.url, "<-- URL FOUND", r.status_code)
        else:
            print(r.url, "<-- URL NOT FOUND", r.status_code)


mainSetup()