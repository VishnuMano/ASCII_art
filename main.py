from PIL import Image, ImageOps

# Opening and Grayscaling Input Image
im = Image.open("monalisa.jpeg")
print(im.format, im.size, im.mode)
print(im.getpixel((0,0)))
im_grayscale = ImageOps.grayscale(im)
print(im_grayscale.getpixel((0,0)))
width, height = im_grayscale.size
im_grayscale.show()


# Opening File
output_file = open("output.txt", "w")

# Iterate Through Pixels and Print Corresponding ASCII Character to File
for y in range(0, height):
    for x in range(0, width):
        pixel_brightness = im_grayscale.getpixel((x, y))
        if pixel_brightness <= 29:
            output_file.write("@")
        elif pixel_brightness <= 57:
            output_file.write("#")
        elif pixel_brightness <= 85:
            output_file.write("*")
        elif pixel_brightness <= 114:
            output_file.write("=")
        elif pixel_brightness <= 142:
            output_file.write("-")
        elif pixel_brightness <= 170:
            output_file.write(":")
        elif pixel_brightness <= 199:
            output_file.write(",")
        elif pixel_brightness <= 227:
            output_file.write(".")
        elif pixel_brightness <= 255:
            output_file.write(" ")
    output_file.write("\n") # Create New Line as Y-Coordinate Increases

output_file.close()