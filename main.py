from PIL import Image
import pywhatkit as kt

true_path = input("-------------------------------------------"
                  "\n[ # example: /Users/leva/Desktop/nori.jpg ]"
                  "\n[ enter your path and file name:          ]"
                  "\n-------------------------------------------\n>>> ")

start = input("------------------------------------------"
              "\n[ type '1' to see the result in terminal ]"
              "\n[ type '2' to get result in txt file     ]"
              "\n------------------------------------------\n>>> ")

if start == '1':

    ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

    def scale_image(image, new_width=100):
        (original_width, original_height) = image.size
        aspect_ratio = original_height/float(original_width)
        new_height = int(aspect_ratio * new_width)
        new_image = image.resize((new_width, new_height))
        return new_image

    def convert_to_grayscale(image):
        return image.convert("L")

    def map_pixels_to_ascii(image, range_width=25):
        pixels = image.getdata()
        ascii_str = ""
        for pixel_value in pixels:
            ascii_str += ASCII_CHARS[pixel_value//range_width]
        return ascii_str

    def convert_image_to_ascii(image_path, new_width=100):
        try:
            image = Image.open(image_path)
        except Exception as e:
            print(e)
            return

        image = scale_image(image)
        image = convert_to_grayscale(image)

        pixels = map_pixels_to_ascii(image)
        len_pixels = len(pixels)

        ascii_image = ""
        for i in range(0, len_pixels, new_width):
            ascii_image += pixels[i:i+new_width] + "\n"

        return ascii_image

    def main():
        image_path = f"{true_path}"

        new_width = 100
        ascii_image = convert_image_to_ascii(image_path, new_width)
        print("------------------------------------------")
        print(ascii_image)
        print("------------------------------------------"
              "\nthis is all, thank you!")

    if __name__ == "__main__":
        main()

elif start == '2':

    def convert_image_to_ascii_and_save(image_path, output_file_path="o"
                                        "utput_ascii_art.png"):
        kt.image_to_ascii_art(image_path, output_file_path)
    convert_image_to_ascii_and_save(f"{true_path}",
                                    output_file_path="output_ascii_art.png")
    print("------------------------------------------"
          "\nthis is all, thank you!")

else:

    print('\nnothing here')
    exit()
