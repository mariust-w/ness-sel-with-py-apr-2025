'''

def add(num1,num2):
    # print(num1+num2)
    return num1+num2

result = add(10,20)
print(result)

def mul(num1,num2):
    pass

def sum(*num):
    print(num)
    print(type(num))

sum(10,20)
sum(1,2,3,)
sum(1,2,3,4,5)
'''

def sayhi(**kwargs):
    print(f'Hi {kwargs["firstname"]+" "+kwargs["lastname"] }')

sayhi(firstname="Ivan", lastname="Lendl")

mark_list = [90,80,70,98,88]
print(min(mark_list))
print(max(mark_list))

print(eval('100+200*90'))