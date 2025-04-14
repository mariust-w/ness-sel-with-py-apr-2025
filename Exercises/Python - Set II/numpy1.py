import numpy as np

cities = ['London', 'Tokyo', 'Sydney', 'Cairo', 'Dubai']

temp_data = np.random.randint(10, 30, size=(5, 3))
print(temp_data)

for i, city in enumerate (cities):
    print(f"{city}: {temp_data[i][0]} {temp_data[i][1]} {temp_data[i][2]}")
    print(f"{city} avg = {np.average(temp_data[i])}")

avg_temp = np.average(temp_data)
print(avg_temp)