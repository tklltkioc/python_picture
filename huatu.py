# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:03:37 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import spline

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False


#
def formatnum( x, pos ):
    return '$%.1f$x$10^{-7}$' % (x * 10000000)


formatter = FuncFormatter(formatnum)

x = np.arange(5)
# 0.4123991666666681
y = [1.7122961713546577E-6
    , 1.974137545994235E-6
    , 2.0364398690489164E-6
    , 6.164170422357015E-13
    , 2.3187566713583976E-6]
#
y1 = [3.1971319216036473E-6
    , 5.61704450463787E-7
    , 2.290615386567937E-6
    , 8.044426373356054E-9
    , 1.4838218368172328E-7]
#
y2 = [8.710854096974353E-7
    , 1.3718282432334452E-7
    , 8.648407736484448E-7
    , 4.132910538963315E-7
    , 7.2254854519417E-7]
#
y3 = [1.0785083004829597E-6
    , 1.9808742553745284E-9
    , 5.141206123829414E-8
    , 2.2470514717995714E-10
    , 7.077639983415637E-7]
plt.figure(figsize=(10, 5))
bar_width = 0.2
tick_label = ["1", "2", "3", "4", "5"]
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(x, y, linestyle='-', marker='o', color="mediumblue", label='x1')

line2, = ax.plot(x, y1, linestyle='-', marker='^', color="brown", label='x2')

line3, = ax.plot(x, y2, linestyle='-', marker='D', color="grey", label='x3')

line4, = ax.plot(x, y3, linestyle='-', marker='s', color="chocolate", label='x4')

ax.legend()

# xnew = np.linspace(x.min(), x.max(), 300)  # 300 represents number of points to make between T.min and T.max
#
# power_smooth = spline(x, y, xnew)
#
# plt.plot(xnew, power_smooth)


# plt.xlabel("DataCenter ID")
# plt.ylabel("Load Variance")
plt.xlabel("数据")
plt.ylabel("负载")

plt.xticks(x + bar_width / 6, tick_label)

plt.legend()

plt.savefig("1.jpg")

plt.show()
