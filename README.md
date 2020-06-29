# GUILeagueAPIAccessor

## What is this?

This is an application that will allow the user to search ranked data about a player in the game "League of Legends" made by the company Riot.
I wanted to make an easier and more accessible version of already known web applications that accomplish this task (i.e. op.gg and u.gg). I added
this functionality to a simple GUI using python3 and one external library, requests(see Requirements/Installation).

## Requirements/Installation

The user will need to have python3 installed on their machine and use the cmd to run the command 'pip install requests'.
This will install the requests library into the python3 folder and allow the user to run the program. The user will also need
an active API key from https://developer.riotgames.com/. Here all the user needs to have is an active Riot account to sign in with. I am not able
to provide a commercial API key at this time. The API key will need to be pasted into line 12 of the program, in place of "MAKE SURE TO ADD THE API KEY BEFORE RUNNING".

## Usage

To access the program, the user will need to run the Main.py file. The GUI should pop up on the main screen of their machine(as long as all requirements are met).
Once up and running, all the user needs to do is enter a single summoner name, or the text outputed when a lobby of 5 team members is matched, 
and click the 'ENTER' button. Examples of these inputs are in the Examples.txt file.
