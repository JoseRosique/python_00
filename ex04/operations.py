# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:36:22 by joslopez          #+#    #+#              #
#    Updated: 2023/04/13 12:37:38 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) <= 2:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
    exit()
elif len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    exit()

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    print("Error: argument must be an integer")
    exit()

a = int(sys.argv[1])
b = int(sys.argv[2])


sum = a + b
print(f"Sum: {sum}")

difference = a - b
print(f"Difference: {difference}")

product = a * b
print(f"Product: {product}")

if b != 0:
    quiotient = a / b
    print(f"Quotient: {quiotient}")
else:
    print("Quotient: ERROR (division by zero)")

if b != 0:
    remainder = a % b
    print(f"Remainder: {remainder}")
else:
    print("Remainder: ERROR (modulo by zero)")