from PIL import Image

# Function to convert text to binary
def text_to_binary(text):
    binary_message = ' '.join(format(ord(char), '08b') for char in text)
    return binary_message

# Function to hide the binary message in an image
def encode_image(img_path, message):
    # Open the image
    img = Image.open(img_path)
    width, height = img.size

    binary_message = text_to_binary(message)
    message_length = len(binary_message)

    if message_length > width * height * 3:
        raise ValueError("Message is too long to be encoded in this image.")

    binary_message += '1111111111111110'  # Adding a termination marker

    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))

            for color_channel in range(3):
                if data_index < message_length:
                    pixel[color_channel] = int(bin(pixel[color_channel])[2:9] + binary_message[data_index], 2)
                    data_index += 1

            img.putpixel((x, y), tuple(pixel))

            if data_index == message_length:
                break

    img.save("encoded.png")

def decode(encoded_img_path):
    img = Image.open(encoded_img_path, 'r')
    data = ''
    imgdata = iter(img.getdata())

    termination_marker = '1111111111111110'  # The termination marker to stop decoding

    while True:
        try:
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]]

            binstr = ""

            if data[-16:] == termination_marker:
                break
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))

            # Check if the termination marker is found
        except StopIteration:
            break

    return data



# Main menu
def main():
    while True:
        choice = input("Choose an option:\n1. Encode a message into an image\n2. Decode a message from an image\n3. Exit\n")

        if choice == '1':
            img_path = input("Enter the path to the image: ")
            message = input("Enter the message to hide: ")
            encode_image(img_path, message)
            print("Message encoded successfully.")
        elif choice == '2':
            encoded_img_path = input("Enter the path to the encoded image: ")
            decoded_message = decode(encoded_img_path)
            print("Decoded message: " + decoded_message)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()
