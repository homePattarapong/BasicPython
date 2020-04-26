# i = 1
# while i <= 10:
#     if i == 10:
#         print(i)
#     else:
#         print(i, end=',')
#     i = i+1

# a = 1
# while a < 100:
#     print(a)
#     a = a+1

b = 1
while True:
    print(b, end=' ')
    if(b % 10 == 0):
        print(end='\n')
    b = b+1

    if(b == 101):
        break
print()
i = 1
while i <= 100:
    if i % 10 == 0:
        print(i)
    else:
        print(i, end=" ")
    i = i+1
