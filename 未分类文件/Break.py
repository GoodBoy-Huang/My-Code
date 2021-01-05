'''break语句,和C中的类似用于跳出最近的for或while循环.循环语句可能带有一个else子句；
   它会在循环遍历完列表(使用for) 或是在条件变为假(使用while)的时候被执行,但是不会
   在循环被break语句终止时被执行'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
    # loop fell through without finding a factor
        print(n, 'is a prime number')
