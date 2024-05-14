# tree-simplification
Lehman Garrison (@lgarrison)

Some exploration of halo tree simplification implementations (replacing nodes of degree 2 with an edge). `tree_simplification.py` is a pure-Python implementation, and `tree_simplification_numba.py` is accelerated with Numba.

On my workstation, simplifying a (dummy) tree with $10^6$ nodes using the Python version takes 1.5 seconds. The numba version takes 0.5 seconds.

The problem is very similar to [Day 23](https://adventofcode.com/2023/day/23) in last year's Advent of Code!
