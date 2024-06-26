#Este archivo utiliza el análisis realizado con analisis.py para trazar un histograma con las respuestas correctas del modelo.
import pandas as pd
import matplotlib.pyplot as plt
import math

df_resultados = pd.read_excel("archivo_analizado.xlsx")

# Normalizar las probabilidades 
min_probabilidad = df_resultados['Probabilidad'].min()
max_probabilidad = df_resultados['Probabilidad'].max()
df_resultados['Probabilidad_Normalizada'] = (df_resultados['Probabilidad'] - min_probabilidad) / (max_probabilidad - min_probabilidad)

incorrecta = df_resultados[df_resultados['Respuesta Correcta'] == 0]

# Crear el histograma 
plt.figure(figsize=(10, 6))
plt.hist(incorrecta['Probabilidad_Normalizada'], color='red', alpha=0.5, label='Respuesta Incorrecta', bins=int(math.sqrt(df_resultados.notnull().sum().sum())))
plt.xlabel('Probabilidad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Probabilidades de las Respuestas incorrectas. Indicar versión y modelo')

media_probabilidades = incorrecta['Probabilidad_Normalizada'].mean()

plt.axvline(x=media_probabilidades, color='blue', linestyle='--')


plt.legend([f'Respuestas Incorrectas', f'Media = {media_probabilidades}'])

plt.grid(True)
plt.savefig("hist_incorrectas_version_modelo.png")
plt.show()

