import numpy as np
import matplotlib.pyplot as plt

p0 = np.array([0,0])
p1 = np.array([2,4])
p2 = np.array([4,0])

def quad_bezier (t:float, p0, p1, p2):
    return (1-t)**2 * p0 + 2 * (1-t) * t * p1 + t**2 * p2


t_values = np.linspace(0, 1, 100)

curve_points = np.array([quad_bezier(t) for t in t_values])

plt.figure()

plt.plot(curve_points[:,0], curve_points[:,1])

control_x = [p0[0], p1[0], p2[0]]
control_y = [p0[1], p1[1], p2[1]]
plt.plot(control_x, control_y, marker='o')

plt.title("Curva de Bézier Cuadrática")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

def it_bezier(t, p0, p1, p2):
    q0 = (1-t)*p0 + t*p1
    q1 = (1-t)*p1 + t*p2
    return (1-t)*q0 + t*q1


print(it_bezier(1))