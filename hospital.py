
class Rooms:
    normalRooms = 50
    oxygenRooms = 50
    icu = 50
        
class Beds:
    flatBeds = 80
    reclinerBeds = 100

class Equipments:
    ventilator = 16
    oxygenCylinder = 110
    normalMasks = 200
    nonRebreatherMasks = 120


class roomAlloter(Rooms, Beds, Equipments):
    def remainingAvailability(self):
        if Rooms.normalRooms == 0:
            Rooms.normalRooms = "N/A"
        if Rooms.oxygenRooms == 0:
            Rooms.oxygenRooms = "N/A"
        if Rooms.icu == 0:
            Rooms.icu = "N/A"
        print("Remaining Availability:")
        print("Normal Rooms: ",Rooms.normalRooms)
        print("Oxygen Rooms: ", Rooms.oxygenRooms)
        print("ICU: ", Rooms.icu)
        
        
    def normalRoom(self):
        if Rooms.normalRooms != "N/A" and Beds.flatBeds >= 1 and Equipments.normalMasks >= 2:
            Beds.flatBeds -= 1
            Equipments.normalMasks -= 2
            Rooms.normalRooms -= 1
            print("01 Normal room(with 1 flat bed + 2 normal masks) reserved.")
        else:
            print("Sorry, no rooms could be reserved.")
        print(self.remainingAvailability())

    def oxygenRoom(self):
        if Rooms.oxygenRooms != "N/A" and Beds.reclinerBeds >= 1 and Equipments.oxygenCylinder >= 2 and Equipments.nonRebreatherMasks >= 2:
            Beds.reclinerBeds -= 1
            Equipments.oxygenCylinder -= 2
            Equipments.nonRebreatherMasks -= 2
            Rooms.oxygenRooms -= 1
            print("01 Oxygen room (2 oxygen cylinder + 1 recliner bed + 2 non rebreather masks) reserved.")
        else:
            print("Sorry, no rooms could be reserved.")
        print(self.remainingAvailability())



    def icuRoom(self):
        if Equipments.ventilator >= 1 and Beds.reclinerBeds >= 1 and Rooms.icu != "N/A" and Equipments.oxygenCylinder >= 1:
            Beds.reclinerBeds -= 1
            Equipments.ventilator -= 1
            Equipments.oxygenCylinder -= 1
            Rooms.icu -= 1
            print("01 ICU room (with 1 ventilator + 1 oxygen cylinder + 1 recliner bed) reserved.")
        else:
            print("Sorry, no rooms could be reserved.")
            Rooms.icu = "N/A"
        print(self.remainingAvailability())

    def room(self, roomType):
        if roomType == "Normal Room":
            self.normalRoom()
        elif roomType == "Oxygen Room":
            self.oxygenRoom()
        else:
            self.icuRoom()



while True:
    print("Please enter the type of room you want to reserve:")
    roomType = input()
    checkRoom = roomAlloter()
    checkRoom.room(roomType)

