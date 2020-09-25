'''
    EXO 3
'''

# 1
for i in range(1, 21):
    print(' ', end='')
    print(7*i, end='')
    if 7*i%3==0:
        print('*', end='')
print('')

# 2
for i in range(1, 51):
    if 13*i%7==0:
        print(13*i, '', end='')
print('')

# 3
v = '0'
vals = []
while True:
    v = input('v['+str(len(vals))+'] = ')
    if v=='':
        break
    vals.append(int(v))
if len(vals)>0:
    print('Max = ', max(vals))
    print('Min = ', min(vals))

# 4
n = int(input('Donnez n : '))
s = 0
for i in range(0, n+1):
    s += i
print('Somme =', s)

# 5
x = int(input('Donnez x : '))
n = int(input('Donnez n : '))
print(str(x)+'^'+str(n)+' = '+str(x**n))

# 6
case = int(input('Case : '))
print('Nombre de grains est :', 2**(case-1))
s = 0
for i in range(1, 65):
    s += 2**(i-1)
print('Total =', s)

# 7
taux = 1.5
i = 1
while i<16385:
    print(i, 'euros =', i*taux, 'dollars')
    i *= 2

# 8
import random
n = int(input('N : '))
for i in range(0, n):
    print(random.randint(1, 6), '', end='')
print('')

# 9
s = 'Une chaine pour le test de compteur'
n = 0
c = input('Le caracter a compter : ')
for i in s:
    if i==c:
        n += 1
print('Count =', n)