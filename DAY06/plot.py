from matplotlib import pyplot as plt
import numpy as np


plt.style.use('fivethirtyeight')
plt.xkcd()

# x = np.arange(9)
# y = np.arange(9,18)

# plt.plot(x,y)
# plt.show()


x = np.arange(0,4*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")

plt.title('represent sin cosine values')
plt.xlabel('Angles')
plt.ylabel('sin cos values')
plt.legend()
plt.savefig('plot.png')
# plt.show()







