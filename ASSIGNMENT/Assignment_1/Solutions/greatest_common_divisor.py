def find_GCD(a, b):
    if b==0:
        return a
    return find_GCD(b, a % b)

x, y = map(int, input("Enter 2 positive integers: ").split())
GCD = find_GCD(x, y)
print(f'The greatest common divisor of {x} and {y} is {GCD}')