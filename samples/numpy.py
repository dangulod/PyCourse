import numpy as np

from numpy import pi

# ver todos los modulos y funciones que tiene numpy

dir(np)

# crear arrays

x = np.zeros(10)
x = np.zeros((10, 10))
x = np.eye(10)

a = np.arange(15)

a.reshape(3, 5)

type(a)
dir(a)

a.shape
a.ndim

a = np.array([2, 4, 6, 8, 10 , 12, 14, 16, 18, 20])
b = np.array([(2, 4, 6, 8, 10, 12, 14, 16, 18, 20), (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)])

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

c = np.linspace( 2, 0, 9 )

# operaciones con arrays

10 * c

np.sqrt(c)
np.sin(c)

c < 1

# matrices

A * B
np.dot(A, B)
A.transpose()

# metodos de arrays

c.min()
c.mean
c.std()

b.std()
b[0].std()
b[1].std()

# anidar metodos

np.dot(A, B).transpose().reshape(1,4).sum().max().min()

# Indexar 

a = np.arange(10) ** 3

a
a[2]
a[2:5]
a[0:6:2] = -1000
a[-1]
a[-3]
a[a > 10]

b = np.arange(36).reshape(6,6) ** 2
b[2, 3]
b[0:2, 2:5]
b[:, 5]

## ndimensionales

b = np.arange(1296).reshape(6,6,6,6)
b[:4,2:4,3:5,1:4]

# aplicar funcion sobre axes

def my_func(a):
  """Average first and last element of a 1-D array"""
  return (a[0] + a[-1]) ** 0.5

b = np.array([[1,2,3], [4,5,6], [7,8,9]])

np.apply_along_axis(my_func, 0, b)

(b[0] + b[-1]) ** 0.5

np.apply_along_axis(my_func, 1, b)

(b[:,0,:] + b[:,-1,:]) ** 0.5

# funcion map

c = np.arange(100)
list(map(lambda x: x +  np.pi, c))
c[list(map(lambda x: x < 5, c))]
c[list(map(lambda x: x < 5 and x > 90, c))]

list(map(lambda x, y, z, a, b, c: x + y + z +a + b+ c,range(10), range(10), range(10), range(10), range(10), range(10)))

# modulo np.random para generar arrays de numeros aleatorios

np.random.randn(10)

# dir(np.random)
# help(np.random.negative_binomial)

# Ejemplo: convolucion de una poisson y una normal

def conv_pois(l, mu, sigma):
    return(np.random.normal(mu, sigma, np.random.poisson(l)).sum())

mu = 10
sigma = 5
l = 100
n_simul = 100000

x = np.zeros(n_simul)

x = np.array(list(map(lambda x: conv_pois(l = l, mu = mu, sigma = sigma), x)))

np.percentile(x, (0, 25, 50, 75, 100))

np.percentile(x, 99.95)

