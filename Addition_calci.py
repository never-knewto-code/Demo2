from tracemalloc import stop


def sum(q, p):
    return q + p

print("Welcome")
while True:
    print("Please enter Your Nos.")
    num1 = float(input("1st No."))
    num2 = float(input("2nd No."))
    print( num1, "+", num2, "=", sum(num1, num2))
    