from matplotlib import pyplot as plt
import numpy as nmpi
xpoints=nmpi.array(['missouri' , 'mississippi' , 'north carolina' , 'tennessee' , 'oklahoma' , 'alabama' , 'louisiana' , 'arkansas' , 'kentucky' , 'west virginia'])
ypoints=nmpi.array([5.1,5.3,5.7,5.7,5.8,6.1,6.0,6.4,6.3,8.3])
plt.bar(xpoints,ypoints)
plt.xlabel('states')
plt.ylabel('% of people having heart disease')
plt.title("Parviz's Graph On Top 10 States With Heart Disease")
plt.show()