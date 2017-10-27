'''
Comentando nuestros scripts, Python permite comentar de dos formas diferentes,

  1. Para comentarios más largos entre una triple comilla
  2. Con #

'''

print('Hello World!')

# Nuestra primera funcion

def hw():
  print('Hello World')

hw()

# Asignar variables

x = [1, 'Hi', 3.14, ['a', 'b', 3]]

x[0]
x[3]
x[3][1]
x[3][1] = 1
x[3][1] += 2
x[3][1] *= 2
x[3][1] **= 2
x[3][1] /= 2

_

y = (1, 'Hi', 3.14)
y[0] = 2

del(y)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
knights.keys()
knights.values()
knights.items()

# Operadores logicos

1 < 0
"car" != "car"
'car' in ('pet', 'house', 'sun')
'car' in ('pet', 'house', 'sun', 'car')

# Dos formas de definir una funcion

exponencial_1 = lambda x, y: x ** y

exponencial_1(2, 3)

def exponencial_2(x, y):
  return(x ** y)

exponencial_2(2, 3)

# Bucles for

# 1 loop

words = ['cat', 'window', 'defenestrate']

for w in words:
  print(w, len(w))

# 2 loop

for  i in range(5):
  print(i)

# 3 loop

for  i in range(len(words)):
  print(words[i])

# 4 loop

x = 0

for i in range(0, 10):
  if (i == 5): 
    continue
  else:
    x += i

x == 0 + 1 + 2 + 3 + 4 + 6 + 7 + 8 + 9

# 5 loop

for n in range(2, 10):
    for x in range(2, n):
       if n % x == 0:
           print(n, 'equals', x, '*', n//x)
           break
    else:
       print(n, 'is a prime number')

# 6 loop

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# 7 loop 

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)

# 8 loop

for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)

# while

i = 0

while i < 10:
  print(i)
  i += 1

# importacion de librerias

from datetime import date

hoy = date.today()

hoy

hoy.__class__

date.today().strftime("%Y-%m-%d")
