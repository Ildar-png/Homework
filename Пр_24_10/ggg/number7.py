a = 0
b = int(input())
c = int(input())
while c!=0:
    if c>b:
        a+=1
    b = c
    c = int(input())
print(a)