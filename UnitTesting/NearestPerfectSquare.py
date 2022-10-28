def nearest_perfect_square(num):
    n = 0
    while (n + 1) ** 2 <= num:
        n = n + 1
    return n ** 2


print("File NearestPerfectSquare is set to: {}", __name__)
