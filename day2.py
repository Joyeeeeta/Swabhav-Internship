#task 1: variables & data types
a=25 
b=5.18
c="joyeeta"
d=True

print(f"integer:{a}, type:{type(a)}")
print(f"float:{b}, type:{type(b)}")
print(f"string:{c}, type:{type(c)}")
print(f"boolean:{d}, type:{type(d)}\n")


#task 2: string manipulation
x="Python programming is fun!"
a=x.upper()
print("uppercase:",a)

b=x.replace("fun", "powerful")
print("replaced text:",b)

c=x[9:20]
print("sliced text:",c)

print("length:",len(x))


#task 3: lists and loops
y=[2, 4, 6, 8, 10] 
print("list:",y)

for num in y:
    print(num)

i=0
total=0
while i < len(y):
    total+=y[i]
    i+=1

print("sum:",total)


#task 4: conditional
try:
    age=int(input("age:"))
    if age >=18:
        print("adult")

    else:
        print("not adult")

except ValueError:
    print("invalid")


#task 5: functions
def area (a,b):
    return a*b
print("area1", area(7,5))
print("area2", (2.5, 3.8))


#task 6: dictionaries
students= {"Joyeeta":85, "Harsh":92, "Pranav":89}

students["Ishan"]=82
students["Joyeeta"]=98

print(students)


#task 7: file handling
f=open("student.txt", "w")
f.write("Joyeeta, Harsh, Pranav, Ishan, Nishi")
f.close()

f=open("student.txt","r")
content=f.read()
print("content:",content)
f.close()


#task 8: error handling 
try:
    a=float(input("numerator:"))
    b=float(input("denominator:"))
    c=a/b
    print("result",c)

except ZeroDivisionError:
    print("error:")

except Exception:
    print("unexpected error", Exception)        
