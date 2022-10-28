from NearestPerfectSquare import nearest_perfect_square

nearest_n9 = nearest_perfect_square(-9)
assert (nearest_n9 == 0)
print("The Nearest perfect square less than -9 is ", nearest_perfect_square(-9), "The correct answer should be 0")
nearest_12 = nearest_perfect_square(12)
assert (nearest_12 == 9)
print("The Nearest perfect square less than 12 is ", nearest_perfect_square(12), "The correct answer should be 9")
nearest_0 = nearest_perfect_square(0)
assert (nearest_0 == 0)
print("The Nearest perfect square less than 0 is ", nearest_perfect_square(0), "The correct answer should be 0")
nearest_1 = nearest_perfect_square(1)
assert (nearest_1 == 1)
print("The Nearest perfect square less than 1 is ", nearest_perfect_square(1), "The correct answer should be 1")

print("File bad_test01 is set to: {}", __name__)