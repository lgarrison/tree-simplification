# tree-simplification
Lehman Garrison (@lgarrison)

Some exploration of halo tree simplification implementations. A pure-Python implementation is in `tree_simplification.py`, with a Numba version in `tree_simplification_numba.py`.

On my desktop, simplifying a (dummy) tree with $10^6$ nodes using the Python version takes 1.5 seconds. The numba version takes 0.5 seconds.
