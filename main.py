import time
import random
import subprocess

gameselection = input("Choose a game to play: ")

if gameselection.lower() == "space invaders":
    print("Game starting..")
    subprocess.run(["python", "Space Invaders/space_invaders.py"])  
elif gameselection.lower() == "rock paper scissors":
    print("Game starting..")
    subprocess.run(["python", "Rock paper Scissors/rock_paper_scissors.py"]) 
elif gameselection.lower() == "text adv":
    print("Game starting..")
    subprocess.run(["python", "Text adventure engine/app.py"])
elif gameselection.lower() == "tic tac toe":
    print("Game starting..")
    subprocess.run(["python", "Tic Tac Toe/tic tac toe.py"])
else:
    print("This game wasn't recognised, hopefully its coming soon..")


















