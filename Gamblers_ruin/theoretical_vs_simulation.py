import numpy as np # noqa
import matplotlib.pyplot as plt


def gamblers_ruin_outcome(probability,
                          win_prize=1,
                          loss=1,
                          initial_money=15,
                          fortune=30,
                          ruin=0):
    """Return 1 if the gambler succeeds and -1 if he is ruined."""
    money = [initial_money]
    while money[-1] < fortune and money[-1] > ruin:
        if np.random.random() <= probability:
            money.append(money[-1] + win_prize)
        else:
            money.append(money[-1] - loss)
    if money[-1] == fortune:
        return 1
    elif money[-1] == ruin:
        return 0


def simulation_probability(probability,
                           initial_money,
                           fortune,
                           number_of_simulations=1000):
    """Return the proportion of successful outcomes from a simulation."""
    number_of_successes = 0
    number_of_ruins = 0
    for t in range(number_of_simulations):
        outcome = gamblers_ruin_outcome(probability,
                                        initial_money=initial_money,
                                        fortune=fortune)
        if outcome == 1:
            number_of_successes += 1
        elif outcome == 0:
            number_of_ruins += 1
    return number_of_successes/number_of_simulations


def theoretical_probability(probability, initial_money, fortune):
    """Return the theoretical probability of successful gameplay."""
    if probability == 0.5:
        return initial_money/fortune
    else:
        p = probability
        q = 1 - probability
        return (1-(q/p)**initial_money)/(1-(q/p)**fortune)


# Compare theoretical results with simulation
probabilities = np.linspace(0.1, 1, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 7.5))
# plot theoretical probabilities of winning
for p in probabilities:
    ax1.scatter(p,
                theoretical_probability(probability=p,
                                        initial_money=10,
                                        fortune=20),
                color="C0")
ax1.title.set_text("Theoretical probability of gaining fortune")
ax1.set_xlabel("Probability p of winning each turn")

# plot simulation proportion of gaining fortune for different p
for p in probabilities:
    ax2.scatter(p,
                simulation_probability(probability=p,
                                       initial_money=10,
                                       fortune=20),
                color="C1")
ax2.title.set_text("Simulated probability of gaining fortune for different p")
ax2.set_xlabel("Probability p of winning each turn")
plt.show()
