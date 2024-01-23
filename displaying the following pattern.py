#adding up some title 
print('\nPRINT THE FOLLOWING PATTERN.\n')

#adding some string to the variable 
numeral = int(input('Type the number you want to print: '))

#function to display the rows you want to show
for vertical_row in range(-1, numeral+1):
    for horizontal_column in range(1, vertical_row + 1):
           print(vertical_row, end= '   ')
    print()

