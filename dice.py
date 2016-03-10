import random
import collections

def pause():
    raw_input("Press any key to continue")


sidesa = int(raw_input("How many sides on the first die? "))
sidesb = int(raw_input("How many sides on the second die? "))
rolls = int(raw_input("How many times do you want to roll? "))
results = []
statsa = {}
statsb = {}
resab = {}

for i in range(1, sidesa + 1):
    statsa[i] = (0)
	
for i in range(1, sidesb + 1):
    statsb[i] = 0
	
for i in range(1, sidesa + 1):
    for j in range(1, sidesb + 1):
        resab[(i, j)] = 0
		

pause()

while rolls > 0:
    resulta = random.randint(1, sidesa)
    resultb = random.randint(1, sidesb)
    data = str((resulta, resultb))
    results.append((resulta, resultb))
    statsa[resulta] += 1
    statsb[resultb] += 1
#    resab[data] += 1
    rolls -= 1

	
print results

for res in results:
    resab[res] += 1

pause()

for res in resab:
    if resab[res] != 0:
        print res, resab[res]

print "----------------------------------------------"

pause()

od = collections.OrderedDict(sorted(resab.items()))

for k, v in od.items():
    if v != 0:
        print k, v