import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
#执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:",r.status_code)

#将API存储在一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

names, plot_dicts = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
                 "value": repo_dict['stargazers_count'],
                 "label": str(repo_dict['description']),
                 "xlink":repo_dict["html_url"]
                 }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS("#FF0000",base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
#隐藏图表中的水平线
my_config.show_legend = False
#设置图表标题、副标签和主标签的字体大小
# 副标签是 x 轴上的项目名以及 y 轴上的大部分数字。主标签是 y 轴上为5000整数倍的刻度
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_lable_font_size = 18
#使用truncate_label 将较长的项目名缩短为15个字符
my_config.truncate_label = 5
#隐藏图表中的水平线
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("Des",plot_dicts)
chart.render_to_file("python_repos.svg")

