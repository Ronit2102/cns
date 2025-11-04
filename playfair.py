# PLAYFAIR CIPHER

def generate_matrix(key):
    key = key.replace("j", "i").lower()
    key_unique = ""
    used = set()

    # remove duplicates from key
    for i in key:
        if i not in used and i.isalpha():
            used.add(i)
            key_unique += i

    # fill remaining alphabets (no 'j')
    alpha = [chr(i) for i in range(97, 123) if chr(i) != 'j']
    for i in alpha:
        if i not in used:
            key_unique += i

    # create 5x5 matrix
    matrix = [list(key_unique[i:i+5]) for i in range(0, 25, 5)]
    return matrix


def find_position(matrix, char):
    if char == 'j':
        char = 'i'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return [i, j]
    return None


def prepare_text(plaintext):
    plaintext = plaintext.lower().replace(" ", "").replace("j", "i")
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'x'
        if a == b:
            pairs.append(a + 'x')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    if len(pairs[-1]) == 1:
        pairs[-1] += 'x'
    return pairs


def encrypt_playfair(plaintext, matrix):
    digraphs = prepare_text(plaintext)
    cipher = ""
    for d in digraphs:
        a, b = d[0], d[1]
        locA = find_position(matrix, a)
        locB = find_position(matrix, b)
        if locA[0] == locB[0]:  # same row
            cipher += matrix[locA[0]][(locA[1] + 1) % 5]
            cipher += matrix[locB[0]][(locB[1] + 1) % 5]
        elif locA[1] == locB[1]:  # same column
            cipher += matrix[(locA[0] + 1) % 5][locA[1]]
            cipher += matrix[(locB[0] + 1) % 5][locB[1]]
        else:  # rectangle rule
            cipher += matrix[locA[0]][locB[1]]
            cipher += matrix[locB[0]][locA[1]]
    return cipher


def decrypt_playfair(cipher, matrix):
    plaintext = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        locA = find_position(matrix, a)
        locB = find_position(matrix, b)
        if locA[0] == locB[0]:  # same row
            plaintext += matrix[locA[0]][(locA[1] - 1) % 5]
            plaintext += matrix[locB[0]][(locB[1] - 1) % 5]
        elif locA[1] == locB[1]:  # same column
            plaintext += matrix[(locA[0] - 1) % 5][locA[1]]
            plaintext += matrix[(locB[0] - 1) % 5][locB[1]]
        else:  # rectangle rule
            plaintext += matrix[locA[0]][locB[1]]
            plaintext += matrix[locB[0]][locA[1]]
    return plaintext


# ---------------- MAIN PROGRAM ----------------
plaintext = input("Enter plaintext: ").lower()
key = input("Enter key: ").lower()

matrix = generate_matrix(key)
print("\nPlayfair Key Matrix:")
for row in matrix:
    print(row)

cipher = encrypt_playfair(plaintext, matrix)
print("\nCiphertext:", cipher)

decrypted = decrypt_playfair(cipher, matrix)
print("Decrypted Text:", decrypted)
