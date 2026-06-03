#print vs return:print just shows the human user output in a console.
#return is used to terminate function and gives back a value from the function
'''def a(a,b):
    print(a+b)
a(2,3)'''
'''def cal(a,b):
    return a+b
print(cal(2,3))'''
'''def add(a,b):
    c=a-b
    d=a+b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return(c)
    return(d)
    return(e)
print(add(2,3))'''

'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return(c)
    #return(d)
    #return(e)
print(add(2,3))'''
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    return(c,d,e)
    
print(add(2,3))'''
#key word and positional arguments
'''def de(id,name,phone):
    id=78
    name="sreshta"
    phone=6472676768
    print(id,name,phone)
de(id="id",name="name",phone="phone")'''
'''def de(id,name,phone):
    print(id,name,phone)
de(id="id",name="name",phone="phone")
de(id="40",name="sreshta",phone=6889754456)
de(id="67",name="uuhh",phone=6778898)
de(id="76", name="hhuhu",phone="7766766554\n")
de(45,"sreshta",667473487)
de(id=87,name="sreshta",phone=787873874)'''
#default arguments:
'''def grocery(item,price):
    print("item is%s" %item)
    print("price is %.2f"%price)
grocery("rice",3000)'''
'''def grocery(item="sugar",price=600):
    print("item is %s" %item)
    print("price is %.2f"%price)
grocery()'''
'''def grocery(item="sugar",price):
    print("item is %s" %item)
    print("price is %.2f"%price)
grocery(300)#error'''
'''def grocery(item,price=900):
    print("item is %s" %item)
    print("price is %.2f"%price)
grocery("paste")'''
'''def grocery(item="cake",price=600,qty=42):
    print("item is %s" %item)
    print("price is %.f"%price)
    print("qty is %.f"%qty)
grocery()'''
#* is used to unpack the elements
'''a=[1,2,3,4,5]
print(a)
print(*a)'''
'''a=(1,2,3,4,5)
print(a)
print(*a)'''
'''a={1,2,3,4,5}
print(a)
print(*a)'''
'''a="codegnan"

print(*a)'''
'''a={"name":"sreshta","year":2006}
print(*a)'''

'''a,b,c=1,2,3,4,5
print(a)
print(b)
print(c)'''#error
'''*a,b,c=1,2,3,4,5
print(*a)
print(b)
print(c)'''
'''*a,*b,*c=1,2,3,4,5
print(*a)
print(*b)
print(*c)#error'''
'''a,b,c="codegnan"
print(a)
print(b)
print(c)#error'''
'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''

'''def cal():
    a=int(input())
    b=int(input())
    op=input("sum,sub,mul")
    if op=="sum":
        print(a+b)
    elif op=="mul":
        print(a*b)
    elif op=="sub":
        print(a-b)
    else:
        print("Invalid option")
cal()'''
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while 1:
    a=int(input())
    b=int(input())
    op=input("sub,sum,mul")
    if op=="sum":
        add()
    elif op=="sub":
        sub()
    elif op=="mul":
        mul()
    else:
        print("Invalid")
add()
mul()
sub()'''
'''def splitbill():
    members=int(input())
    ammount=int(input())
    c=ammount//members
    print(f"per head{c}")
splitbill()'''

'''def splitbill():
    members=int(input())
    ammount=int(input())
    c=ammount//members
    print("per head {}".format(c))
splitbill()'''
#variable length arguments are automatically stores in tuple and we use star arguments
'''def check(*s):
    print(s)
    print(type(s))
check()
check(2,3,4,5,6,7)
b=[5,6,7,8]
check(*b)
c={7,8,9,9}
check(*c)
d={"name":"srehta","city":"vij"}
check(*d)'''

'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5)
check1(3,4,5,6,7)
check1(3,4,5,6.7,7.9,"pooja")'''
#max
'''print(max(1,2,3,4,45))
print(min(1,2,3,4,8))
#print(sum(3,4))error'''
'''a=2,3,5,6
print(sum(a))'''

'''a=2,3,5,6
b=5,6,7
print(sum(a))
print(sum(b))'''
#marks analysis report
a=int(input())
for i in range(a):
    print("studens{i}")
    b=int(input())









