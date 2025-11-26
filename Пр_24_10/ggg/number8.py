a = 0
b = 0
c = int(input())
while c!=0:
    if c>a:
        b=a
        a=c
    elif c>b and c!=a:
        b = c
    c = int(input())
print(b)