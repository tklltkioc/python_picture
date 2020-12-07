import matplotlib.pyplot as plt

name = ['part1_00', 'part1_01', 'part1_02', 'part1_03', 'part2_00', 'part2_01', 'part2_02', 'part2_03', 'part2_04',
        'part2_05', 'part2_06', 'all_num']
num = [79855, 39995, 39997, 1734, 99778, 95630, 99167, 13781, 96339, 57913, 14885]

show_all = True
all_num = 0
if show_all:
    for i in num:
        all_num = all_num + i
num.append(all_num)

plt.bar(name, num, color='rgby')
plt.xlabel('name of file')
plt.ylabel("num-of-file")
plt.title("num-of-each-file")
for a, b in zip(name, num):
    plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=11)

plt.show()
