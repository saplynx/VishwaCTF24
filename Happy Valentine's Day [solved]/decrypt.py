from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i ^ j for i, j in zip(a, cycle(b))]

# Read the encrypted file
enc = open('enc.txt', 'rb').read()

# Read the key from the original encrypted image
# key = [enc[0], enc[1], enc[2], enc[3], enc[4], enc[5], enc[6], enc[7]]
key = [ 137, 80, 78, 71, 13, 10, 26, 10]

# Decrypt the image
decrypted_data = bytearray(xor(enc, key))

# Save the decrypted image
with open('decrypted_image.png', 'wb') as f:
    f.write(decrypted_data)
