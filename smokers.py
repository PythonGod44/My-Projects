from matplotlib import pyplot as plt
import numpy as nmpi
xpoints=nmpi.array(['alaska' , 'mississippi' , 'guam' , 'tennessee' , 'indiana' , 'oklahoma' , 'ohio' , 'arkansas' , 'kentucky' , 'west virginia'])
ypoints=nmpi.array([17,17,17,18,18,18,19,19,20,22])
plt.bar(xpoints,ypoints)
plt.xlabel('states')
plt.ylabel('% of people who smoke')
plt.title("Parviz's Graph On Top 10 States With People That Smoke")
plt.show()
