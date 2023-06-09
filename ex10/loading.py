# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: joslopez <joslopez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 13:56:57 by joslopez          #+#    #+#              #
#    Updated: 2023/04/13 15:53:49 by joslopez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

def ft_progress(lst):
    length = len(lst)
    start_time = time.time()
    eta = 0
        
    for i, item in enumerate(lst):
        
        t = time.time() - start_time
        percent_complete = (i + 1) * 100 / length
        
        filled_slots = int(percent_complete / 5)
        empty_slots = 20 - filled_slots
        elapsed_time = time.time() - start_time
        eta = (elapsed_time / (percent_complete / 100.0))
        
        progress_bar = "[" + "=" * filled_slots + ">" + " " * empty_slots + "]"
        
        
        sys.stdout.write("\rETA: {:.2f}s [{:0.2f}%] {} ({}/{}) | elapsed time {:.2f}s".format(eta, percent_complete,
            progress_bar, i+1, length, elapsed_time))
        sys.stdout.flush()
        yield item

if __name__ == "__main__":
    lst = range(-98765464987984874, 0)
    ret = 0
    for elem in ft_progress(lst):
        ret += elem
        time.sleep(0.005)
    print()
    print("...")
    print(ret)
