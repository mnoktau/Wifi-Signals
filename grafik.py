import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Verileri yükle
data = pd.read_csv('wifi_signal_data.csv')

# Örnek veriler için 3D koordinatlar oluşturun
x = np.linspace(0, 10, len(data[data['arduino'] == 1]))
y = np.linspace(0, 10, len(data[data['arduino'] == 2]))
X, Y = np.meshgrid(x, y)
Z1 = np.array(data[data['arduino'] == 1]['rssi']).reshape(len(x), len(y))
Z2 = np.array(data[data['arduino'] == 2]['rssi']).reshape(len(x), len(y))
Z = (Z1 + Z2) / 2  # Ortalama sinyal gücü

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X ekseni')
ax.set_ylabel('Y ekseni')
ax.set_zlabel('Sinyal Gücü (dBm)')

plt.show()
