'''
    EXO 2
'''
# 1
n1 = input('Donnez n1 : ')
if '.' not in n1:
    n1 += '.0'
n2 = input('Donnez n2 : ')
if '.' not in n2:
    n2 += '.0'
n3 = input('Donnez n3 : ')
if '.' not in n3:
    n3 += '.0'

m = n3
if n1 >= n2 and n1 >= n3 :
    m = n1
else:
    if n2 > n1 and n2 > n3:
        m = n2
    else:
        m = n3
print('le max est : ', m)

# 2
d = input('Debut : ')
if '.' not in d:
    d += '.0'
f = input('Fin : ')
if '.' not in f:
    f += '.0'
n = input('Donnez un nombre : ')
if '.' not in n:
    n += '.0'
if n >= d and n <= f:
    print('appartient')
else:
    print('n\'appartient pas')

# 3
nom = input('Votre nom : ')
sexe = input('Votre sexe : ')

if sexe == 'M':
    print('A Cher Monsieur', nom)
else:
    print('A Chère Mademoiselle', nom)

# 4
import math
n = input('N = ')
if '.' not in n:
    n += '.0'
n = float(n)
if n < 0:
    print('La racine ne peut etre calculee')
else:
    print('Racine =', math.sqrt(n))

# 5
a = input('Donnez a : ')
if '.' not in a:
    a += '.0'
a = float(a)
b = input('Donnez b : ')
if '.' not in b:
    b += '.0'
b = float(b)
c = input('Donnez c : ')
if '.' not in c:
    c += '.0'
c = float(c)

if a+b>c and a+c>b and b+c>a:
    print('Triangle possible')
    if a==b and a==c:
        print('Triangle equilateral')
    else:
        if (a**2+b**2 == c**2) or (a**2+c**2 == b**2) or (c**2+b**2 == a**2):
            print('Triangle rectangle')
        if a==b or a==c or b==c:
            print('Triangle isocele')
else:
    print('Triangle impossible')

# 6
a = int(input("Annee : "))
if a%4 == 0:
   if a%100 == 0:
       if a%400 == 0:
        print(a, 'est bissextile')
       else:
           print(a, 'n\'est pas bissextile')
   else:
       print(a, 'est bissextile')
else:
   print(a, 'n\'est pas bissextile')