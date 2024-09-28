import Object_Building 

class Church(Object_Building.Building):
    def __init__(self, address, length, width, height, tower_height):
        Object_Building.Building.__init__(self, address ,length ,width ,height)
        self.tower_height = tower_height

    def calc_volume(self):
        building_vol = super().calc_volume()
        tower_base_area = self.widthy*self.widthy
        return building_vol + tower_base_area*self.tower_height

x = Church("apa",10,20,40,25)

print(x)
print("-----")
print(x.calc_volume())