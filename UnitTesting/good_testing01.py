from NearestPerfectSquare import nearest_perfect_square


def nearest_n9():
    assert (nearest_perfect_square(-9) == 0)


def nearest_0():
    assert (nearest_perfect_square(0) == 0)


def nearest_1():
    assert (nearest_perfect_square(1) == 1)


def nearest_12():
    assert (nearest_perfect_square(12) == 9)
