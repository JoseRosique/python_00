# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 18:24:59 by joslopez          #+#    #+#              #
#    Updated: 2023/04/12 16:06:49 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = "The right format"

total_length = 42
padding_length = total_length - len(kata)

output_string = kata.rjust(total_length, '-')

print(output_string, end="")