import subprocess
import time
print("What would you like to view? \n\nAnime\nMovies/Shows\nDisney+\n")
loop = True
pause = 2

while loop == True:
    answer = input("Type what you would like to watch and press the enter key.\n\n")
    answer = answer.lower()
    answer = answer[:3]
    if answer == "ani":
        print("\nEnjoy watching anime!")
        time.sleep(pause)
        subprocess.Popen(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://www.crunchyroll.com'])
        loop = False
        
    elif answer == "mov" or answer == "sho":
        print("\nEnjoy watching movies/Shows!")
        time.sleep(pause)
        subprocess.Popen(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://www.netflix.com/browse'])
        loop = False
        
    elif answer == "dis":
        print("\nHi, I'm Curtis and you're watching Disney+!")
        time.sleep(pause)
        subprocess.Popen(['C:\Program Files\Google\Chrome\Application\chrome.exe','https://www.disneyplus.com/home'])
        loop = False
        
    else:
        print("Please type another item from the list as seen and press enter.")
        time.sleep(3)
