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
# 0.4123991666666681 0.8188238888888899 1.2291874999999997 1.6318033333333282 2.03814166666668 2.4495950000000035
y = [412, 819, 1229, 1631, 2038, 2449]
# 0.4080783333333348 0.7815150000000014 1.1771074999999982 2.02242916666668  1.5612211111111043 2.3713766666666696
y1 = [408, 781, 1177, 1561, 2022, 2371]
# 0.3774591666666686 0.7317222222222239 1.067866666666637 1.4023366666666575 1.8772958333333445  2.0522550000000034
y2 = [374, 731, 1067, 1402, 1877, 2052]
# 0.3236697222222235 0.6052666666666636 0.9045016666666665 1.200708888888883 1.5282444444444514 1.7856166666666637
y3 = [324, 605, 904, 1201, 1528, 1785]

bar_width = 0.2
tick_label = ["150", "300", "450", "600", "750", "900"]

patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')
plt.figure(figsize=(10, 5))

#plt.bar(x, y, bar_width, align="center", color='w', edgecolor='k', hatch='xxx', label="FCFS", alpha=1.0)
#plt.bar(x+bar_width, y1, bar_width, color='w', edgecolor='k', hatch='\\\\\\\\', align="center", label="HDFS", alpha=1.0)
#plt.bar(x+bar_width+bar_width, y2, bar_width, color='w', edgecolor='k', hatch='---', align="center", label="DCS-UD", alpha=1.0)
#plt.bar(x+bar_width+bar_width+bar_width, y3, bar_width, color='w', edgecolor='k', hatch='////', align="center", label="DQRS", alpha=1.0)

plt.bar(x, y, bar_width, align="center", color="mediumblue", label="asd", alpha=1.0)
plt.bar(x+bar_width, y1, bar_width, color="brown", align="center", label="asd", alpha=1.0)
plt.bar(x+bar_width+bar_width, y2, bar_width, color="grey", align="center", label="asd-asd", alpha=1.0)
plt.bar(x+bar_width+bar_width+bar_width, y3, bar_width, color="chocolate", align="center", label="asd", alpha=1.0)

# plt.xlabel("The Number Of File")
# # plt.ylabel("Response Time(ms)")
for a, b in zip(x, y):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2, y1):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2+bar_width/2+bar_width/2, y2):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
for a, b in zip(x+bar_width/2+bar_width/2+bar_width/2+bar_width/2+bar_width/2+bar_width/2, y3):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)
plt.xlabel("sad")
plt.ylabel("sad(ms)")

plt.xticks(x+bar_width+bar_width/2, tick_label)

plt.legend()

plt.savefig("2.jpg")

plt.show()
