n=[1,2,3]
def square(n):
    return n*n

mapping=map(square,n)
mapping=list(mapping)
print(mapping)