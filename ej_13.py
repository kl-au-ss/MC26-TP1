import numpy as np
import random
import matplotlib.pyplot as plt

def cubic_bezier(t, puntos:list[np.array]):
    return (1-t) ** 3 * puntos[0] + 3 * (1-t) ** 2 * t * puntos[1] + 3 * (1-t) * t**2 * puntos[2] + t ** 3 * puntos[3]

puntos_aleatorios_1 = [np.array([random.randint(1, 50),random.randint(1, 50)]),
                     np.array([random.randint(1, 50),random.randint(1, 50)]),
                     np.array([random.randint(1, 50),random.randint(1, 50)]),
                     np.array([random.randint(1, 50),random.randint(1, 50)])]

puntos_aleatorios_2 = puntos_aleatorios_1.copy()

random.shuffle(puntos_aleatorios_2)

# bezier1 = cubic_bezier(0,puntos_aleatorios_1)
# bezier2 = cubic_bezier(0,puntos_aleatorios_2)

# ==============================
# Construir matriz de transformación lineal
# tal que T(P0)=Q3 y T(P3)=Q0
# ==============================

def construir_transformacion(P0, P3, Q3, Q0):
    M = np.column_stack((P0, P3))      # matriz dominio
    N = np.column_stack((Q3, Q0))      # matriz imagen

    if np.linalg.det(M) == 0:
        return None   # No es invertible → no existe T

    A = N @ np.linalg.inv(M)
    return A

# ==============================
# Generar curvas
# ==============================

t_vals = np.linspace(0,1,200)

curva1 = np.array([cubic_bezier(t, puntos_aleatorios_1) for t in t_vals])
curva2 = np.array([cubic_bezier(t, puntos_aleatorios_2) for t in t_vals])

# ==============================
# Graficar B1
# ==============================
plt.figure()
plt.plot(curva1[:,0], curva1[:,1])
control1 = np.array(puntos_aleatorios_1)
plt.plot(control1[:,0], control1[:,1], 'o--')
plt.title("Curva B1(t)")
plt.show()

# ==============================
# Graficar B2
# ==============================
plt.figure()
plt.plot(curva2[:,0], curva2[:,1])
control2 = np.array(puntos_aleatorios_2)
plt.plot(control2[:,0], control2[:,1], 'o--')
plt.title("Curva B2(t)")
plt.show()

# ==============================
# Intentar construir T
# ==============================
P0, P1, P2, P3 = puntos_aleatorios_1
Q0, Q1, Q2, Q3 = puntos_aleatorios_2

A = construir_transformacion(P0, P3, Q3, Q0)

if A is not None:
    curva1_transformada = np.array([A @ punto for punto in curva1])

    plt.figure()
    plt.plot(curva1_transformada[:,0], curva1_transformada[:,1], label="T(B1(t))")
    plt.plot(curva2[:,0], curva2[:,1], label="B2(t)")
    plt.legend()
    plt.title("Comparación T(B1(t)) y B2(t)")
    plt.show()
else:
    print("No es posible definir la transformación lineal (P0 y P3 son dependientes).")