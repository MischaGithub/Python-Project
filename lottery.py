import random


# Creating a function to determined whether the user is old enough to play
# Importing sys function allows the program to close if the user is under age
# Doing the error handling and having the if statement within the try block
def legal_age():

    player = ""
    try:
        player = int(input("Please enter your age. \n"))
        if player < 18:
            print("You are not allowed to play")
            exit()
        elif player >= 18:
            print("Welcome to the National lottery")
    except ValueError:
        print("Error input")
        exit()

    return player

# Creating a function for the random numbers to be selection between 1 and 49
def generate_random_number():

    random_number = random.randint(1, 49)
    return random_number


# Creating function to generate lottery numbers
# Creating a empty list for the lottery numbers to be added
def lottery_random():

    # Creating a for loop to generate the lottery numbers with the range between 1 and 49.
    # Also sorting the lottery numbers list
    lottery_numbers = []

    for lottery_number_index in range(0, 6):

        random_number = generate_random_number()
        if random_number not in lottery_numbers:
            lottery_numbers.append(random_number)

            lottery_numbers.sort()
    return lottery_numbers


#Creating a function for the user to input the numbers from 1 to 49.
#Creating en empty list fro the users selection to be added and then displayed
def player_numbers():
    #Creating a empty list for the users numbers
    user_numbers = []

    for user_number_index in range(0, 6):
        while True:
            try: #Creating a error handling if a string might be enter
                user_random = int(input("Please enter a number between 1 and 49. \n"))
                user_numbers.append(user_random)
                break
            except ValueError:
                print("Oops! That was not a valid number only positive numbers are accepted. Try again")

    #Sorting the users numbers in acsending order
    user_numbers.sort()

    return user_numbers


#Creating a function to display the lottery numbers horizontally
def display_lottery_numbers(lottery_numbers):
    for lottery_number_index in range(len(lottery_numbers)):
        if lottery_number_index == len(lottery_numbers) - 1:
            print(lottery_numbers[lottery_number_index], end=". ")
        else:
            print(lottery_numbers[lottery_number_index], end=", ")

    return lottery_numbers


#Creating a function to comparing the lottery numbers and the users numbers
#Also having a category will determine how many numbers matched and then showing the prize
def prize_catogery(player_numbers, lottery_numbers):
    #Creating a count to determine how many numbers match
    count = 0
    user_results = player_numbers
    lottery_results = lottery_numbers

    for number in user_results:
        if number in lottery_results:
            count += 1

    #Creating the categories if the count == to the amount of numbers match
    #And then the count determines the prize
    category = ""
    if count == 6:
        category = "Jackpot Amount!! R10 000.00"
    elif count == 5:
        category = "R8 584.00"
    elif count == 4:
        category = "R2 384.00"
    elif count == 3:
        category = "R100.50"
    elif count == 2:
        category = "R20.00"
    else:
        category = "R0.00"

    category_details = {'count': count, 'category': category}
    return category_details


#Creating a function to display all the required results
def display_all(player, lottery_numbers, user_numbers):
    return player + lottery_numbers + user_numbers



