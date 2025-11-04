# PRODUCT CIPHER: Substitution + Transposition

plaintext = input("Enter plaintext: ").lower().replace(" ", "")
key = int(input("Enter numeric key (e.g., 3): "))

# Padding to make 16 characters
while len(plaintext) < 16:
    plaintext += "z"

alphaToNum = {chr(i + 97): i for i in range(26)}
numToAlpha = {i: chr(i + 97) for i in range(26)}

# 1️⃣ Substitution (Caesar cipher)
cipher1 = ""
for i in plaintext:
    cipher1 += numToAlpha[(alphaToNum[i] + key) % 26]

# 2️⃣ Transposition (4x4 matrix column-wise)
matrix = [list(cipher1[i:i+4]) for i in range(0, 16, 4)]
cipher2 = "".join([matrix[r][c] for c in range(4) for r in range(4)])

print("\nSubstitution Cipher:", cipher1)
print("After Transposition (Final Cipher):", cipher2)

# 3️⃣ Decryption
# Reverse Transposition
rev_matrix = [[''] * 4 for _ in range(4)]
k = 0
for c in range(4):
    for r in range(4):
        rev_matrix[r][c] = cipher2[k]
        k += 1
plain_order = "".join(["".join(row) for row in rev_matrix])

# Reverse Substitution
result = ""
for i in plain_order:
    temp = (alphaToNum[i] - key) % 26
    result += numToAlpha[temp]

print("\nDecrypted Text:", result)
