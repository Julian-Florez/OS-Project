import numpy as np

# m1 y m2 son arrays np.array

def sumaMatrices(m1, m2):
    return m1+m2

def multiplicadorMatrices(m1, m2):
    return np.dot(m1,m2)

def productoCruz(m1,m2):
    return  np.cross(m1,m2)

def productoPunto(m1,m2):
    return np.dot(m1, m2)

def traspuesta(m1):
    return m1.T

def inversa(m1):
    return np.linalg.inv(m1)
#Matrises cuadradas
def sistemasDeEcuaciones(m1,rm1):
    return np.linalg.solve(m1,rm1)



