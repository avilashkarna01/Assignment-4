print("Question1")
t=(1,2,3,4,5)
print(len(t))
print("\n")


print("Question2")
t=(1,5,7,8,9)
print(max(t))
print("\n")
t=(7,5,3,2,0)
print(min(t))
print("\n")


print("Question3")
t=(1,5,4,7,6)
u=1
for b in range(0,5):
     k=t[b]
     u=k*u
print(u)
print("\n")


print("Question4")
l=[0,0,0,0]
l[0]=input("enter first element")
l[1]=input("enter second element")
l[2]=input("enter third element")	
l[3]=input("enter third element")

l1=[0,0,0,0]
l1[0]=input("enter third element")
l1[1]=input("enter third element")
l1[2]=input("enter third element")
l1[3]=input("enter third element")

s1=set(l)
s2=set(l1)
print(s1)
print(s2)
print(s1-s2)
print("\n")

l=[0,0,0,0]
l[0]=input("enter first element")
l[2]=input("enter third element")
l[1]=input("enter second element")
l[3]=input("enter third element")

l1=[0,0,0,0]
l1[0]=input("enter third element")
l1[1]=input("enter third element")
l1[2]=input("enter third element")
l1[3]=input("enter third element")
 
s1=set(l)
s2=set(l1)
print(s1)
print(s2)
print(s1&s2)
print("\n")


print("question5")
d={}
name=""
marks=""
l=[]
for a in range(10):
	name=input("enter a name:")
	marks=int(input("enter a marks"))
	l.append(marks)
	d[name]=marks
print(d)
print(l)
l.sort()
print(l)
print("\n")

print("Question6")
l=["M","I","S","S","I","S","S","I","P","P","I"]
a=l.count('m')
b=l.count('I')
c=l.count('S')
e=l.count('P')
d={}
d["M"]=a
d["I"]=b
d["S"]=c
d["P"]=e
print(d)

  


