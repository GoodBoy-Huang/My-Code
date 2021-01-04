class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age  = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over")

"""输入两只小狗的信息"""
my_dog= Dog("peter",4)
your_dog = Dog("Jack",3)

"""打印My dog的信息"""
print("\nMy dog's name is "+ my_dog.name.title()+"!")
print("My dog is "+str(my_dog.age)+"!")
my_dog.sit()

"""打印your dog的信息"""
print("\nyour dog's name is "+ your_dog.name.title()+"!")
print("your dog is "+str(your_dog.age)+"!")
your_dog.roll_over()
