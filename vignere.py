plaintext = input("Enter the plaintext: ").lower().replace(" ", "")
key = input("Enter the key: ").lower()

# Extend key to match plaintext length
newKey = ""
while len(newKey) < len(plaintext):
    newKey += key
finalKey = newKey[:len(plaintext)]

# Alphabets to numbers
alpha = {chr(i + 97): i for i in range(26)}
nums = {i: chr(i + 97) for i in range(26)}

# Encryption
cipher = ""
for i in range(len(plaintext)):
    cipher += nums[(alpha[plaintext[i]] + alpha[finalKey[i]]) % 26]

print("Ciphertext:", cipher)
