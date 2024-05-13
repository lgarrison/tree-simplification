from collections import defaultdict

import numpy as np

def simplify_tree_iterative(desc: dict[int, int], progs: dict[int, set[int]]):
    """Replace nodes that only have one descendant and one progenitor
    with an edge, using an iterative algorithm.
    """

    for hid in list(desc.values()):
        if hid not in desc:
            continue
        d = desc[hid]
        # automatically have 1 descendent by virtue of being in desc
        if len(progs.get(hid,[])) == 1:
            p = progs[hid].pop()
            desc[p] = d
            progs[d].remove(hid)
            progs[d].add(p)
            
            del desc[hid], progs[hid]


def print_tree(desc, progs):
    print('Desc representation:')
    for h, d in desc.items():
        print(f"{h} -> {d}")

    print('\nProg representation:')
    for h, ps in progs.items():
        print(f"{ps} -> {h}")


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

    hid = rng.permutation(Nh)*1000 + 1
    desc = np.roll(hid, -1)
    desc[-1] = -1
    desc[0] = desc[1]

    shuf = rng.permutation(Nh)
    hid = hid[shuf]
    desc = desc[shuf]

    # Represent the tree as two dicts:
    # - desc[hid]: the descendant of hid
    # - progs[hid]: the list of progenitors of hid
    desc = {h: d for h, d in zip(hid, desc) if d != -1}
    progs = defaultdict(set)
    for h, d in desc.items():
        progs[d].add(h)
    progs = dict(progs)

    print_tree(desc, progs)

    simplify_tree_iterative(desc, progs)

    print()
    print_tree(desc, progs)


main()
