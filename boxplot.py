import matplotlib.pyplot as plt
import random

arr = [random.randint(0, 10000) for number in range(50)]
plt.boxplot(arr)
plt.show()