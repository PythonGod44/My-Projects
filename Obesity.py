from matplotlib import pyplot as plt
import numpy as nmpi
xpoints=nmpi.array(['oklahoma' , 'arkansas' , 'iowa' , 'delaware' , 'kentucky' , 'indiana' , 'louisiana' , 'alabama' 'west virginia' , 'mississippi'])
ypoints=nmpi.array([36.4, 36.4, 36.5, 36.5, 36.6, 36.8, 38.1, 39, 39.1, 39.7])
plt.bar(xpoints,ypoints)
plt.ylabel('% of people who are obese')
plt.title("Parviz's Graph On People With Obesity In The US ")
plt.show()