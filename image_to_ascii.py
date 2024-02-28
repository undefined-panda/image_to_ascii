"""
Takes a image and replaces every pixel with an ascii charachter by checking its brightness factor.
"""
from PIL import Image

def convert_to_ascii(image_path, ascii_path, scale, type):
    img = Image.open(image_path)
    width, height = img.size

    img.resize((width//scale, height//scale)).save("resized."+type)

    img = Image.open("resized."+type)
    img = img.convert('L')
    width, height = img.size

    ascii_img = []
    for i in range(height):
        ascii_img.append(["X"] * width)

    ascii_chars = "@%#*+=-:. "
    for y in range(height):
        for x in range(width):
            brightness = img.getpixel((x, y)) / 255.0
            ascii_index = int(brightness * (len(ascii_chars) - 1))
            ascii_img[y][x] = ascii_chars[ascii_index]
    
    file = open(ascii_path, "w")
    for row in ascii_img:
        file.write(''.join(row)+"\n")
    
    file.close()


if __name__ == "__main__":
    image = "Luffi.jpg"
    type = image[-3:]
    ascii = "image[:-4].txt"
    scale = 1
    convert_to_ascii(image, ascii, scale, type)