a = [1, 2, 3, 4, 5]
# a.append(6)
print(a)
b = len(a)
for i in range(b//2):
    a[i], a[-i-1] = a[-i-1], a[i]

print(a)