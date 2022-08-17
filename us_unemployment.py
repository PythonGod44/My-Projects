

from matplotlib import pyplot as plt

x = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
y = [6.0, 5.7, 5.4, 4.9, 4.4, 5.0, 7.3, 9.9, 9.3,8.6,7.9,6.7,5.6,5.0,4.7,4.1,3.9,3.6,6.7,3.9,3.5]

plt.plot(x,y)
plt.xlabel('Years')
plt.ylabel('Unemployment Rate')
plt.title("Parviz's Graph on US unemployment since 2002" )
plt.show()
