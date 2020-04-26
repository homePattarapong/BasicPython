class Car:
    # Properties
    color = ""
    brand = ""
    number_of_wheels = 4
    number_of_seats = 4
    maxspeed = 0

    # Constructor กำหนดค่าเริ่มต้นของ Class
    def __init__(self, _color="", _brand="", _number_of_wheels="", _number_of_seats="", _maxspeed=""):
        self.color = _color
        self.brand = _brand
        self.number_of_wheels = _number_of_wheels
        self.number_of_seats = _number_of_seats
        self.maxspeed = _maxspeed

    # Create method set color
    def setColor(self, x):
        self.color = x

    def setBrand(self, x):
        self.brand = x

    def setMaxSpeed(self, x):
        self.maxspeed = x

    def printData(self):
        print("Color of this car is ", self.color)
        print("Brand of this car is ", self.brand)
        print("Max speed of this car is ", self.maxspeed)

    # Deconstructor
    def __del__(self):
        print()
