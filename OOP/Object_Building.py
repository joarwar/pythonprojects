class Building:
    def __init__(self, address, length, width, height):
        self.addy = address
        self.lengthy = length
        self.widthy = width
        self.heighty = height
        self.volume = length * width * height

    def calc_volume(self):
        return self.lengthy * self.widthy * self.heighty


    def __str__(self):
        return f"address: {self.addy} \nlength: {self.lengthy} \nwidth:{self.widthy} \nheight:{self.heighty} \nvolume:{self.volume}"
def main():
    length_input = int(input("length "))
    width_input = int(input("width "))
    height_input = int(input("height "))
    building1 = Building("GataJoar",length_input,width_input,height_input)

if __name__ == '__main__':
    main()
#print(building1)
