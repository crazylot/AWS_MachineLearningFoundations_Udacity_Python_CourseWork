from NearestPerfectSquare import nearest_perfect_square


def test_nearest_n9():
    assert (nearest_perfect_square(-9) == 0)


def test_nearest_0():
    assert (nearest_perfect_square(0) == 0)


def test_nearest_1():
    assert (nearest_perfect_square(1) == 1)


def test_nearest_12():
    assert (nearest_perfect_square(12) == 9)
