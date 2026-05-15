import numpy as np
import matplotlib.pyplot as plt

p0 = np.array([0,0])
p1 = np.array([2,4])
p2 = np.array([4,0])

# Punto (a)

def quad_bezier (t:float, p0, p1, p2):
    return (1-t)**2 * p0 + 2 * (1-t) * t * p1 + t**2 * p2

# Punto (b)

t_values = np.linspace(0, 1, 100)

# Punto (c)

curve_points = np.array([quad_bezier(t,p0,p1,p2) for t in t_values])

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

# Punto (d)

def it_bezier(t, p0, p1, p2):
    q0 = (1-t)*p0 + t*p1
    q1 = (1-t)*p1 + t*p2
    return (1-t)*q0 + t*q1

son_iguales = True

for t in range(10):
    if quad_bezier(t/10,p0,p1,p2).all() != it_bezier(t/10,p0,p1,p2).all(): son_iguales == False

print(son_iguales)