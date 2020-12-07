# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:03:37 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.ticker import FuncFormatter

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(5)
def formatnum(x, pos):
    return '$%.1f$x$10^{-7}$' % (x * 10000000)


formatter = FuncFormatter(formatnum)
y = [1.7122961713546577E-6
,  1.974137545994235E-6
,  2.0364398690489164E-6
,  6.164170422357015E-13
,  2.3187566713583976E-6]
#
y1 = [ 3.1971319216036473E-6
,  5.61704450463787E-7
,  2.290615386567937E-6
,  8.044426373356054E-9
,  1.4838218368172328E-7]
#
y2 = [ 8.710854096974353E-7
,  1.3718282432334452E-7
,  8.648407736484448E-7
,  4.132910538963315E-7
,  7.2254854519417E-7]
#
y3 = [ 1.0785083004829597E-6
,  1.9808742553745284E-9
,  5.141206123829414E-8
,  2.2470514717995714E-10
,  7.077639983415637E-7]

bar_width = 0.2
tick_label = ["150", "300", "450", "600", "750"]
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)

plt.bar(x, y, bar_width, align="center", color="mediumblue", label="sd-a", alpha=1.0)
plt.bar(x+bar_width, y1, bar_width, color="brown", align="center", label="sd", alpha=1.0)
plt.bar(x+bar_width+bar_width, y2, bar_width, color="grey", align="center", label="s-asd", alpha=1.0)
plt.bar(x+bar_width+bar_width+bar_width, y3, bar_width, color="chocolate", align="center", label="sd", alpha=1.0)
ax.legend()

plt.xlabel("The Number Of File")
plt.ylabel("Response Time(ms)")

plt.xticks(x+bar_width+bar_width/2, tick_label)

plt.legend()

plt.savefig("12.jpg")

plt.show()
