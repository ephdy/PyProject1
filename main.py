from email.header import USASCII
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class student:
    name=None
    age=None
    native_place=None

    def __init__(self,name,age,native_place):
        self.name=name
        self.age=age
        self.native_place=native_place
    def say_hi(self):
        print(f"hi,i am {self.name}")


num=int(input("请输入学生个数:"))
stu=[]
for i in range(num):
    print("当前录入第位{}学生信息，总共需录入{}位学生信息".format(i+1,num))
    name=input("请输入学生姓名:")
    age = input("请输入学生年龄:")
    place = input("请输入学生地址:")
    stu_1=student(name,age,place)
    stu.append(stu_1)
    print(f"学生信息录入完成，信息为：[学生姓名：{stu_1.name}，年龄：{stu_1.age}，学生地址：{stu_1.native_place}]")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


