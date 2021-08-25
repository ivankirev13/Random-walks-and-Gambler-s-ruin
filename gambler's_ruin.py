import numpy as np # noqa
import matplotlib.pyplot as plt


def gamblers_ruin(probability,
                  number_of_games,
                  win_prize=1,
                  loss=1,
                  initial_money=50,
                  fortune=100,
                  ruin=0):
    """Return a plot of simulation of the game."""
    # record the amount of money during each game in a list
    money = np.zeros(number_of_games)
    money[0] = initial_money
    # simulate random number between 0 and 1
    random_numbers = np.random.random(number_of_games)
    for i in range(1, number_of_games):
        if random_numbers[i] < probability:
            money[i] = money[i-1] + win_prize
        else:
            money[i] = money[i-1] - loss
    # if we reach fortune or ruin, our money stays the same
    for i in range(len(money)):
        if money[i] >= fortune:
            money[i:] = fortune
            break
        elif money[i] <= ruin:
            money[i:] = ruin
            break

    plt.title(f"Gambler's ruin with p={probability}, "
              f"initial money={initial_money}")
    plt.plot(money)


# Visualization
number_of_simulations = 10
for i in range(number_of_simulations):
    gamblers_ruin(probability=0.4,
                  number_of_games=500,
                  win_prize=1,
                  loss=1,
                  initial_money=50,
                  fortune=100)
plt.show()
