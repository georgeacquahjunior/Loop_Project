# COUNTDOWN TIMER

# Stretch Goal: Print “Time’s up!” or play a sound at the end.

import time
import playsound, winsound

print('---------- A COUNTDOWN TIMER ----------')

# Ask for a number and count down
number_count = int(input('Enter a number to countdown: '))
while number_count > -1:
    print(number_count)
    number_count = number_count - 1
    time.sleep(1) # 1 second delay
print("Time's Up!")
# playsound('alarm.mp3')  # Replace with your sound file path
winsound.Beep(2000, 1000) # High-pitched, long beep