# 1
for a in range(151):
    print(a)
# 2
for b in range(0, 1000, 5):
    print(b)
# 3 
for c in range(1, 100, 1):
    if c % 10 == 0:
        c = ("Coding Dojo")
    elif c % 5 == 0:
        c = ("Coding")
    print(c)
# 4 
sum = 0
for d in range (1, 500000, 2):
    sum = sum + d
print(sum)
# 5 
for e in range (2018, 0, -4):
    print (e)
# 6 
lowNum = 2
highNum = 9
mult = 3
for z in range(lowNum, highNum+1, 1):
    if z % mult == 0:
        print(z)
