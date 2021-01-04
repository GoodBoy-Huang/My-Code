class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year
        self.odometers_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometers(self):
        """打印一条指出汽车里程的消息"""
        print("this car has "+ str(self.odometers_reading)+" miles on it.")

    def update_odometers(self,mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometers_reading:
            self.odometers_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometers(self,miles):
        """将里程表读数增加指定的量"""
        self.odometers_reading += miles


"""
my_new_car.odometers_reading = 23    #直接修改属性的值
my_new_car.read_odometers()
"""

"""
my_new_car.updata_odometers(23)       #通过方法修改属性的值
my_new_car.read_odometers()
"""

my_uesd_car = Car("subura","outback","2010")
print(my_uesd_car.get_descriptive_name())

my_uesd_car.updata_odometers(2100)
my_uesd_car.read_odometers()

my_uesd_car.increment_odometers(120)
my_uesd_car.read_odometers()