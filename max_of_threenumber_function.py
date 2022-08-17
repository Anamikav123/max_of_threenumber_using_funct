def max_of_three(a):
    return a
sum=max_of_three(1)
print(sum)
print("-------------------------------------------------")
def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
sum=max_of_three(8,7,6)
print(sum)
print("-------------------------------------------------")
def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("enter first number:" ))
b=int(input("enter second number:" ))
c=int(input("enter third number:" ))
sum=max_of_three(a,b,c)
print(sum)


