a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[1:10])
print("-"*20)
print(a[8:14])
print("-"*20)
print(a[::2])
print("-"*20)
print(a[1::2])
print("-"*20)
print(a[0::2])
print(a[0::3])
print(a[0::4])
print("-"*20)
a.reverse()
print(a)
a.reverse()
print("-"*20)
i1 = sum(a[10:])
i2 = sum(a[3:10])
r = float(i1/i2)
print(f"{r:.2f}")
