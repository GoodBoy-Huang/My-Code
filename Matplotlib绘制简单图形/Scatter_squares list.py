import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_value = [x**2 for x in x_values]

#绘制图像并设置图形使用点的颜色和尺寸
#颜色设置可采用三位数元组RGB数值,数值范围为0~1之间的小数
#颜色映射使用渐变色显示数值大小

plt.scatter(x_values, y_value, c = y_value, cmap= plt.cm.Blues, edgecolor= "none" ,s = 20)

#设置图标标题并给坐标轴加上标签
plt.title("Square numbers", fontsize =20)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Value of Squares", fontsize =14)

#设置刻度标记的大小
plt.tick_params(axis="both", which = "major", labelsize =14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()
#自动保存图表，将plt.show()替换为以下代码即可，其中bbox_iunches实参数将图表空余区域裁剪掉
#plt.savefig("Squares_plot.png", bbox_inches = "tight")
