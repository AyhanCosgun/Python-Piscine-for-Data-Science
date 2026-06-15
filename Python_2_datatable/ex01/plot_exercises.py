import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# lines = plt.plot(
#     [1,2,3],[4,5,6], marker='o', mfc='red', mec='green', ms=15, lw=8
# )

# plt.plot(
#     [1,2,3],[4,5,6],"r-",
#     [1,2,3],[1,4,9],"bo--"
# )

x = np.linspace(0, 2*np.pi, 10000)
y1 = np.sin(x)
y2 = np.cos(x)

intersections = [(i, np.sin(i)) for i in x if abs(np.sin(i) - np.cos(i)) < 0.001]
plt.scatter([p[0] for p in intersections], [p[1] for p in intersections], c='red', s=50, label='Intersections')
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")

plt.legend(loc='upper center')
plt.show()

print(__file__)
script_path = Path(__file__)
print(script_path)
print(script_path.resolve())
print(script_path.parent)
