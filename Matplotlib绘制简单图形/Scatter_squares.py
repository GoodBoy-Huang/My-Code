import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_value = [1,4,9,16,25]

plt.scatter(x_values, y_value, s = 200)

#设置图标标题并给坐标轴加上标签
plt.title("Square numbers", fontsize =20)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Value of Squares", fontsize =14)

#设置刻度标记的大小
plt.tick_params(axis="both", which = "major", labelsize =14)

plt.show()

