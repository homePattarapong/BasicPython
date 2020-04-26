# # import ทั้งหมดทุกฟังก์ชันใน Module
# import module_numbers as numbers

# # เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

# #import บางฟังก์ชัน
# from module_numbers import factorial,fibonacci
# from module_numbers import * #ทุกฟังก์ชัน
# print(factorial(5))
# print(fibonacci(120))

from module_numbers import factorial as fa, fibonacci as fi  # เปลี่ยนชื่อฟังก์ชัน
print(fa(5))
print(fi(120))
