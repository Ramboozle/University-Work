# Write a program that manages a list of countries and their capital cities. It should
#  prompt the user to enter the name of a country. If the program already "knows"
#  the name of the capital city, it should display it. Otherwise it should ask the user to
#  enter it. This should carry on until the user terminates the program (how this
#  happens is up to you).
#  Note: A good solution to this task will be able to cope with the country being entered
#  variously as, for example, "Wales", "wales", "WALES" and so on.

while True:
    countries = {"england" : "london", "wales" : "cardiff", "scotland" : "edinburgh",
                 "romania" : "bucharest" , "netherlands" : "amsterdam", "france" : "paris"}
    country = input('Enter the name of a country: ').lower()
    if country in countries:
        print(f'The capital city of {country} is {countries[country]}')
    else:
        capital = input(f'Enter the capital city of {country}: ')
        countries[country] = capital
    if input('Do you want to continue? (y/n) ') == 'n':
        break