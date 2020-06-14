'''
From Facebook group: '>implying we can discuss mathematics', by Ben Crossley, 13/06/2020

Simple game, can’t figure out this probability.

Coin toss: Heads = +1, Tails =-1. 3rd consecutive head onwards is worth +2. Consecutive tails is always -1.

E.g. H,H,H,H,T,T,T,T,T,H,H,T,H

is worth: +1,+1,+2,+2,-1,-1,-1,-1,-1,+1,+1,-1,+1
with an overall score of +3.

For what p(heads) is the long term expected value 0?
'''


import random
import numpy as np


def get_p_head(p_head):
    score = 0
    coin_tosses = (random.choices(population=['H', 'T'], weights=[p_head, 1 - p_head], k=10000))

    for i in range(0, 2):
        if coin_tosses[i] == 'H':
            score += 1
        else:
            score -= 1

    for i in range(2, len(coin_tosses)):
        if coin_tosses[i] == coin_tosses[i-1] == coin_tosses[i-2] and coin_tosses[i] == 'H':
            score += 2
        elif coin_tosses[i] == 'H':
            score += 1
        else:
            score -= 1

    return score


experimental_p_head = np.NaN
min_score = np.inf

for x in np.arange(0.44, 0.46, 0.00001):
    x = round(x, 5)
    curr_score = get_p_head(x)
    if np.abs(curr_score) < np.abs(min_score):
        min_score = curr_score
        min_p_head = x


print("P('H') with expected value 0 is: " + str(min_p_head))
