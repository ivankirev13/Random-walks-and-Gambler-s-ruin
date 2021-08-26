# Random-walks-and-Gambler-s-ruin

There are three main folders: Gambler's ruin, 2D random walk and 3D random walk. The following is a description for each:

## Gambler's ruin problem

In the gamblers_ruin.py file we create a simulation of the problem and plot a visualization of the entire game. In the second file, we compare the theoretical results described below with the results from our simulation.

### The Problem

The problem is as such: Consider a gambler with an initial fortune i and at each turn the gambler has

- probability p of winning 1 unit
- probability q = 1-p of losing 1 unit

What is the probability that if the gambler starts with i units, he reaches N before reaching 0?

### Theoretical Result

If we denote $h_i$ to be the probability that the gambler reaches N before 0, then in theory we have that if p is not equal to 0.5
$$h_i = \frac{1 - (q/p)^i}{1 - (q/p)^N}$$
and if p = 0.5, then
$$h_i = \frac{i}{N}$$

## 2D Random walk

There are 3 files. The random_walk_2D_grid.py file creates a simulation of a 2D random walk where on each step we can only move to a neighbor on the grid.

The random_walk_2D_grid_animation.py file is once again a simulation on a grid, but this time we create an animation of the process.

The random_walk_2D_animation.py creates an animation of a simulation of a 2D random walk, where we can move on an arbitraty point in the plane within radius one of the previous point.

## 3D Random walk

There are 3 files. The random_walk_3D_grid.py file creates a simulation of a 3D random walk where on each step we can only move to a neighbor on the grid.

The random_walk_3D_grid_animation.py file is once again a simulation on a grid, but this time we create an animation of the process.

The random_walk_3D_animation.py creates an animation of a simulation of a 3D random walk, where we can move on an arbitraty point in the plane within radius one of the previous point.
