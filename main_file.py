import time
#Import from the lottery file all that will be needed for display purposes
#And to be able to write for the text file

from lottery import legal_age, lottery_random, player_numbers, prize_catogery


#Importing the date from datetime module to get the output of the date
from datetime import date

#Creating the variables for the functions to be displayed on screen and to be able to write
#in a text file

player_age = legal_age()


now = date.today()

lottery_numbers = lottery_random()

player_numbers = player_numbers()

category_details = prize_catogery(player_numbers, lottery_numbers)

#Printing the results per function with its output
print("The results of the lottery for today", str(now))
print("Lottery Numbers: ", str(lottery_numbers))
print("User Numbers: ", str(player_numbers))
print("You have won: ", category_details['category'])
time.sleep(5)

#Creating a text file to write the results
#And putting each results on a new line
with open('output-file.txt', 'w+') as file:
    file.write("The results of the lottery for today " + str(now) + "\n")
    file.write("Lottery Numbers: " + str(lottery_numbers) + "\n")
    file.write("User Numbers: " + str(player_numbers) + "\n")
    file.write("You have won: " + category_details['category'] + "\n")
