x=float(input("Number1"))
if x % 2 == 0:
    print(x, "is a Even")
else:
    print(x, "is a odd")
count = 0
n1, n2 = 0, 1
while count < x:
    print(n1)
    x1= n1 + n2
    n1=n2
    n2=x1
    count = count + 1
a='c'
print(ord(a))
print(chr(99))