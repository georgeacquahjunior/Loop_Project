# COUNTDOWN TIMER

# Goal: Ask for a number and count down to 0 with a 1-second delay.
# Success Criteria: Countdown prints properly with pauses.
# Stretch Goal: Print “Time’s up!” or play a sound at the end.

import time
import playsound

print('---------- A COUNTDOWN TIMER ----------')

# Ask for a number and count down
number_count = int(input('Enter a number to countdown: '))
while number_count > -1:
    print(number_count)
    number_count = number_count - 1
    time.sleep(1) # 1 second delay
