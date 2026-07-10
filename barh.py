import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5]
temperature = [22, 24, 19, 23, 25]

plt.figure(figsize=(10,8))
plt.barh(days, temperature, color='skyblue') 
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("Temperature over 5 days")
plt.grid(axis="y")
plt.show()