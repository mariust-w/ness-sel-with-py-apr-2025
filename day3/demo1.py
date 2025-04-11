class Demo:

    def add(self,num1,num2):
        return num1+num2

    def add(self,num1,num2,num3):
        return num1+num2+num3

demo = Demo()
result1 = demo.add(10,20)
result2 = demo.add(10,20,30)

print(result1)
print(result2)
