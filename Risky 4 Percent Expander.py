from collections import Counter
# Pluto Plutonium Round
# 1,1,1,2.25,2.25
# 1x3
# 2.25x2
# 
# Risky Risky 4 Percent (Unskilled)
# 0,1,1,1,1,1,1,1,1,1,2,3,4
# 0x1
# 1x9
# 2x1
# 3x1
# 4x1
FOURP = Counter({1:24,10:1})
THERM = Counter({1:11,2.6:9})
DUBBL = Counter({1:67,2:33})
PLUTO = Counter({1:3,2.25:2})
RISKY = Counter({0:1,1:9,2:1,3:1,4:1}) #Unskilled
#RISKY = Counter({0:2,1:4,2:2,3:2,4:1}) #First Skill
#RISKY = Counter({0:4,0.85:12,1.7:6,2.55:6,3.4:3}) #Both Skill
options = Counter([1])


def RiskyItem(options):
    tmp = Counter()
    for opt in options.items():
        for risk in RISKY.items():
            tmp += Counter({(opt[0]*risk[0]):(opt[1]*risk[1])})
    return tmp

def PlutoItem(options):
    tmp = Counter()
    for opt in options.items():
        for plut in PLUTO.items():
            tmp += Counter({(opt[0]*plut[0]):(opt[1]*plut[1])})
    return tmp

def ThermItem(options):
    tmp = Counter()
    for opt in options.items():
        for elec in THERM.items():
            tmp += Counter({(opt[0]*elec[0]):(opt[1]*elec[1])})
    return tmp

def DubblItem(options):
    tmp = Counter()
    for opt in options.items():
        for dubb in DUBBL.items():
            tmp += Counter({(opt[0]*dubb[0]):(opt[1]*dubb[1])})
    return tmp

def WriteOutput(outputBase):
    unique = sorted(list(options.keys()))
    mean = 0
    for opt in options.items():
        mean += opt[0]*opt[1]
    mean /= options.total()
    with open(outputBase, 'w') as f:
        if riskyCount > 0:
            f.write(f'Risky 4 Percent Count: {riskyCount}\n')
        if plutoCount > 0: 
            f.write(f'Plutonium Round Count: {plutoCount}\n')
        if thermCount > 0: 
            f.write(f'Thermite/Charged Round Count: {thermCount}\n')
        if dubblCount > 0: 
            f.write(f'33 Percent Count: {dubblCount}\n')
        f.write(f'Total Possiblities: {options.total()}\n')
        f.write(f'Arithmetic Mean: {mean}\n')
        for key in unique:
            f.write(f'{key} x {options[key]} - % of total options: {options[key]/options.total()*100}\n')

outputFile = input('Enter output File: ')
riskyCount = int(input('Enter number of Risky 4 Percent: '))
plutoCount = int(input('Enter number of Plutonium Round: '))
thermCount = int(input('Enter number of Thermite/Charged Round: '))
dubblCount = int(input('Enter number of 33 Percent: '))

if riskyCount > 0:
    print('risky')
    for x in range(riskyCount):
        options = RiskyItem(options)
        print(x+1)
if plutoCount > 0:
    print('pluto')
    for x in range(plutoCount):
        options = PlutoItem(options)
        print(x+1)
if thermCount > 0:
    print('therm')
    for x in range(thermCount):
        options = ThermItem(options)
        print(x+1)
if dubblCount > 0:
    print('dubbl')
    for x in range(dubblCount):
        options = DubblItem(options)
        print(x+1)
WriteOutput(outputFile)
input('End.')