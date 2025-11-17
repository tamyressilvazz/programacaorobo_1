import numpy as np
import math
from numpy.linalg import inv



def SE_xy(x, y):
    theta = 0
    cos_theta = math.cos(theta)
    sen_theta = math.sin(theta)
    H = np.array([
            [1, 0, x],
            [0, 1, y],
            [0, 0, 1]
    ])
    return H

def SE2_theta(theta):
    cos_theta = math.cos(theta)
    sen_theta = math.sin(theta)

    H = np.array([
            [cos_theta, -sen_theta, x],
            [sen_theta, cos_theta, y],
            [0, 0, 1]
    ])
    return H

x = 0
y = 0
#print(SE_xy(x, y))


theta1 = np.radians(90)

theta2 = np.radians(-90)

#print(SE2_theta(theta1))
#print(SE2_theta(theta2))



def teste():
    H1 = SE_xy(1, 0.25)

    #coordenadas do referencial p2
    p2 = np.array([
        [0.5],
        [0.5],
        [1]
    ])

    result = H1 @ p2

    return result

#print(teste())


def inv_matrix():
    H1 = SE_xy(1, 0.25)
    H1_inv = inv(H1)

    #coordenadas do referencial p2
    p2 = np.array([
        [0.5],
        [0.5],
        [1]
    ])

    mult = np.matmul(H1_inv, p2)
    
    return mult


#print(f'Resolução 2: {inv_matrix()}')


def exercicio3():
    x1 = SE_xy(1, 0.25)

    x2 = np.array([
        [0.5],
        [0.5],
        [1]
    ])


    translation = np.matmul(x1, x2)

    rad_angle = np.radians(45)
    rotation = SE2_theta(rad_angle)

    return rotation

#print(exercicio3())
