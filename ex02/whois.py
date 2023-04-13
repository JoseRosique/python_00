# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:08:39 by joslopez          #+#    #+#              #
#    Updated: 2023/04/12 16:31:43 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


counter = 0

for item in sys.argv[1:]:
    counter += 1

if counter == 0:
    exit()

if counter >= 2:
    print("AssertionError: more than one argument are provided")
    exit()

try:
    number = int(sys.argv[1])
except ValueError:
        print("AssertionError: argument is not an integer")
        exit()

if number == 0:
    print("I'm Zero")
elif number % 2 == 0:
    print("I'm Even")
else:
    print("I`m Odd")
    