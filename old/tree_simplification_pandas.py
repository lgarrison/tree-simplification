import numpy as np
import pandas as pd


def simplify_tree_iterative(df):
    """Replace nodes that only have one descendant and one progenitor
    with an edge, using an iterative algorithm.
    """
    
    return df


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

    df = pd.DataFrame({'hid': hid, 'desc': desc})
    df['desc'] = df['desc'].astype('Int64')  # use nullable int type
    df.set_index('hid', inplace=True)

    print(df)

    newdf = simplify_tree_iterative(df)

    print(newdf)


main()
