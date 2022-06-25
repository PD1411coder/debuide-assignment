
class Equipments:
    # ventilator = 16
    # oxygenCylinder = 110
    # normalMasks = 200
    # nonRebreatherMasks = 120
    def __init__(self, property):
        self.property = property

class Ventilator(Equipments):
    def __init__(self, property):
        super().__init__(property)

        