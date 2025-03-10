import cv2


class Encoder:
    def __init__(self):
        pass


    def set_image_path(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def set_output_path(self, output_path):
        p = output_path.split('.')
        if len(p) < 2 or p[-1].lower() != "png":
            raise ValueError("Invalid file format: Output must be .png file")
        self.output_path = output_path

    def encode(self,message):
        bin_str = self.convert_to_binary_string(message)

        string_counter = 0
        for line in self.image:
            for pixel in line:
                self.replace_pixel(pixel,bin_str[string_counter])
                string_counter += 1
                if string_counter >= len(bin_str):
                    cv2.imwrite(self.output_path,self.image)
                    return

    def replace_pixel(self,pixel,binary_value):
        if pixel[0] % 2 ==  0 and binary_value == '1':
            pixel[0] += 1
        if pixel[0] % 2 == 1 and binary_value == '0':
            pixel[0] -= 1

    def convert_to_binary_string(self, message):
        message += '/'
        return ''.join(format(ord(char), '08b') for char in message)

