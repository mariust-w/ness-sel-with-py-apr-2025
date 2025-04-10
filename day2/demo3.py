list_of_values = [5,12,17,24,25,35]

def fun(vale):
    if vale % 2 == 0:
        return True
    else:
        return False

even_list = filter(fun, list_of_values)

print(even_list)

for vale in even_list:
    print(vale)

# v1 = (20,30,40)
# v2 = list(v1)
#
# print(v1)
# print(v2)

def getlen(wd):
    return len(wd)

cities = ['Chester','Manchester','Leichester','Liverpool']
new_list = map(getlen,cities)

for x in new_list:
    print(x)