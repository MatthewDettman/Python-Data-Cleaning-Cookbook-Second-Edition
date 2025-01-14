# import pandas, matplotlib, and seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.width', 53)
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 200)
pd.options.display.float_format = '{:,.0f}'.format
landtemps = pd.read_csv("data/landtemps2023avgs.csv")

# run a scatter plot latitude by avgtemp
plt.scatter(x="latabs", y="avgtemp", data=landtemps)
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature (Celsius)")
plt.yticks(np.arange(-60, 40, step=20))
plt.title("Latitude and Average Temperature in 2023")
plt.show()

landtemps.shape

# show the high elevation points in a different color
low, high = landtemps.loc[landtemps.elevation<=1000], landtemps.loc[landtemps.elevation>1000]
plt.scatter(x="latabs", y="avgtemp", c="blue", data=low)
plt.scatter(x="latabs", y="avgtemp", c="red", data=high)
plt.legend(('low elevation', 'high elevation'))
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature (Celsius)")
plt.title("Latitude and Average Temperature in 2023")
plt.show()

# show this as a 3D plot
fig = plt.figure()
plt.suptitle("Latitude, Temperature, and Elevation in 2023")
ax = plt.axes(projection='3d')
ax.set_xlabel("Elevation")
ax.set_ylabel("Latitude")
ax.set_zlabel("Avg Temp")
ax.scatter3D(low.elevation, low.latabs, low.avgtemp, label="low elevation", c="blue")
ax.scatter3D(high.elevation, high.latabs, high.avgtemp, label="high elevation", c="red")
ax.legend()
plt.show()

# show scatter plot with a regression line
sns.regplot(x="latabs", y="avgtemp", color="blue", data=landtemps)
plt.title("Latitude and Average Temperature in 2023")
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature")
plt.show()

# show scatter plot with different regression lines by elevation group
landtemps['elevation'] = np.where(landtemps.elevation<=1000,'low','high')
sns.lmplot(x="latabs", y="avgtemp", hue="elevation", palette=dict(low="blue", high="red"),  facet_kws=dict(legend_out=False), data=landtemps)
plt.xlabel("Latitude (N or S)")
plt.ylabel("Average Temperature")
plt.yticks(np.arange(-60, 40, step=20))
plt.title("Latitude and Average Temperature in 2023")
plt.show()

# check some average temperatures above the regression lines
high.loc[(high.latabs>38) & \
  (high.avgtemp>=18),
  ['station','country','latabs',
  'elevation','avgtemp']]
low.loc[(low.latabs>47) & \
  (low.avgtemp>=14),
  ['station','country','latabs',
  'elevation','avgtemp']]

# check some average temperatures below the regression lines
high.loc[(high.latabs<5) & \
  (high.avgtemp<18),
  ['station','country','latabs',
  'elevation','avgtemp']]
low.loc[(low.latabs<50) & \
  (low.avgtemp<-9),
  ['station','country','latabs',
  'elevation','avgtemp']]

