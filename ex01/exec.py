# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:12:35 by joslopez          #+#    #+#              #
#    Updated: 2023/04/13 12:57:12 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
    string = " ".join(sys.argv[1:])
    print(''.join(reversed(string.swapcase())))