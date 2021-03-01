'''
File Name：   draw
Author：      tim
Date：        2018/8/15 16:47
Description： 图形绘制。十分有用，对于工作中实验性的项目，可以快速展示效果。如果使用java，还需要配合前端展示。
'''

import matplotlib.pyplot as plt
import numpy as np  # 模块取别名


# 直方图
def draw_hist():
    mu = 100
    sigma = 20

    x = mu + sigma * np.random.randn(20000)  # 样本数量
    plt.hist(x, bins=100, color='green', normed=True)  # bins：显示有几个直方，normed是否对数据进行标准化

    plt._show()


# 条形图
def draw_bar():
    y = [20, 10, 30, 25, 15]  # Y轴数据
    index = np.arange(5)  # X轴数据，也可以是index = [0,5]

    plt.bar(left=index, height=y, color='blue', width=0.5)
    plt.show()


# 折线图
def draw_plot():
    x = np.linspace(-10, 10, 100)  # -10到10，100个点
    y = x ** 3  # x的3次幂

    plt.plot(x, y, linestyle='--', color='orange', marker='<')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()


# 散点图
def draw_scatter():
    x = np.random.randn(1000)
    y = x + np.random.randn(1000) * 0.5

    plt.scatter(x, y, s=5, marker='<')  # s表示面积，marker表示图形
    plt.show()


# 饼状图
def draw_pie():
    labels = 'A', 'B', 'C', 'D'  # 4个模块
    fracs = [15, 30, 45, 10]  # 每个模块占比例

    plt.axes(aspect=1)  # 使x、y轴比例相同
    explode = [0, 0.5, 0, 0]  # 突出某一部分区域

    plt.pie(x=fracs, labels=labels, autopct='%.0f%%', explode=explode)  # autopct显示百分比
    plt.show()


# 带图例
def draw_with_legend():
    x = np.arange(1, 11, 1)  # x轴坐标，1开始，11结束，步长为1

    plt.plot(x, x * 2)  # 第一条线，x,y坐标
    plt.plot(x, x * 3)
    plt.plot(x, x * 4)

    plt.legend(['Normal', 'Fast', 'Faster'])  # 设置图例，与上面的线对应
    plt.grid(True, color='green', linestyle='--', linewidth=1)  # 绘制网格

    plt.show()


# start
if __name__ == '__main__':
    # draw_hist()
    # draw_bar()
    draw_plot()
    # draw_scatter()
    # draw_pie()
    # draw_with_legend()