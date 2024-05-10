import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        # Hash the provided key using SHA-256 algorithm to generate a 32-byte key
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        # Pad the plain text to match the block size
        plain_text = self.__pad(plain_text)
        # Generate a random IV (Initialization Vector)
        iv = Random.new().read(self.block_size)
        # Create AES cipher in CBC (Cipher Block Chaining) mode
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Encrypt the plain text and prepend the IV to the ciphertext
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        # Decode the base64 encoded encrypted text
        encrypted_text = b64decode(encrypted_text)
        # Extract the IV from the encrypted text
        iv = encrypted_text[:self.block_size]
        # Create AES cipher in CBC (Cipher Block Chaining) mode with the IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Decrypt the encrypted text and remove the padding
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        # Calculate the number of bytes needed for padding
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        # Create a padding string with ASCII character representing the number of bytes to pad
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        # Append the padding to the plain text
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        # Extract the last character which represents the padding size
        last_character = plain_text[len(plain_text) - 1:]
        # Remove the padding from the plain text
        return plain_text[:-ord(last_character)]

# Example usage
def main():
    key = "mysecretpassword"  # This is the secret key
    message = "Hello, world!"  # This is the message to be encrypted
    # Create an instance of AESCipher with the secret key
    cipher = AESCipher(key)
    # Encrypt the message
    encrypted_text = cipher.encrypt(message)
    print("Encrypted text:", encrypted_text)
    # Decrypt the encrypted text
    decrypted_text = cipher.decrypt(encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
