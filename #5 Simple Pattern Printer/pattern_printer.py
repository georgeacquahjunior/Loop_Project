# Simple Pattern Printer

# Goal: Print a triangle pattern of * using loops.
# Success Criteria: Number of rows is user-defined; pattern prints correctly.
# Stretch Goal: Add inverted and pyramid pattern options.

pattern = int(input('Insert the number of rows for sketching the triangle.'))
for i in range(pattern + 1):
    print('*' * i)