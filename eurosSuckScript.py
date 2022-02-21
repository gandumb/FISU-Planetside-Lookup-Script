import pandas as pd
import webbrowser as wb
import requests as rqst
from ratelimit import limits, RateLimitException, sleep_and_retry

CSV = 'eurosSUCK.csv'
URL = 'https://ps2.fisu.pw/player/'
MAX_CALLS_PER_TIME_PERIOD = 1
TIME_PERIOD = 60 #in seconds

def getPlayerNames(csvPath):
    columns = pd.read_csv(csvPath).columns
    
    data = pd.read_csv(csvPath, names=columns)
    
    playerNames = data.PlayerNames.tolist()
    
    return playerNames[1:]
   
@sleep_and_retry
@limits(calls=MAX_CALLS_PER_TIME_PERIOD, period=TIME_PERIOD) 
def sendFisuGetRequest(fisuURL, name):
    params = {'name':name}
    
    r = rqst.get(fisuURL, params)
    
    print("Finished %s search request" % (name))
   
 
playerNames = getPlayerNames(CSV)

print(playerNames)

while(1==1):
    print('\nStarting to put euros in their place!\n')

    for playerName in playerNames:
        print("Sending %s search request..." % (playerName))
        sendFisuGetRequest(URL, playerName)
        
    print('Finished putting euros in their place!')
    
    print("Restarting the cycle of putting euros in their place!")


"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

# sendFisuGetRequest('https://ps2.fisu.pw/player/', 'LEXNC')

# def openURL():
#     return urllib.urlopen('https://www.youtube.com/')

# openBrowser()

# def openBrowser():
    
#     url = 'https://ps2.fisu.pw/player/?name=LEXNC'
#     chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    
#     c = wb.get(chrome_path)
    
#     c.open('https://ps2.fisu.pw/player/?name=eurossuck')
    
#     print(url)