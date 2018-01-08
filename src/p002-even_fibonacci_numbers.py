s = 0
a = 1
b = 2

while b < 4000000:
    if b % 2 == 0: s += b
    t = b
    b = a + b
    a = t

print(s)


