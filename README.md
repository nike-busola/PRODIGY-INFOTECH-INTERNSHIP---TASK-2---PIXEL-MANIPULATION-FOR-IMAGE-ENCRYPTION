Encrypting an Image: The encrypt_image function takes an image, converts it into a numerical array, and then adds a number (the key) to every pixel. It wraps around with modulo 256 so that if any pixel value goes above 255, it loops back to the start. This “scrambles” the image data, creating an encrypted version.

Decrypting an Image: The decrypt_image function does the opposite: it subtracts the same key from every pixel. Again, modulo 256 is used to handle any wrap-around, so you get back the original image if you use the correct key.

Command-Line Magic: The script is meant to be run from the command line. You provide four arguments:
The mode (encrypt or decrypt).
The path to the input image.
The path where you want the output saved.
And the key (an integer) used for encryption or decryption.

It even checks if you’ve provided the right number of arguments and whether the key is a valid integer.

