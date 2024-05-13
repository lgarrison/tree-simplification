from collections import defaultdict
from timeit import default_timer

import numpy as np


def simplify_tree_iterative(desc: dict[int, int], nprog: dict[int, int]):
    """Replace nodes that only have one descendant and one progenitor
    with an edge, using an iterative algorithm.
    """

    dirty = True
    while dirty:
        dirty = False
        for hid in set(desc):
            if hid not in desc:
                continue
            d = desc[hid]
            if nprog.get(d, 0) == 1 and d in desc:
                desc[hid] = desc[d]
                del desc[d], nprog[d]
                dirty = True


def print_tree(desc, nprog):
    print("Tree:")
    for h, d in desc.items():
        print(f"{h} -> {d}")

    print()
    print("Num progenitors:")
    for h, p in nprog.items():
        print(f"{h}: {p} prog")


def main(Nh=10**1):
    rng = np.random.default_rng(123)

    # Make a tree that looks like:
    # o  o
    #  \/
    #  o
    #  |
    #  o
    #  : [long chain]
    #  o

    hid = rng.permutation(Nh) * 1000 + 1
    desc = np.roll(hid, -1)
    desc[-1] = -1
    desc[0] = desc[1]

    # Represent the tree as two dicts:
    # - desc[hid]: the descendant of hid
    # - nprog[hid]: the number of progenitors
    desc = {h: d for h, d in zip(hid, desc) if d != -1}
    nprog = defaultdict(int)
    for d in desc.values():
        nprog[d] += 1

    if Nh <= 100:
        print_tree(desc, nprog)

    t = -default_timer()
    simplify_tree_iterative(desc, nprog)
    t += default_timer()

    if Nh <= 100:
        print()
        print_tree(desc, nprog)

    print(f"Time: {t:.3g} sec, {Nh/1e6/t:.3g} M node / sec")


main()
