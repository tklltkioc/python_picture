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

x = np.arange(6)

# 953.265998632806 1972.5428193431 2868.39366853772 3811.691429 4784.1160924512 5876.47770762992
y = [953, 1972, 2868, 3811, 4784, 5876]
# 966.0486203168772 1937.87900487119 2866.7114822222 3834.44405703606 4793.11392016307 5767.21586477727
y1 = [966, 1937, 2866, 3834, 4793, 5767]
# 951.026058221279 1901.95401642825 2808.503966 3789.95202552537 4691.79484264873 5767.21586477727
y2 = [951, 1901, 2808, 3789, 4691, 5676]
# 916.737049656064 1833.47409931212 2755.19588807731 3644.15258417583 4583.68524828032 5410.39177615462
y3 = [916, 1833, 2755, 3644, 4583, 5410]

bar_width = 0.2
tick_label = ["150", "300", "450", "600", "750", "900"]
plt.figure(figsize=(10, 5))
#plt.bar(x, y, bar_width, align="center", color='w', edgecolor='k', hatch='xxx', label="FCFS", alpha=1.0)
#plt.bar(x+bar_width, y1, bar_width, color='w', edgecolor='k', hatch='\\\\\\\\', align="center", label="HDFS", alpha=1.0)
#plt.bar(x+bar_width+bar_width, y2, bar_width, color='w', edgecolor='k', hatch='---', align="center", label="DCS-UD", alpha=1.0)
#plt.bar(x+bar_width+bar_width+bar_width, y3, bar_width, color='w', edgecolor='k', hatch='////', align="center", label="DQRS", alpha=1.0)

plt.bar(x, y, bar_width, align="center", color="mediumblue", label="ad", alpha=1.0)
plt.bar(x+bar_width, y1, bar_width, color="brown", align="center", label="asd", alpha=1.0)
plt.bar(x+bar_width+bar_width, y2, bar_width, color="grey", align="center", label="ads-asd", alpha=1.0)
plt.bar(x+bar_width+bar_width+bar_width, y3, bar_width, color="chocolate", align="center", label="asd", alpha=1.0)

for a, b in zip(x, y):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2+bar_width/8, y1):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2+bar_width/2+bar_width/2+bar_width/4, y2):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2+bar_width/2+bar_width/2+bar_width/2+bar_width/2+bar_width/3, y3):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
# plt.xlabel("The Number Of File")
# plt.ylabel("Storage Space(GB)")
plt.xlabel("sad")
plt.ylabel("asd(GB)")

plt.xticks(x+bar_width+bar_width/2, tick_label)

plt.legend()

plt.savefig("3.jpg")

plt.show()
