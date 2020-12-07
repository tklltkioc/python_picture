# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:03:37 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(4)

# 953.265998632806 1972.5428193431 2868.39366853772 3811.691429 4784.1160924512 5876.47770762992
y = [0, 105, 46, 130]
# 966.0486203168772 1937.87900487119 2866.7114822222 3834.44405703606 4793.11392016307 5767.21586477727
y1 = [95, 110, 31, 236]
# 951.026058221279 1901.95401642825 2808.503966 3789.95202552537 4691.79484264873 5767.21586477727
y2 = [321, 180, 23, 524]

plt.figure(figsize=(10, 5))
bar_width = 0.2
tick_label = ["asd", "asd", "asd", "sad"]

plt.bar(x, y, bar_width,color='w', edgecolor='k', hatch='\\\\\\\\', align="center", label="sad", alpha=1.0)
plt.bar(x+bar_width, y1, bar_width, color='w', edgecolor='k', hatch='---', align="center", label="sad", alpha=1.0)
plt.bar(x+bar_width+bar_width, y2, bar_width, color='w', edgecolor='k', hatch='////', align="center", label="asd", alpha=1.0)

# plt.xlabel("sad（s）")
plt.ylabel("sad(s)")
for a, b in zip(x, y):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2, y1):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2+bar_width/2+bar_width/2, y2):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)


plt.xticks(x+bar_width+bar_width/2, tick_label)

plt.legend()

plt.savefig("4.jpg")

plt.show()
