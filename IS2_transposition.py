def encrypt(plaintext, key):
    # Create the ciphertext variable
    ciphertext = ''
    # Create the matrix with the plaintext
    matrix = []
    for i in range(0, len(plaintext), key):
        matrix.append(plaintext[i:i+key])
    # Transpose the matrix
    transposed_matrix = []
    for i in range(key):
        transposed_matrix.append('')
        for j in range(len(matrix)):
            try:
                transposed_matrix[i] += matrix[j][i]
            except IndexError:
                transposed_matrix[i] += ' '
    # Read the ciphertext from the transposed matrix
    for row in transposed_matrix:
        ciphertext += row
    return ciphertext

def decrypt(ciphertext, key):
    # Create the plaintext variable
    plaintext = ''
    # Calculate the number of columns in the transposed matrix
    num_cols = len(ciphertext) // key
    # Create the matrix with the ciphertext
    matrix = []
    for i in range(0, len(ciphertext), num_cols):
        matrix.append(ciphertext[i:i+num_cols])
    # Transpose the matrix
    transposed_matrix = []
    for i in range(num_cols):
        transposed_matrix.append('')
        for j in range(len(matrix)):
            try:
                transposed_matrix[i] += matrix[j][i]
            except IndexError:
                transposed_matrix[i] += ' '
    # Read the plaintext from the transposed matrix
    for row in transposed_matrix:
        plaintext += row
    return plaintext.strip()

# Example usage
plaintext = 'Hello,World!'
key = 3
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)
print(f'Plaintext: {plaintext}')
print(f'Encrypted ciphertext: {ciphertext}')
print(f'Decrypted plaintext: {decrypted_plaintext}')