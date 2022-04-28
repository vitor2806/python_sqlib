import matplotlib.pyplot as plt

data = open('populacao_brasileira.csv').readlines()

x = []
y = []

for line in range(len(data)):
    if(line != 0):
        line = data[line].split(';')
        x.append(int(line[0]))
        y.append(int(line[1]))
plt.title('Brazil Birth Rate')
plt.xlabel('Year')
plt.ylabel('Population x100.000.000')
plt.bar(x, y, color='#e5e5e5')
plt.plot(x, y, color='k')
plt.show()

