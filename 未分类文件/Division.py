#输入两个数字和输入Q退出程序
print("Give me two numbers,and I'll divide them")
print("Enter 'q' to quit")

while True:
    #输入需要进行计算的数和输入Q退出
    first_number = input("\nFirst number:")
    if first_number == "q" or first_number == "Q":
        break

    second_number = input("\nSecond number:")
    if second_number=="q" or second_number=="Q":
        break
    #判断除数是否为0，是输出提示，否则进行除法运算
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero !")

    else:
        print(answer)
