import matplotlib.pyplot as plt
import numpy as np
import math

# x-værdierne
a = [1, 2, 3, 4]
# y-værdierne
b = [1.2 ,3, 8.5, 16.3]
# rækkevidden den skal lave regression på (fra -0,5 til 5) og hvor ofte den skal opdatere (0.1)
c = [.1*x for x in range(-5,50)]

# laver en regression på 2. grad
coef = np.polyfit(a,b,2)
# laver en funktion ud fra regressionen
poly1d_fn = np.poly1d(coef)


# plotter punkterne (ro giver farve "r" er for rød, "o" er ???) og regressionen
plt.plot(a,b, 'ro', c, poly1d_fn(c), '-.c')

# navngiver x- og y-aksen
plt.ylabel('y-aksen')
plt.xlabel('x-aksen')
# sætter x- og y-akserne til at gå fra -1 til 6 og 0 til 30
plt.xlim(-1, 6)
plt.ylim(0, 30)

plt.show()