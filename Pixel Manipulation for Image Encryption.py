from PIL import Image
import numpy as np
import sys

def encrypt_image(image_path, key, output_path):
    """
    Encrypts the image by adding a key to every pixel value.
   
    Args:
        image_path (str): Path to the original image.
        key (int): The integer key to add to each pixel.
        output_path (str): Where to save the encrypted image.
    """
    # Open the image and convert it to a NumPy array for easier manipulation.
    img = Image.open(image_path)
    data = np.array(img, dtype=np.uint8)
   
    # Add the key to each pixel. We use modulo 256 to ensure values wrap around correctly.
    encrypted_data = (data + key) % 256
   
    # Convert the manipulated array back into an image and save it.
    encrypted_img = Image.fromarray(encrypted_data)
    encrypted_img.save(output_path)
    print(f"Encryption complete! Encrypted image saved as '{output_path}'.")

def decrypt_image(image_path, key, output_path):
    """
    Decrypts the image by subtracting the key from every pixel value.
   
    Args:
        image_path (str): Path to the encrypted image.
        key (int): The integer key to subtract from each pixel.
        output_path (str): Where to save the decrypted image.
    """
    # Open the encrypted image and convert to a NumPy array.
    img = Image.open(image_path)
    data = np.array(img, dtype=np.uint8)
   
    # Subtract the key from each pixel. Again, modulo 256 ensures correct wrap-around.
    decrypted_data = (data - key) % 256
   
    # Convert back to image and save.
    decrypted_img = Image.fromarray(decrypted_data)
    decrypted_img.save(output_path)
    print(f"Decryption complete! Decrypted image saved as '{output_path}'.")

if __name__ == '__main__':
    # This script can be run from the command line.
    # Example usage: python image_encryptor.py encrypt input.jpg encrypted.jpg 50
    if len(sys.argv) != 5:
        print("Usage: python image_encryptor.py [encrypt/decrypt] input_image output_image key")
        sys.exit(1)
   
    mode = sys.argv[1].lower()          # 'encrypt' or 'decrypt'
    input_image = sys.argv[2]           # Input image file path
    output_image = sys.argv[3]          # Output image file path
    try:
        key = int(sys.argv[4])          # The key must be an integer
    except ValueError:
        print("Error: The key must be an integer.")
        sys.exit(1)
   
    if mode == "encrypt":
        encrypt_image(input_image, key, output_image)
    elif mode == "decrypt":
        decrypt_image(input_image, output_image, key)
    else:
        print("Invalid mode. Choose 'encrypt' or 'decrypt'.")    