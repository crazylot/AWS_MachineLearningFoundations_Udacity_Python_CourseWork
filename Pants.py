print("File one __name__ is set to: {}", __name__)

class Pants :

    def __int__(self, size , length , width , color , brand):
        self.size = size
        self.length = length
        self.width = width
        self.color = color
        self.brand = brand

    def get_size(self):
        return self.size

    def set_price(self, size):
        self.size = size

