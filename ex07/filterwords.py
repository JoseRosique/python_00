# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 10:41:27 by joslopez          #+#    #+#              #
#    Updated: 2023/04/13 11:13:32 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if (len(sys.argv) == 3):
    try:
        length = int(sys.argv[2])
    except ValueError:
        print("ERROR")
        sys.exit()
elif (len(sys.argv) < 3):
    print("ERROR")
    sys.exit()
elif (len(sys.argv) > 3):
    print("ERROR")
    sys.exit()
    
s = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
s = s.split()

w = [item for item in s if len(item) >= length]
print(w)