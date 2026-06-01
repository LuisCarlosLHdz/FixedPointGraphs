#Este es un código que genera una grafica de un punto fijo de Q6,25
#Autor: Luis Carlos Lujano Hernandez
#Fecha: 20/10/2023
############################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
############################
#Función para convertir un número en formato Q6.25 a decimal
def hex_to_q625(hex_str, signed=True):
    total_bits = 32
    frac_bits = 28
    val = int(hex_str, 16)
    if signed and val & (1 << (total_bits - 1)):
        val -= (1 << total_bits)
    return val / (2 ** frac_bits)
################################
# Ejemplo de uso
#hex_values = ["00333333", "00333333", "00333333", "00333333"]
#fixed_values = [hex_to_q625(h) for h in hex_values]
#print(fixed_values)
################################
#Leer los datos del archivo de texto y convertirlos a decimal
df = pd.read_csv("data_Lu.txt", header=None, sep=',', encoding='utf-8') #Leer datos del archivo: data.txt
n = len(df) #Tamaño del dataframe
var = 3; #Número de variables
q625_to_dec = np.zeros((n,var)) #Crear un arreglo de índices
for i in range(var):
    for j in range(n):
        q625_to_dec[j][i] = hex_to_q625(df[i][j])
print(n) #Imprimir la primera columna del arreglo
###############################
with open("matriz.txt", "w") as f:
    for fila in q625_to_dec:
        linea = ", ".join(f"{x:.6f}" for x in fila)
        f.write(linea + "\n")

################################
#Graficar los datos
plt.subplot(2, 2, 1)
plt.plot(q625_to_dec[:, 0], q625_to_dec[:, 1], linestyle='-', color='black', label='Q3,28')
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
plt.subplot(2, 2, 2)
plt.plot(q625_to_dec[:, 0], q625_to_dec[:, 2], linestyle='-', color='black', label='Q3,28')
plt.xlabel("x1")
plt.ylabel("x3")
plt.grid(True)
plt.subplot(2, 2, 3)
plt.plot(q625_to_dec[:, 1], q625_to_dec[:, 2], linestyle='-', color='black', label='Q3,28')
plt.xlabel("x1")
plt.ylabel("x4")
plt.grid(True)

plt.show()
####################
