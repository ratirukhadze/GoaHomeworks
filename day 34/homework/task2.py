temperatures = list[72,68,75,70,78,74,71]

temperatures.max()
print(temperatures)

temperatures.min()
print(temperatures)

average_temp = sum(temperatures) / len(temperatures)
print(average_temp) 

above_70 = [temp for temp in temperatures if temp > 70]
print(above_70)


