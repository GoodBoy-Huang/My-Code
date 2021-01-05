'''小明身高1.75,体重80.5kg.请根据BMI公式(体重除以身高的平方)
    帮小明计算他的BMI指数,并根据BMI指数输出结果：
        低于18.5：过轻
        18.5-25：正常
        25-28：过重
        28-32：肥胖
        高于32：严重肥胖'''

def index_bmi(weight,height):
    bmi = weight / (height ** 2)
    if bmi <18.5:
        print('你的BMI是{},过轻'.format(bmi))
    elif 18.5 <= bmi < 25:
        print('你的BMI是{},正常'.format(bmi))
    elif 25 <= bmi <= 28:
        print('你的BMI是{},过重'.format(bmi))
    elif 28<= bmi <= 32:
        print('你的BMI是{},肥胖'.format(bmi))
    else:
        print('你的BMI是{},过重'.format(bmi))

height = float(input("请输入你的身高(m):"))
weight = float(input("请输入你的体重(kg):"))

index_bmi(weight,height)
