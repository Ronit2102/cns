from math import gcd
plaintext = int(input("Enter The Plaintext: "))
p = int(input("Enter The Number p: "))
q = int(input("Enter The Number q: "))
n = p * q
totient = (p - 1) * (q - 1)
e = 3
while gcd(e, totient) != 1:
 e += 2
def modInverse(a, m):
 for d in range(2, m):
 if (a * d) % m == 1:
 return d
 return None
d = modInverse(e, totient)
print()
print("p:", p, "q:", q, "n:", n, "totient:", totient, "e:", e, "d:", d)
print()
cipher = (plaintext ** e) % n
plain = (cipher ** d) % n
print("Ciphertext:", cipher)
print("Decrypted:", plain)
