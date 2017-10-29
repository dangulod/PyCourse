
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# ver todos los modulos y funciones que tiene numpy

dir(np)

# crear un array de ceros

x = np.zeros(10)
x = np.zeros((10, 10))

# matriz identidad

x = np.eye(10)


# In[6]:


# modulo np.random para generar arrays de numeros aleatorios

np.random.randn(10)


# In[8]:


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

