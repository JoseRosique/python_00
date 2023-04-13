# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 18:07:43 by joslopez          #+#    #+#              #
#    Updated: 2023/04/11 18:24:11 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for language, creator in kata.items():
    print(f"{language} was created by {creator}")