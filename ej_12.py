import numpy as np
# import matplotlib as plt
import matplotlib.pyplot as plt

p0 = np.array([-5,0])
p1 = np.array([2,-2])
p2 = np.array([9,6])
p3 = np.array([16,3])

# aclarar en reporte

def cubic_bezier(t):
    return (1-t) ** 3 * p0 + 3 * (1-t) ** 2 * t * p1 + 3 * (1-t) * t**2 * p2 + t ** 3 * p3

def cubic_bezier2(t, puntos:list[np.array]):
    return (1-t) ** 3 * puntos[0] + 3 * (1-t) ** 2 * t * puntos[1] + 3 * (1-t) * t**2 * puntos[2] + t ** 3 * puntos[3]

lista = [np.array([-5,0]),
         np.array([2,-2]),
         np.array([9,6]),
         np.array([16,3])]

print(cubic_bezier(0.8))
print(cubic_bezier2(0.8,lista))


t = np.linspace(0, 1, 400)

B0 = (1 - t)**3
B1 = 3*(1 - t)**2*t
B2 = 3*(1 - t)*t**2
B3 = t**3

plt.plot(t, B0)
plt.plot(t, B1)
plt.plot(t, B2)
plt.plot(t, B3)

plt.xlabel("t")
plt.ylabel("Coeficientes")
plt.title("Funciones de Bernstein grado 3")
plt.legend(["B0", "B1", "B2", "B3"])
plt.grid()
plt.show()