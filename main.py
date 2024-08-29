import numpy as np


def d20(n):
    return np.random.randint(1, 21, (n,))

if __name__ == "__main__":
    print(d20(10))
