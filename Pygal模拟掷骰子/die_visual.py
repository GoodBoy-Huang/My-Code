import pygal
from die import Die

#创建一个D6和一个D10
die_1=Die()
die_2=Die(10)

#掷多次骰子，并将结果存储在一个列表中
results = []

for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析投掷结果，统计各点数出现的次数
frequencies = []
max_reslut = die_1.num_sides + die_2.num_sides

for value in range(2,max_reslut+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and D10 5000 times."
hist.x_labels = [x_value for x_value in range(2,17)]
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6+D10",frequencies)
hist.render_to_file("Document/die_visual.svg")

