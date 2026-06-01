#Autor: Luis Carlos Lujano Hernandez
#Fecha: 20/10/2023
############################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
############################
#Función para convertir un número en formato Q6.25 a decimal
# Function to convert a number in Q6.25 format to decimal
def hex_to_FPDec(hex_str, signed=True):
    total_bits = 32 #Ancho de palabra/Word size
    frac_bits = 28 #Número de bits para la parte fraccionaria/Number of bits for the fractional part
    val = int(hex_str, 16)
    if signed and val & (1 << (total_bits - 1)):
        val -= (1 << total_bits)
    return val / (2 ** frac_bits)
################################
# Ejemplo de uso 1: Conversión directa de un número hexadecimal a decimal
# Function to convert a number in Q3.28 format to decimal
hex_values = ["00333333", "00333333", "00333333", "00333333"]
fixed_values = [hex_to_FPDec(h) for h in hex_values]
print(fixed_values)
################################
#Ejemplo de uso 2: Leer los datos del archivo de texto y convertirlos a decimal
# Read data from the text file and convert it to decimal
df = pd.read_csv("data_Lu.txt", header=None, sep=',', encoding='utf-8') #Leer datos del archivo: data_Lu.txt/ Read data from the file: data_Lu.txt
n = len(df) #Tamaño del dataframe / Size of the dataframe
var = 3; #Número de variables / Number of variables
q625_to_dec = np.zeros((n,var)) #Crear un arreglo de índices / Create an array of indices
for i in range(var):
    for j in range(n):
        q625_to_dec[j][i] = hex_to_FPDec(df[i][j])
###############################
with open("matriz.txt", "w") as f:
    for fila in q625_to_dec:
        linea = ", ".join(f"{x:.6f}" for x in fila)
        f.write(linea + "\n")

################################
#Graficar los datos / Plot the data
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

