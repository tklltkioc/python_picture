import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import xlrd
import xlwt

def data_read():
    file = xlrd.open_workbook(r'数据.xlsx')
    sheet1 = file.sheet_by_name('#1准确率&时间')
    sheet2 = file.sheet_by_name('#2收敛过程')
    sheet3 = file.sheet_by_name('#2准确率&时间')

    X = sheet1.col_values(1)[1:26]
    for i in range(len(X)): X[i] = int(X[i])

    Bar_len = 0.7

    BSPtime_before = sheet1.col_values(2)[1:26]
    BSPtime_after = sheet1.col_values(6)[1:26]

    BSPacc_before = sheet1.col_values(3)[1:26]
    BSPacc_after = sheet1.col_values(7)[1:26]

    SSPtime_before = sheet1.col_values(2)[38:63]
    SSPtime_after = sheet1.col_values(6)[38:63]

    SSPacc_before = sheet1.col_values(3)[38:63]
    SSPacc_after = sheet1.col_values(7)[38:63]


    PSGRD_acc = sheet3.col_values(2)[1:26]
    SGD_acc = sheet3.col_values(5)[1:26]
    Adam_acc = sheet3.col_values(8)[1:26]
    RMSprop_acc = sheet3.col_values(11)[1:26]
    Adagrad_acc = sheet3.col_values(14)[1:26]
    Adadelta_acc = sheet3.col_values(17)[1:26]

    PSGRD_time = sheet3.col_values(1)[1:26]
    SGD_time = sheet3.col_values(4)[1:26]
    Adam_time = sheet3.col_values(7)[1:26]
    RMSprop_time = sheet3.col_values(10)[1:26]
    Adagrad_time = sheet3.col_values(13)[1:26]
    Adadelta_time = sheet3.col_values(16)[1:26]

    jam = sheet3.col_values(23)[15:33]
    jam_x = sheet3.col_values(22)[15:33]


    #1

    #plot_1(X, BSPacc_before, BSPacc_after)
    #plot_1(X, SSPacc_before, SSPacc_after)

    #plot_1(X, BSPtime_before, BSPtime_after)
    #plot_1(X, SSPtime_before, SSPtime_after)


    #2

    #X = sheet2.col_values(0)[3:203]

    #plot_2(X, sheet2)

    #3

    #plot_3(X, PSGRD_acc, SGD_acc, Adam_acc, RMSprop_acc, Adagrad_acc, Adadelta_acc)
    #plot_3(X, PSGRD_time, SGD_time, Adam_time, RMSprop_time, Adagrad_time, Adadelta_time)

    #4

    #plot_4(jam_x, jam)

    #5
    X = sheet2.col_values(0)[3:203]
    Y1 = sheet2.col_values(19)[3:203]
    Y2 = sheet2.col_values(22)[3:203]
    plot_5(X, Y1, Y2)


def plot_1(X, bef, aft):
    x_major_locator = MultipleLocator(2)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    Bar_len = 0.7
    plt.bar([x-0.3 for x in X], bef, Bar_len, color='w', edgecolor='k', hatch='---')
    plt.bar([x+0.3 for x in X], aft, Bar_len, color='w', edgecolor='k', hatch='////')
    plt.xlim(2, 55)
    plt.ylim(3000, 41000)
    plt.xlabel('Number of Processes')
    plt.ylabel('Training Time')
    plt.legend(labels=['Model Average', 'OWA-MA'])
    plt.show()

def plot_2(X, sheet):
    x_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    PSGRD = sheet.col_values(1)[3:203]
    SGD = sheet.col_values(4)[3:203]
    Adam = sheet.col_values(7)[3:203]
    RMSprop = sheet.col_values(10)[3:203]
    Adagrad = sheet.col_values(13)[3:203]
    Adadelta = sheet.col_values(16)[3:203]

    markersize = 4
    plt.figure(figsize=(10,5))
    plt.plot(X, PSGRD, label='PSGRD', linewidth=1, marker='>', mfc='w', color='k', ms=markersize)
    plt.plot(X, SGD, label='SGD', linewidth=1, marker='o', mfc='w', color='k', ms=markersize)
    plt.plot(X, Adam, label='Adam', linewidth=1, marker='+', mfc='w', color='k', ms=markersize)
    plt.plot(X, RMSprop, label='RMSprop', linewidth=1, marker='x', mfc='w', color='k', ms=markersize)
    plt.plot(X, Adagrad, label='Adagrad', linewidth=1, marker='s', mfc='w', color='k', ms=markersize)
    plt.plot(X, Adadelta, label='Adadelta', linewidth=1, marker='v', mfc='w', color='k', ms=markersize)
    plt.xlim(0, 201)
    plt.xlabel('Number of Epochs')
    plt.ylabel('Training Accuracy')
    plt.legend()

    plt.show()

def plot_3(X, data1, data2, data3, data4, data5, data6):
    x_major_locator = MultipleLocator(5)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    markersize = 4
    plt.figure(figsize=(10, 5))
    plt.plot(X, data1, label='PSGRD', linewidth=1, marker='>', mfc='w', color='k', ms=markersize)
    plt.plot(X, data2, label='SGD', linewidth=1, marker='o', mfc='w', color='k', ms=markersize)
    plt.plot(X, data3, label='Adam', linewidth=1, marker='+', mfc='w', color='k', ms=markersize)
    plt.plot(X, data4, label='RMSprop', linewidth=1, marker='x', mfc='w', color='k', ms=markersize)
    plt.plot(X, data5, label='Adagrad', linewidth=1, marker='x', mfc='w', color='k', ms=markersize)
    plt.plot(X, data6, label='Adadelta', linewidth=1, marker='s', mfc='w', color='k', ms=markersize)

    plt.xlim(2, 55)
    plt.ylim(9000, 65000)
    plt.xlabel('Number of Processes')
    plt.ylabel('Training Time')
    plt.legend(labels=['PSGRD', 'SGD', 'Adam', 'RMSprop', 'Adagrad', 'Adadelta'])
    plt.show()

def plot_4(X, Y):
    x_major_locator = MultipleLocator(2)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    markersize = 4
    plt.figure(figsize=(10, 5))
    plt.plot(X, Y,  linewidth=1, marker='>', mfc='w', color='k', ms=markersize)

    plt.xlim(16, 52)
    plt.ylim(7500, 9000)
    plt.xlabel('Number of Processes')
    plt.ylabel('Training Time')
    #plt.legend(labels=['PSGRD', 'SGD', 'Adam', 'RMSprop', 'Adagrad', 'Adadelta'])
    plt.show()

def plot_5(X, Y1, Y2):
    x_major_locator = MultipleLocator(10)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    markersize = 4
    plt.figure(figsize=(10, 5))
    plt.plot(X, Y1, label='MA', linewidth=1, marker='>', mfc='w', color='k', ms=markersize)
    plt.plot(X, Y2, label='OWA-MA', linewidth=1, marker='o', mfc='w', color='k', ms=markersize)

    plt.xlim(0, 201)
    plt.ylim(0.4, 5)
    plt.xlabel('Number of Epochs')
    plt.ylabel('Validation Loss')
    plt.legend(labels=['MA', 'OWA-MA'])
    plt.show()



if __name__ == '__main__':
    data_read()