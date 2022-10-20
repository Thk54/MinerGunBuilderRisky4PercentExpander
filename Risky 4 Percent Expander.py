from collections import Counter
# Plut Plutonium Round
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
PLUT = [1,1,1,2.25,2.25]
RISKY = [0,1,1,1,1,1,1,1,1,1,2,3,4]
options = [1]

def RiskyItem(options):
    tmp = []
    for opt in options:
        tmp.extend([opt*risk for risk in RISKY])
    print(tmp)
    return tmp

riskyCount = int(input('Enter number of Risky 4 Percent: '))
#b = int(input('Enter 2nd number: '))

for x in range(riskyCount):
    options = RiskyItem(options)
unique = list(set(options))
unique.sort()
for numb in unique:
    print(f'{numb} x {options.count(numb)}')
#print(options)
zzzzzergy = input('Return to end')
#print(f'Sum of {a} and {b} is {sum(a, b)}')