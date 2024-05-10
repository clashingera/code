import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("n (prime number) = "))
g = int(input("g (primitive root modulo n) = "))

if not (is_prime(n) and is_prime(g)):
    print("Invalid input. Both n and g must be prime numbers.")
    exit()

x = int(input("No. selected by Alice: "))
y = int(input("No. selected by Bob: "))

A = pow(g, x, n)
B = pow(g, y, n)

print("\nA =", A)
print("B =", B)

k1 = pow(B, x, n)
k2 = pow(A, y, n)

print("\nk1 =", k1)
print("k2 =", k2)

if k1 == k2:
    print("Algorithm is correct")
else:
    print("Algorithm is wrong")