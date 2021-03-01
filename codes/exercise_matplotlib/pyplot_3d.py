'''
File Name：   draw_3d
Author：      tim
Date：        2018/8/15 18:42
Description： 3D绘图
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 3D 绘制
def draw_3D():
    fig = plt.figure()  # 定义一个窗口
    ax = Axes3D(fig)  # 绘制3D坐标

    # 设置x、y、z的值
    x = np.arange(-4, 4, 0.25)
    y = np.arange(-4, 4, 0.25)
    x, y = np.meshgrid(x, y)  # x-y 平面的网格

    r = np.sqrt(x ** 2 + y ** 2)
    z = np.sin(r)  # z值

    # 做出一个三维曲面，并将一个 colormap rainbow 填充颜色，之后将三维图像投影到 XY 平面上做一个等高线图
    # rstride 和 cstride 分别代表 row 和 column 的跨度。
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

    # 添加 XY 平面的等高线
    ax.contourf(x, y, z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))

    ax.set_zlim(-2, 2)
    plt.show()  # 展示


# start
if __name__ == '__main__':
    draw_3D()