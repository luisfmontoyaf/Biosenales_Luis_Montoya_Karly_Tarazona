import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('EMG.csv')

# Graficar la señal EMG
plt.plot(df['EMG'])

plt.xlabel('Muestras')
plt.ylabel('EMG')
plt.title('Señal EMG')
plt.grid()
plt.show()