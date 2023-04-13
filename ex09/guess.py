# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 13:34:41 by joslopez          #+#    #+#              #
#    Updated: 2023/04/12 18:16:17 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

num = random.randint(1, 99)
intent = 1
while 1:
    choice = input("What's your guess between 1 and 99?\n>> ")
    if choice == 'exit':
        print("Goodbye!")
        break
    try:
        choice = int(choice)
    except ValueError:
        print("That's not a number.")
        intent += 1
        continue
    if choice < 1 or choice > 99:
        print("Number is out of range.")
    elif choice < num:
        print("Too low!")
    elif choice > num:
        print("Too high!")
    elif choice == num and num == 42 and intent > 1:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
        break
    elif choice == num and num == 42 and intent == 1:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("Congratulations, you got it first try!!!")
        break
    elif choice == num and intent == 1:
        print("Congratulations, you got it first try!!!")
        break
    elif choice == num and intent > 1:
        print("Congratulations, you've got it!")
        print("You won in {} attempts!".format(intent))
        break
    intent += 1