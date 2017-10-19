import random

y = int(input("Number of cards: "))
print y
numberset = []
for x in range (0,y):
    numberset.append(x/2)
numberset1 = numberset
numberoftriesneeded = []
for x in range (0,1000000):
    numberset1 = list(numberset)
    numberofsteps = 0
    knownnumbers = []
    while numberset1:
        draw = random.choice(numberset1)
        numberset1.remove(draw)
        if draw in knownnumbers:
            knownnumbers.remove(draw)
        else:
            knownnumbers.append(draw)
            draw2 = random.choice(numberset1)
            numberset1.remove(draw2)
            if draw2 == draw:
                knownnumbers.remove(draw)
            elif draw2 in knownnumbers:
                knownnumbers.remove(draw2)
                numberofsteps = numberofsteps + 1
            else:
                knownnumbers.append(draw2)
                numberofsteps = numberofsteps + 1

    numberoftriesneeded.append(numberofsteps)

if 0 in numberoftriesneeded:
    print "ZERO"
expectation = sum(numberoftriesneeded)/float(len(numberoftriesneeded))
print expectation
 
