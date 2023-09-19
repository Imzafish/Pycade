import time
import random
import subprocess

gameselection = input("Choose a game to play: ")

if gameselection.lower() == "space invaders":
    print("Game starting..")
    subprocess.run(["python", "Space Invaders/space_invaders.py"])  # Replace "space_invaders.py" with the actual filename of the game



















