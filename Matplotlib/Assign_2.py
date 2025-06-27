import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
sachin_runs = [357, 782, 1095, 1066, 1688]
sehwag_runs = [254, 1344, 1414, 1535, 1991]
kohli_runs  = [757, 1381, 2186, 1910, 2595]

# Bar positions
x = np.arange(len(years))
bar_height = 0.25  # smaller = more spacing

plt.style.use('grayscale')

# Plotting
plt.barh(y=x - bar_height, width=sachin_runs, height=bar_height,
          linewidth=1, color='#0ABAB5', label='Sachin')

plt.barh(y=x, width=sehwag_runs, height=bar_height,
          linewidth=2, color='yellow', label='Sehwag')

plt.barh(y=x + bar_height, width=kohli_runs, height=bar_height,
          linewidth=3, color='green', label='Kohli')

# Y-axis ticks
plt.yticks(x, years)
plt.xlabel("Runs")
plt.title("Total Runs in Debut 5 Years")
plt.legend()
plt.tight_layout()
plt.show()
