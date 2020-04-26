a = 3
b = 4.92
c = "itgenius"

print(a)
print(b)
print(c)

b += 1
b -= 1

# การสร้างตัวแปรหลายตัวในบรรทัดเดียวกัน
x = y = z = 10
print(x, y, z)

j, k = 5, 15
print(j, k)

# Boolean
status = True
msg = False
print(status, msg)

# ตัวแปรแสดงผลร่วมกับข้อความ
# solution 1 (concat string)
print("ราคาขายต่อชิ้น", b, "บาท มีจำนวน", a, "ชิ้น")

# solution 2 (string interpolation)
#print("ราคาขายต่อชิ้น %.2f บาท" % b)
# การนี้ใส่ตัวแปรมากกว่า 1
print("ราคาขายต่อชิ้น %.2f บาท มีจำนวน %d ชิ้น" % (b, a))
# กรณีใส่ Type ผิด จะแสดงตาม Type ที่นำมาแสดง
#print("ราคาขายต่อชิ้น %f บาท" % a)

# solution 3 (format string)
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
