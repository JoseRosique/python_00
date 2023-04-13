# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:53:41 by joslopez          #+#    #+#              #
#    Updated: 2023/04/12 18:39:13 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer (text=''):
    
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    
    if not isinstance(text, str):
        print("Error: argument is not a string")
        return
    
    if text == '':
        text = input("What is the text to analyze? \n")
    
    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0
    
    for string in text:
    
        if string.isupper():
            upper_count += 1
        elif string.islower():
            lower_count += 1
        elif string.isspace():
            space_count += 1
        elif string.isascii() and not string.isnumeric():
            punct_count += 1
            
    print(f"The text contains {len(text)} character(s)")
    print(f"{upper_count} upper letters(s)")
    print(f"{lower_count} lower letter(s)")
    print(f"{punct_count} punctuation mark(s)")
    print(f"{space_count} space(s)")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Error: too many arguments. Usage: python3 count.py 'text'")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    elif len(sys.argv) < 2:
        text_analyzer('')