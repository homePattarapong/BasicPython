scores = {
    'john': 1200,
    'bobby': 2000,
    'janny': 4200
}

print(scores)
print(scores['bobby'])

# เพิ่มสมาชิกใหม่เข้า dictionary

scores['roger'] = 3200

print(scores)

# การสร้าง dictionary ว่าง
points = {}

# เพิ่มค่าเข้า dictionary ว่าง
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

# การ loop อ่านสมาชิกของ Dictionary ออกมา

# สร้างตัวแปรรับทั้ง key, Value
for k, v in scores.items():
    print(k, v)
