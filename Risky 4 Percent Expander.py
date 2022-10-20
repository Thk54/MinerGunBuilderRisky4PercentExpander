from collections import Counter
# Pluto Plutonium Round
# 1,1,1,2.25,2.25
# 1x3
# 2.25x2
# 
# Risky Risky 4 Percent
# 0,1,1,1,1,1,1,1,1,1,2,3,4
# 0x1
# 1x9
# 2x1
# 3x1
# 4x1
PLUTO = Counter([1,1,1,2.25,2.25])
RISKY = Counter([0,1,1,1,1,1,1,1,1,1,2,3,4]) #Unskilled
#RISKY = Counter([0,0,1,1,1,1,2,2,3,3,4]) #First Skill
#RISKY = Counter([0,0,0.85,0.85,0.85,0.85,1.7,1.7,2.55,2.55,3.4,0,0,0.85,0.85,0.85,0.85,1.7,1.7,2.55,2.55,3.4,0.85,0.85,0.85,0.85,1.7,1.7,2.55,2.55,3.4]) #Both Skill
options = Counter([1])
#options = Counter([1,0,3,0])

"""testing = RISKY + PLUTO
for test in testing:
    print(test*2)
#    print(testing[test])"""

def RiskyItem(options):
    tmp = Counter()
    for opt in options.items():
        for risk in RISKY.elements():
            tmp += Counter({(opt[0]*risk):opt[1]})
    return tmp

def PlutoItem(options):
    tmp = Counter()
    for opt in options.items():
        for plut in PLUTO.elements():
            tmp += Counter({(opt[0]*plut):opt[1]})
    return tmp

outputfile = input('Enter output File: ')
riskyCount = int(input('Enter number of Risky 4 Percent: '))
plutoCount = int(input('Enter number of Plutonium Round: '))

#for x in range(plutoCount):
#    options = PlutoItem(options)
for x in range(riskyCount):
    options = RiskyItem(options)
    print(x)
for x in range(plutoCount):
    options = PlutoItem(options)
    print(x)
unique = sorted(list(options.keys()))
mean = 0
for opt in options.items():
    mean += opt[0]*opt[1]
mean /= options.total()
with open(outputfile, 'w') as f:
    f.write(f'Risky 4 Percent Count: {riskyCount}\n')
    f.write(f'Plutonium Round Count: {plutoCount}\n')
    for key in unique:
        f.write(f'{key} x {options[key]} - % of total options: {options[key]/options.total()*100}\n')
    f.write(f'Total Possiblities: {options.total()}\n')
    f.write(f'Arithmetic Mean: {mean}\n')
    #print(Counter(options))
#print(options)
#zzzzzergy = input('Return to end')
#print(f'Sum of {a} and {b} is {sum(a, b)}')
#    with open(filename, 'w') as f:
#        f.writelines([','.join([items[x],str(prices[x]),str(quantities[x])])+"\n" for x in range(len(items))])