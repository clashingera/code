import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_e(m):
    for i in range(2, m):
        if gcd(i, m) == 1:
            return i
    return None

def find_d(e, m):
    for i in range(1, m):
        if (e * i) % m == 1:
            return i
    return None

def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

def main():
    message_str = input("Enter the message to be encrypted: ")
    message = [ord(c) for c in message_str]

    p = 7
    q = 17
    n = p * q
    m = (p - 1) * (q - 1)
    e = find_e(m)
    if e is None:
        print("No suitable 'e' found")
        return
    d = find_d(e, m)
    if d is None:
        print("No suitable 'd' found")
        return
    print("Public key (n, e):", (n, e))
    print("Private key (n, d):", (n, d))
    ciphertext = [encrypt(m, e, n) for m in message]
    print("Encrypted Message:", ciphertext)
    decrypted_message = ''.join([chr(decrypt(c, d, n)) for c in ciphertext])
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()