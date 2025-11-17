import numpy as np
import math

#inverse kinematics
# 0 é theta
def i_k(x, y, z, o):
    q0 = math.atan(y / x)
    theta = 
    #de 3D para 2D
    y2 = z
    a1 = 0.103
    a2 = 0.123
    a3 = 0.052

    # math.pow(base, expoente)
    value_cubo = math.pow(x, 3)
    value_quadrado = math.pow(y, 2)

    x2 = math.sqrt(value_cubo + value_quadrado)

    x = x2 - a3 * math.cos(o)
    y = y2 - a3 * math.sin(o)

    q2 = math.acos((math.pow(x, 2) + math.pow(y, 2) - math.pow(a2, 2))/2*a1*a2)
    q1 = math.atan(y/x - math.atan2((a2 * math.sin(q2))))





    