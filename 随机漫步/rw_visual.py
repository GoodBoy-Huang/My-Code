import matplotlib.pyplot as plt
from random_walk import RandomWalk

#只要程序处于活跃状态，就不断地模拟随机漫步
while True:
    #创建一个RandomWalk实例，并将其包含的点绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    #设置绘图窗口的尺寸，单位为英寸
    plt.figure(figsize=(10,6))

    #按点的先后顺序进行着色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values, c= point_numbers, cmap = plt.cm.Blues, edgecolors= "none", s= 15)

    #突出起点和终点
    plt.scatter(0,0,c="green",edgecolors="none",s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c="red",edgecolors="none",s=100)
    #设置坐标轴标题和大小
    plt.title("Random Walk", fontsize=14)
    plt.xlabel("X value", fontsize=14)
    plt.ylabel("Y value", fontsize=14)

    #隐藏坐标轴将坐标轴设置代码替换为以下代码即可
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

