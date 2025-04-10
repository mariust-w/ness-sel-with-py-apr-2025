
def demo_exception(num1,num2):
        try:
                di = num1 / num2
        except ZeroDivisionError:
                di = num1
        else:
                print('Inside else block')
        finally:
                print('Inside finally block')
        return di

print(demo_exception(100,0))
print(demo_exception(100,2))
