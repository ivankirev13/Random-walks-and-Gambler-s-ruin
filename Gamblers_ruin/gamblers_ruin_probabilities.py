import numpy as np # noqa


def gamblers_ruin_outcome(probability,
                          win_prize=1,
                          loss=1,
                          initial_money=15,
                          fortune=30,
                          ruin=0):
    """Return 1 if the gambler succeeds and -1 if he is ruined."""
    # record the amount of money during each game in a list
    money = [initial_money]
    while money[-1] < fortune and money[-1] > ruin:
        if np.random.random() <= probability:
            money.append(money[-1] + win_prize)
        else:
            money.append(money[-1] - loss)
    if money[-1] >= fortune:
        return 1
    elif money[-1] <= ruin:
        return -1


p = 0.55
number_of_successes = 0
number_of_ruins = 0
for i in range(1000):
    outcome = gamblers_ruin_outcome(p)
    if outcome == 1:
        number_of_successes += 1
    elif outcome == -1:
        number_of_ruins += 1
print(number_of_successes)
print(number_of_ruins)
