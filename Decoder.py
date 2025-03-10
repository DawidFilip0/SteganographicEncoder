import cv2

class Decoder:

    def __init__(self):
        pass

    def set_image_path(self,image_path):
        p = image_path.split('.')
        if len(p) < 2 or p[-1].lower() != "png":
            raise ValueError("Invalid file format: Expected a .png file")
        self.image = cv2.imread(image_path)

    def decode(self):
        image = self.image
        output = ""
        eight_block = []
        for line in image:
                for pixel in line:
                    eight_block.append(pixel)
                    if len(eight_block) == 8:
                        letter = self.read_letter(eight_block)
                        if letter == "/":
                            return output
                        else:
                            output += letter
                        eight_block.clear()

    def read_letter(self,eight_block):
            bin_string = ""
            for pixel in eight_block:
                p  = pixel[0].item()
                if p % 2 == 0:
                    bin_string += "0"
                else:
                    bin_string += "1"

            num = int(bin_string,2)
            return chr(num)
