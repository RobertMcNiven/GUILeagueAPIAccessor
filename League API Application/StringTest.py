# This is the string that is outputted by the client when people enter the game lobby
# It comes in the form of "<username> joined the lobby"

# I want people to be able to copy all five of these outputs into the search bar and have it search for all of the players in game.

no_of_lines = 5
lines = ""
for i in range(no_of_lines):
    lines+=input() + " "
    inputList = lines.split()

print(str(inputList[0]))
print(str(inputList[4]))
print(str(inputList[8]))
print(str(inputList[12]))
print(str(inputList[17]))
print(len(inputList))

# This didnt really work because if the player had spaces in their name it would crash.
# instead I changed it, in the main file, to split at the '\n' character.

