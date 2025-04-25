# Multiplication Table Generator

"""
Stretch Goal: Allow user to set custom range.
"""

# Take a number as input
input_by_user = (int(input('Enter a number to display the Multiplication table based on your range ')))

# Take the range of input from the user
input_range1 = int(input('From: '))
input_range2 = int(input('To:  '))

print(f'Based on your range {input_range1} to {input_range2}')


# Display its multiplication table based on the range chose
for number in range(input_range1, input_range2 + 1, 1):
    print(f'{input_by_user} * {number} = {input_by_user * number}')