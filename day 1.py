print("increasing triangle")
n=5
for i in range (1, n+1):
    print("* " * i)
print()

print("decreasing triangle")
n=5
for i in range (n, 0, -1):
    print("* " * i)
print()

print("hill pattern")
n=9
for i in range (n):
    print(" " * (n-i-1) + "* " * (i+1))
print()

print("reverse hill pattern")
n=9
for i in range (n, 0, -1):
    print(" " * (n-i) + "* " * i)
print()
