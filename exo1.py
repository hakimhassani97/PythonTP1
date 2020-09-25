'''
    EXO 1
'''
# 1
nom = 'HASSANI'
age = 23
travail = True
if travail:
    etat = True
salaire = 2000.4
amis = ['friend1', 'friend2']
parents = ('father', 'mother')

# 2
print(type(nom), isinstance(nom, type(nom)))
print(type(age), isinstance(age, type(age)))
print(type(etat), isinstance(etat, type(etat)))
print(type(salaire), isinstance(salaire, type(salaire)))
print(type(amis), isinstance(amis, type(amis)))
print(type(parents), isinstance(parents, type(parents)))

# 3
auteur ='Charles' # faut utiliser le meme caractere au debut et a la fin
print(auteur)

x = 2018
print("La valeur de x est " + str(x)) # le + est applicable entre les variables de meme type

# 4
a = 9
b = 7
c = 5
print('{} + {} + {}'.format(a, b, c))

# 5
PI = 3.14
angle = 180 # angle en degres
rad = angle * PI / 180 # resultat en radians
print(rad)

# 6
s = 123 # temps en secondes
a = s // (60 * 60 * 24 * 30 * 12)
r = s % (60 * 60 * 24 * 30 * 12)
m = r // (60 * 60 * 24 * 30)
r = r % (60 * 60 * 24 * 30)
j = r // (60 * 60 * 24)
r = r % (60 * 60 * 24)
mi = r // (60)
r = r % (60)
print('annees : {}, mois : {}, jours : {}, minutes : {}, secondes : {}'.format(a, m, j, mi, r))

# 7
r = input('Entrez le rayon du sphere : ')
if '.' not in r:
    r += '.0'
r = float(r)
print('le volume est : ', ((4 * PI / 3) * (r ** 3)))

# 8
l = [x for x in range(10, 31)]
print(type(l), l)

# 9
l = [x for x in range(100, 201) if x % 2 == 1]
l += [x for x in range(100, 201) if x % 2 == 0]
print(type(l), l)

# 10
n1 = input('Donnez n1 : ')
if '.' not in n1:
    n1 += '.0'
n2 = input('Donnez n2 : ')
if '.' not in n2:
    n2 += '.0'
print('le max est : ', max(float(n1), float(n2)))