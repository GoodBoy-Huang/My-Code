import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = "Document/death_valley_2014.csv"

#打开并读取CSV文件
with open(file_name) as f :
    reader = csv.reader(f)
    #读取文件首行
    header_row = next(reader)

    #创建一个空列表
    dates,highs,lows = [],[],[]
    #读取文件中的各行并提取最高气温
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            #字符串转化为整数,获取最高温和最低温数据
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,"missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据读取的数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c="red",alpha=0.5)
plt.plot(dates,lows, c="blue",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)
#设置图形的格式
plt.title("Daily high temperatures - 2014",fontsize= 16)
plt.xlabel(" ",fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)

plt.show()

