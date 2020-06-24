import requests
from tkinter import *
import json

root = Tk()
enterSummonerName = Entry(root)
enterSummonerName.grid(row = 0, column = 1)
# comment

apiKey = "RGAPI-a1d63c08-04ab-4f2f-b9b8-eb5662129f4f"

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
def click():
    global placeNameLabel
    global placeTierAndRankLabel
    global placeLPLabel
    global placeWinsAndLossesLabel
    global winRateLabel

    placeNameLabel.destroy()
    placeTierAndRankLabel.destroy()
    placeLPLabel.destroy()
    placeWinsAndLossesLabel.destroy()
    winRateLabel.destroy()

    summonerName = enterSummonerName.get()
    response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + apiKey)
    # print(response.content)
    # print(type(response.content))
    data = response.json()
    encryptedSummonerId = data["id"]
    # print(encryptedSummonerId)
    inGameName = data["name"]
    level = data["summonerLevel"]

    response2 = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerId + "?api_key=" + apiKey)
    # print(response2.content)
    data2 = response2.json()
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
    placeNameLabel.grid(row = 2, column = 0)

    placeTierAndRank = "Rank: " + tier + " " + rank
    placeTierAndRankLabel = Label(root, text = placeTierAndRank)
    placeTierAndRankLabel.grid(row = 3, column = 0)

    placeLP = "League Points: " + str(leaguePoints)
    placeLPLabel = Label(root, text = placeLP)
    placeLPLabel.grid(row = 4, column = 0)

    placeWinsAndLosses = "Wins: " + str(wins) + "\tLosses: " + str(losses)
    placeWinsAndLossesLabel = Label(root, text = placeWinsAndLosses)
    placeWinsAndLossesLabel.grid(row = 5, column = 0)

    winRate = "Winrate: " + str(winRatio) + "%"
    winRateLabel = Label(root, text = winRate)
    winRateLabel.grid(row = 6, column = 0)


mainButton = Button(root, text = "ENTER NAME", command = click)

mainButton.grid(row = 1, column = 1)

spacing = Label(root, text = "Enter the summoner you would like to search:")
spacing.grid(row = 0, column = 0)
spacing2 = Label(root, text = "\t")
spacing2.grid(row = 0, column = 2)

root.mainloop()