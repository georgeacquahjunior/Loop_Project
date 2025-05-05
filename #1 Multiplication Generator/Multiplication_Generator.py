# Multiplication Table Generator

"""
Goal: Take a number as input and display its multiplication table (1 to 10).

Success Criteria: Outputs correctly formatted results (5 x 1 = 5, ..., 5 x 10 = 50).

Stretch Goal: Allow user to set custom range.
"""

# Take a number as input
input_by_user = (int(input('Enter a number to display the Multiplication table from (1 to 10) ')))

# Display its multiplication table (1 to 10)
for number in range(1, 13, 1):
    print(f'{input_by_user} * {number} = {input_by_user * number}')