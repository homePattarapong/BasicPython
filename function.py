# การสร้างฟังก์ชัน แบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# การสร้างฟังก์ชัน แบบมีการ return value
def area(width, height):
    total = width*height
    return total


# เรียกใช้งานฟังก์ชัน hello()
hello("Pattarapong")

# เรียกใช้งานฟังก์ชัน
print(area(5, 8))
print(area(15, 7.5))


# ฟังก์ชันแบบมีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Name: {salary}")
    print(f"Name: {lang}")


# เรียกใช้งานฟังก์ชัน show_info()
show_info()
print()
show_info('Pattarapong Th.', 20000, 'X++')
