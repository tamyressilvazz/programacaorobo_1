import numpy as np
import math

def R_x(theta):
    theta = np.radians(theta)
    cos_theta = math.cos(theta)
    sen_theta = math.sin(theta)

    R_x = np.array([
            [1, 0, 0, 0],
            [0, cos_theta, -sen_theta, 0],
            [0, sen_theta, cos_theta, 0],
            [0, 0, 0, 1]
        ])
    
    return R_x

def R_y(theta):
    theta = np.radians(theta)

    cos_theta = math.cos(theta)
    sen_theta = math.sin(theta)

    R_y = np.array([
            [cos_theta, 0, sen_theta, 0],
            [0, 1, 0, 0],
            [-sen_theta, 0, cos_theta, 0],
            [0, 0, 0, 1]
        ])
    
    return R_y

def R_z(theta):
    theta = np.radians(theta)

    cos_theta = math.cos(theta)
    sen_theta = math.sin(theta)

    R_z = np.array([
            [cos_theta, -sen_theta, 0, 0],
            [sen_theta, cos_theta, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
    return R_z


def T_xyz(x,y,z):
    
    T_xyz = np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])
    
    return T_xyz


def tool_tip_pose1(q0, q1, a1):
    # composição das transformações
    y = 0
    z = 0
    
    t_x = T_xyz(a1, y, z)
    r_y = R_y(q1)
    r_z = R_z(q0)
    #E = r_z @ r_y @ t_x

    res1 = np.matmul(r_z, r_y)
    E1 = np.round(np.matmul(res1, t_x), 3)

    return E1
    

def tool_tip_pose2(q0, q1, a2):
    # composição das transformações
    y = 0
    z = 0
    
    t_x = T_xyz(a2, y, z)
    r_y = R_y(q1)
    r_z = R_z(q0)


    res2 = np.matmul(r_y, r_z)
    E2 = np.round(np.matmul(res2, t_x), 3)

    return E2


theta = 0

"""print(R_x(theta))

print(R_z(theta))

print(T_xyz(1, 1, 1))
"""

# configuração do motor
q0 = 0
q1 = 0
a1 = 0.103

print(tool_tip_pose1(q0, q1, a1))

# configuração do motor
q0 = 90
q1 = 0
a1 = 0.103

print(tool_tip_pose1(q0, q1, a1))

# configuração do motor
q0 = 0
q1 = 90
a1 = 0.103

print(tool_tip_pose1(q0, q1, a1))

# configuração do motor
q0 = -90
q1 = 90
a1 = 0.103

print(tool_tip_pose1(q0, q1, a1))

# configuração do motor
q0 = -90
q1 = 0
a1 = 0.103

print(tool_tip_pose1(q0, q1, a1))