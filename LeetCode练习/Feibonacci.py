#斐波那契数列递归计算f(n)的值
def fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

n = int(input(":"))
fib(n)
print(fib(n))

#我不知道在Leetcode怎么回事提交就一直显示fib没有定义
