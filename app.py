import matplotlib.pyplot as plt
#import numpy as nmpi

x = ["california", "florida", "texas", "washington", "new york", "new jersey", "arizona", "colorado", "illinois",
     "georgia"]
y = [563070, 95640, 80900, 66810, 51870, 47830, 40740, 37000, 36520, 3420]
plt.bar(x,y)
for i in range(len(x)):
 plt.text(i,y[i],y[i],ha = "center" , va = "bottom")
plt.xlabel("States",weight='bold',
           size = 16,)
plt.ylabel("# of Electric Cars",weight='bold',
           size = 16,)
plt.title("Parviz's Graph On Electric Cars In The US ")
plt.show()
