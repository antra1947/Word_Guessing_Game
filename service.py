# service_runner.py

import os
import subprocess
import sys

# Import the Hangman function from the game
from hangman import Hangman
from record import Record

def main():
    print("\n--- Starting Hangman Game ---\n")
    Hangman()

    print("\n--- Viewing Local Records ---\n")
    Record()

    print("\n--- Uploading Data to MySQL ---\n")
    subprocess.run([sys.executable, 'data.py'])

    print("\n--- Viewing MySQL Records ---\n")
    subprocess.run([sys.executable, 'viewmysql.py'])

if __name__ == "__main__":
    main()
