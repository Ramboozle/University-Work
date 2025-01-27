amount  = int(input('Enter the times table you want to print: '))
while amount < 1 or amount > 12:
    amount = int(input('Please enter a number between 1 and 12: '))
for number in range (1, 13):
    print(str(amount) + ' x ' + str(number) + ' = ' + str(amount * number))