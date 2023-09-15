import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ID
print("Nama : Oscar")
print("NRP : 5009211064")

# Membuat sinyal acak
np.random.seed(0)
sinyal_asli = np.random.randn(1000)

# Mendefinisikan filter FIR dengan koefisien low-pass
koef_lowpass = signal.firwin(30, 0.2)  # Filter low-pass orde 30, cut-off frequency 0.2

# Melakukan filtering sinyal asli dengan filter FIR
sinyal_terfilter = signal.lfilter(koef_lowpass, 1.0, sinyal_asli)

# Menampilkan plot sinyal asli dan sinyal terfilter
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(sinyal_asli, label='Sinyal Asli')
plt.title('Sinyal Asli')

plt.subplot(2, 1, 2)
plt.plot(sinyal_terfilter, label='Sinyal Terfilter', color='green')
plt.title('Sinyal Terfilter (Low-pass FIR)')
plt.tight_layout()
plt.show()
