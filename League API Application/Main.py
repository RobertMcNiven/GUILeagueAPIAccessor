import requests
from tkinter import *
import json

root = Tk()
enterSummonerName = Entry(root)
enterSummonerName.grid(row = 0, column = 1)

apiKey = "MAKE SURE TO ADD THE API KEY BEFORE RUNNING"
print(apiKey)
if apiKey == "MAKE SURE TO ADD THE API KEY BEFORE RUNNING":
    exit()

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

def APILookUp(name, amntBeingSearched):
    
    if amntBeingSearched == 1:
        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + apiKey)
        # print(response.content)
        # print(type(response.content))
        data = response.json()
        # print(data)
        encryptedSummonerId = data["id"]
        # print(encryptedSummonerId)
        inGameName = data["name"]
        level = data["summonerLevel"]

        response2 = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerId + "?api_key=" + apiKey)
        # print(response2.content)
        data2 = response2.json()
        # print(data2)
        rankedData = data2[0]
        # print(rankedData)
        getQueueType = rankedData["queueType"]
        if getQueueType == "RANKED_FLEX_SR":
            rankedData = data2[1]
            getQueueType = rankedData["queueType"]
        tier = rankedData["tier"]
        rank = rankedData["rank"]
        leaguePoints = rankedData["leaguePoints"]
        wins = rankedData["wins"]
        losses = rankedData["losses"]
        winRatio = int((wins / (wins + losses)) * 100)

        placeName = "Summoner Name: " + inGameName
        placeNameLabel = Label(root, text = placeName)
        placeNameLabel.grid(row = placeNameRow, column = 0)

        placeTierAndRank = "Rank: " + tier + " " + rank
        placeTierAndRankLabel = Label(root, text = placeTierAndRank)
        placeTierAndRankLabel.grid(row = placeTierAndRankRow, column = 0)

        placeLP = "League Points: " + str(leaguePoints)
        placeLPLabel = Label(root, text = placeLP)
        placeLPLabel.grid(row = placeLPRow, column = 0)

        placeWinsAndLosses = "Wins: " + str(wins) + "\tLosses: " + str(losses)
        placeWinsAndLossesLabel = Label(root, text = placeWinsAndLosses)
        placeWinsAndLossesLabel.grid(row = placeWinsAndLossesRow, column = 0)

        winRate = "Winrate: " + str(winRatio) + "%"
        winRateLabel = Label(root, text = winRate)
        winRateLabel.grid(row = winRateRow, column = 0)

    elif amntBeingSearched == 5:

        response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + apiKey)
        # print(response.content)
        # print(type(response.content))
        data = response.json()
        # print(data)
        encryptedSummonerId = data["id"]
        # print(encryptedSummonerId)
        inGameName = data["name"]
        level = data["summonerLevel"]

        response2 = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerId + "?api_key=" + apiKey)
        # print(response2.content)
        data2 = response2.json()
        # print(data2)
        rankedData = data2[0]
        # print(rankedData)
        getQueueType = rankedData["queueType"]
        if getQueueType == "RANKED_FLEX_SR":
            rankedData = data2[1]
            getQueueType = rankedData["queueType"]
        tier = rankedData["tier"]
        rank = rankedData["rank"]
        leaguePoints = rankedData["leaguePoints"]
        wins = rankedData["wins"]
        losses = rankedData["losses"]
        winRatio = int((wins / (wins + losses)) * 100)

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

def click():
    global placeNameLabel
    global placeTierAndRankLabel
    global placeLPLabel
    global placeWinsAndLossesLabel
    global winRateLabel

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

    placeNameLabel.destroy()
    placeTierAndRankLabel.destroy()
    placeLPLabel.destroy()
    placeWinsAndLossesLabel.destroy()
    winRateLabel.destroy()

    summonerName = enterSummonerName.get()
    # print(summonerName)

    if "joined the lobby" in summonerName:
        allSummonerNames = summonerName.split("joined the lobby", 5)
    else:
        APILookUp(summonerName, 1)
        placeNameRow += 7
        placeTierAndRankRow += 7
        placeLPRow += 7
        placeWinsAndLossesRow += 7
        winRateRow += 7

    allSummonerNamesLength = len(allSummonerNames)
    
    if allSummonerNamesLength > 1:
        listOfAllNames = [str(allSummonerNames[0]), str(allSummonerNames[1]), str(allSummonerNames[2]), str(allSummonerNames[3]), str(allSummonerNames[4])]
        # print(listOfAllNames)
        listOfAllNames[1] = listOfAllNames[1].strip("\n")
        listOfAllNames[2] = listOfAllNames[2].strip("\n")
        listOfAllNames[3] = listOfAllNames[3].strip("\n")
        listOfAllNames[4] = listOfAllNames[4].strip("\n")
        # print(listOfAllNames)

        for i in range(len(listOfAllNames)):
            # print(listOfAllNames[i])
            APILookUp(str(listOfAllNames[i]), 5)
            placeNameColumn += 1
            placeTierAndRankColumn += 1
            placeLPColumn += 1
            placeWinsAndLossesColumn += 1
            winRateCollumn += 1

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

mainButton = Button(root, text = "ENTER NAME", command = click)

mainButton.grid(row = 1, column = 1)

spacing = Label(root, text = "Enter the summoner you would like to search:")
spacing.grid(row = 0, column = 0)
spacing2 = Label(root, text = "\t")
spacing2.grid(row = 0, column = 2)

root.mainloop()
