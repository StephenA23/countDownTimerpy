# This is a basic countdown timer
# The code does not use any GUI
# Testing of the code can be done in the terminal/command-line-interface
# When countdown is done, a song will be played

import time
from playsound import playsound

# -----------------------------------------------------------------------------------
# Function Name - startCount
# Inputs        - int:totalSeconds
# Output        - none
# Purpose       - To start the countdown and alert the user when done
# -----------------------------------------------------------------------------------
def startCount(totalSeconds):

    while totalSeconds:
        hours, seconds = divmod(totalSeconds,3600)
        minutes, seconds = divmod(totalSeconds, 60)
        totalTime = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(totalTime)
        time.sleep(1)
        totalSeconds -= 1
    
    if (totalSeconds == 0):
            print("Countdown Over !!!!!!! ")
            playsound('/Users/stephenagberien/Desktop/songs/Buju.mp3')

# No real need for this function but I used it anyway to make the code 
# easier to read

# -----------------------------------------------------------------------------------
# Function Name - convertSeconds
# Inputs        - str:hours, str:minutes, str:seconds
# Output        - int:totalSeconds
# Purpose       - Convert the totalTime to seconds
# -----------------------------------------------------------------------------------
def convertSeconds(hours, minutes, seconds):

    totalSeconds = int(seconds) + (int(minutes) * 60) + (int(hours) * 60 * 60)
    return totalSeconds



if __name__ == "__main__":
    # Ask the user to input the time
    print("Time format Hours: Minutes: Seconds ")
    hours   = input("Enter hours countdown time: ")
    minutes = input("Enter minutes countdown time: ")
    seconds = input("Enter seconds countdown time: ")


    totalSeconds = convertSeconds(hours, minutes, seconds)
    startCount(totalSeconds)