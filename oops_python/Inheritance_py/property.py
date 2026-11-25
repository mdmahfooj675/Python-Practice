class Student:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math

        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def cal_percentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98 , 95 , 96)

print("marks of phy : " , s1.phy)
print("marks of chem : " , s1.chem)
print("marks of math : " , s1.math)
print("percentage : " , s1.percentage)

print("--------------------")

s1.phy = 86
print("updated marks of phy : " , s1.phy)

s1.cal_percentage()
print("updated percentage : " , s1.percentage)


print("=============================================")

# using @property

class Student:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def cal_percentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return  str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(90 , 88 , 94)

print("marks of phy : " , s1.phy)
print("marks of chem : " , s1.chem)
print("marks of math : " , s1.math)
print("percentage : " , s1.percentage)

print("--------------------")

s1.phy = 80
print("updated marks of phy : " , s1.phy)

#s1.cal_percentage()
print("updated percentage : " , s1.percentage)