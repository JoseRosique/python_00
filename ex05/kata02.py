# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 18:14:13 by joslopez          #+#    #+#              #
#    Updated: 2023/04/11 18:22:05 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime

kata = (2019, 9, 25, 3, 30)

kata_date = datetime.datetime(*kata)

formatted_data = kata_date.strftime("%m/%d/%Y %H:%M")

print(formatted_data)