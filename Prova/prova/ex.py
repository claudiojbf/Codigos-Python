a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("\033[1;35m#1")
print(a[1:10])
print(" :) "*20)
print("#2")
print(a[8:14])
print(" :) "*20)
print("#3")
print(a[0:16:2])
print(" :) "*20)
print("#4")
print(a[1:16:2])
print(" :) "*20)
print("#5")
print(a[0:16:2])
print(a[0:16:3])
print(a[0:16:4])
print(" :) "*20)
print("#6")
a.reverse()
print(a)
print(" :) "*20)
print("#7")
a.reverse()
print(f"{sum(a[10:16]) / sum(a[3:10]):.2f}")





