#pyramid

"""x = 0
while x <= 10:
    itera = x
    x += 1
    print
    for i in range(1, itera):
        print i,
        itera += 1
print 
print

o=0
while o <= 10:
    tick = o
    o += 1
    scale =[]
    print
    for p in range(1, tick):
       print p,
       tick += 1
       if p > 1:
           scale.append(p)
           for q in scale:
               print q,"""

for i in range(10):
    for j in range(10 - i):
        print' ',
    for j in range(1, i + 1):
        print j,
    for j in range(i-1, 0, -1):
        print j,
    print

for i in range(10):
    for j in range(i+2):
        print ' ',
    for j in  range(1, 9-i):
        print j,
    for j in range(7 - i, 0, -1):
        print j,
    print    
"""q=10
space = 0
while q >= 0:
    tick = q
    q -= 1
    space += 1
    print
    for s in range(0, space):
        print' ',
    for r in range(1, tick):
       print r,
       tick -= 1
o=0
while o <= 10:
    tick = o
    o += 1
    print
    for p in range(0, tick):
       print p,
       tick += 1"""

for i in range(55):
    if i >= 10:
        for j in range(i+2):
            print i,
