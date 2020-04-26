from Car import *

# สร้าง Object/Instance ของ Class car
objCar1 = Car('red', 'Toyota', 4, 4, 180)
objCar1.printData()

print()

objCar2 = Car()
objCar2.setColor('Blue')
objCar2.setBrand('Honda')
objCar2.setMaxSpeed('160')
objCar2.printData()
