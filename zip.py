n={1,2,3}
o={4,5,6}

x=zip(n,o)
y=list(x)
print(y)

a=[1,2,3]
b=[9,8,7]
z=zip(a,b)
p=set(z)
print(p)

list1=[1,2,3,4]
list2=[100,200,300,400]

list3=list2[::-1]

for i,g in zip(list1,list3):
    print(i,g)