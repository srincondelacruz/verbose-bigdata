
# Problem: Generate a dictionary containing (i, i*i) for i from 1 up to n.
n = int(input("numero"))
result_dict = {i: i * i for i in range(1, n + 1)}
print(result_dict)


# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
try:
    n = int(input("Escribe un numero "))
except ValueError:
    print("error")
    raise SystemExit(1)

def factorial(num):
    if num < 0:
        raise ValueError("n debe ser no negativo")
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

try:
    print(factorial(n))
except ValueError:
    print("error")