a = [1,2,3,4,5,6,7,8,9,10]
b = [i**2 if i%2==0 else i for i in a]
print(b)