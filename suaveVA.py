import numpy as np
import matplotlib.pyplot as plt

"""def projectile_motion(initial_velocity, launch_angle_degrees, time_points):

    g = 9.81  # m/s^2
    launch_angle_radians = np.deg2rad(launch_angle_degrees)

    x = initial_velocity * np.cos(launch_angle_radians) * time_points
    y = (initial_velocity * np.sin(launch_angle_radians) * time_points) - (0.5 * g * time_points**2)
    return x, y


v_max = 30  # degress/s
a_max = 10 # degress/s
q_i = np.radians(0)
q_j = np.radians(90)
delta_t = v_max/a_max
v = a_max*delta_t
print(v)
time = np.linspace(0, 3)  # Time points

x_pos, y_pos = projectile_motion(v_max, a_max, time)

plt.figure(figsize=(8, 6))
plt.plot(x_pos, y_pos, label='Projectile Trajectory')
plt.xlabel('Horizontal Distance (degress)')
plt.ylabel('Vertical Distance (s)')
plt.title('Projectile Motion')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()"""



# resolucao professor
def trapezoid(qi, qf):
    v_max = 20 # m/s ^2
    a_max = 10 # m/s^2


    # tempo par chegar na velocidade máxima
    delta_t_acc = v_max/a_max

    #distancia percorrida durante a aceleracao
    delta_dist_acc = 0.5*a_max*delta_t_acc**2

    #distancia percorrida constante
    delta_dist_const = abs(qf- qi) - 2*delta_dist_acc

    #tempo constante
    delta_t_const = delta_dist_const/v_max

    # falta 50 graus para percorrer, e o tempo vai ser de 2.5
    print(delta_t_acc, delta_dist_acc, delta_dist_const, delta_t_const)


trapezoid(0, 90)

