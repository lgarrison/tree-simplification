from timeit import default_timer

import numpy as np
import numba as nb


@nb.njit
def simplify_tree_iterative(desc, nprog):
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


def main(Nh=10**6):
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
    desc_arr = np.roll(hid, -1)
    desc_arr[-1] = -1
    desc_arr[0] = desc_arr[1]

    # Represent the tree as two dicts:
    # - desc[hid]: the descendant of hid
    # - nprog[hid]: the number of progenitors
    desc = nb.typed.Dict.empty(key_type=nb.int64, value_type=nb.int64)
    for h, d in zip(hid, desc_arr):
        if d != -1:
            desc[h] = d

    nprog = nb.typed.Dict.empty(key_type=nb.int64, value_type=nb.int64)
    for d in desc.values():
        if d in nprog:
            nprog[d] += 1
        else:
            nprog[d] = 1

    if Nh <= 100:
        print_tree(desc, nprog)

    simplify_tree_iterative(desc.copy(), nprog.copy())

    t = -default_timer()
    simplify_tree_iterative(desc, nprog)
    t += default_timer()

    if Nh <= 100:
        print()
        print_tree(desc, nprog)

    print(f"Time: {t:.3g} sec, {Nh/1e6/t:.3g} M node / sec")


main()
