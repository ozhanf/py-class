data=[50.3,338.4,626.5,959.4,1317.9,1716.7,2134.3,2565.5,3085.6,3626.7]
d=[]
d=data
duration=[]
b=0
p=[]
s=0
t1=int(input("enter t1:"))
t2=int(input("enter t2:"))
for i in data:
    p.append(round(i-b,1))
    if b<=t1:
        duration.append("S")
    elif b>=t1 and b<t2:
        duration.append("M")
    else:
        duration.append("L")
    b=i
print(duration[1::])
