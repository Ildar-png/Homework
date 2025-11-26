a = 0
b = 0
c = int(input())
while c!=0:
    if c>a:
        a = c
        b = 1
    elif c==a:
        b+=1 
    c = int(input())
print(b)
