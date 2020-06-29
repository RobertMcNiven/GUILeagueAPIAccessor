import requests
# Must have this library for application to work.
from tkinter import *
import json

# Initiating Tk method
root = Tk()
enterSummonerName = Entry(root)
enterSummonerName.grid(row = 0, column = 1)

# This api key is user specific unless I have a paid license to share it. It is from https://developer.riotgames.com/
apiKey = "MAKE SURE TO ADD THE API KEY BEFORE RUNNING"
print(apiKey)
if apiKey == "MAKE SURE TO ADD THE API KEY BEFORE RUNNING":
    exit()

# Setting global variables
inGameName = ""
tier = ""
rank = ""
leaguePoints = 0
wins = 1
losses = 1
winRatio = (wins / (wins + losses)) * 100
winRatio = int(winRatio)

placeNameLabel = Label(root)
placeTierAndRankLabel = Label(root)
placeLPLabel = Label(root)
placeWinsAndLossesLabel = Label(root)
winRateLabel = Label(root)

placeNameRow = 2
placeNameColumn = 0
placeTierAndRankRow = 3
placeTierAndRankColumn = 0
placeLPRow = 4
placeLPColumn = 0
placeWinsAndLossesRow = 5
placeWinsAndLossesColumn = 0
winRateRow = 6
winRateCollumn = 0

# Function to acess API data. It is recieved in JSON format.
def APILookUp(name):
    # connecting to API and getting data
    response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + apiKey)
    # Changing data type from byte to JSON
    data = response.json()
    # Accessing values based on keys
    encryptedSummonerId = data["id"]
    inGameName = data["name"]
    level = data["summonerLevel"]

    # Using the encrypted summoner ID to access the second API
    response2 = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerId + "?api_key=" + apiKey)
    data2 = response2.json()
    rankedData = data2[0]

    # This next conditional checks to make sure the queue type is ranked and not ranked_flex
    # I wanted ranked becasue that is what is more widely played
    getQueueType = rankedData["queueType"]
    if getQueueType == "RANKED_FLEX_SR":
        rankedData = data2[1]
        getQueueType = rankedData["queueType"]
    
    # Grabbing data by key again to display on screen
    tier = rankedData["tier"]
    rank = rankedData["rank"]
    leaguePoints = rankedData["leaguePoints"]
    wins = rankedData["wins"]
    losses = rankedData["losses"]
    winRatio = int((wins / (wins + losses)) * 100)

    # Creating the labels that are placed on screen using Tkinter
    placeName = "Summoner Name: " + inGameName
    placeNameLabel = Label(root, text = placeName)
    placeNameLabel.grid(row = placeNameRow, column = placeNameColumn)

    placeTierAndRank = "Rank: " + tier + " " + rank
    placeTierAndRankLabel = Label(root, text = placeTierAndRank)
    placeTierAndRankLabel.grid(row = placeTierAndRankRow, column = placeTierAndRankColumn)

    placeLP = "League Points: " + str(leaguePoints)
    placeLPLabel = Label(root, text = placeLP)
    placeLPLabel.grid(row = placeLPRow, column = placeLPColumn)

    placeWinsAndLosses = "Wins: " + str(wins) + "\tLosses: " + str(losses)
    placeWinsAndLossesLabel = Label(root, text = placeWinsAndLosses)
    placeWinsAndLossesLabel.grid(row = placeWinsAndLossesRow, column = placeWinsAndLossesColumn)

    winRate = "Winrate: " + str(winRatio) + "%"
    winRateLabel = Label(root, text = winRate)
    winRateLabel.grid(row = winRateRow, column = winRateCollumn)

# Function for when the button is clicked.
def click():
    # Accessing all my global variables that will change within this function.
    global placeNameColumn
    global placeTierAndRankColumn
    global placeLPColumn
    global placeWinsAndLossesColumn
    global winRateCollumn

    global placeNameRow
    global placeTierAndRankRow
    global placeLPRow
    global placeWinsAndLossesRow
    global winRateRow

    # Getting the string entered by the user into the text box.
    summonerName = enterSummonerName.get()

    # Conditional statement that checks if the user is looking up one person or a lobby of people.
    if "joined the lobby" in summonerName:
        # If more than one person, split the string at "joined the lobby" and you should have 5 elements
        allSummonerNames = summonerName.split("joined the lobby", 5)
        # Making a list of all the names
        listOfAllNames = [str(allSummonerNames[0]), str(allSummonerNames[1]), str(allSummonerNames[2]), str(allSummonerNames[3]), str(allSummonerNames[4])]
        # Stripping the \n character from every element in the list
        listOfAllNames[1] = listOfAllNames[1].strip("\n")
        listOfAllNames[2] = listOfAllNames[2].strip("\n")
        listOfAllNames[3] = listOfAllNames[3].strip("\n")
        listOfAllNames[4] = listOfAllNames[4].strip("\n")

        # Using a for loop to iterate the call to the API function for as many names that are in the list.
        for i in range(len(listOfAllNames)):
            # print(listOfAllNames[i])
            APILookUp(str(listOfAllNames[i]))
            placeNameColumn += 1
            placeTierAndRankColumn += 1
            placeLPColumn += 1
            placeWinsAndLossesColumn += 1
            winRateCollumn += 1
    else:
        # If only one person then just look up the one username and move the next search down.
        APILookUp(summonerName)
        placeNameRow += 7
        placeTierAndRankRow += 7
        placeLPRow += 7
        placeWinsAndLossesRow += 7
        winRateRow += 7

    # Resetting the column and row values for each click of the button.
    placeNameColumn = 0
    placeTierAndRankColumn = 0
    placeLPColumn = 0
    placeWinsAndLossesColumn = 0
    winRateCollumn = 0

    placeNameRow += 7
    placeTierAndRankRow += 7
    placeLPRow += 7
    placeWinsAndLossesRow += 7
    winRateRow += 7

# Creating a button in the root window.
mainButton = Button(root, text = "ENTER NAME", command = click)
# placing the button at (1,1)
mainButton.grid(row = 1, column = 1)
# The text that will tell the user what to do.
spacing = Label(root, text = 'Enter the summoner you would like to search\nor\ncopy the client text "<player> joined the lobby" for all five players:')
spacing.grid(row = 0, column = 0)
spacing2 = Label(root, text = "\t")
spacing2.grid(row = 0, column = 2)

# Initiating an image as a PhotoImage to be used as an icon
appIcon = PhotoImage(file = "League API Application\icon.png")
# I got this image from https://icons8.com/icons/set/league-of-legends

# Setting the application icon
root.iconphoto(False, appIcon)
# Chaning the title of the window
root.title("League of Legends: Ranked API Accessor")
# Running the main window until the program is terminated.
root.mainloop()