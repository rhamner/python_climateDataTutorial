from netCDF4 import Dataset
import matplotlib.pyplot as plt

#open reference to the file and see overview of it
data = Dataset("File Name/Path Goes Here.nc", "r");
print(data.variables.items())

#pull the data from file into variables
lon = data.variables['longitude'][:];
lat = data.variables['latitude'][:];
anomaly = data.variables['temperature'][:];
reference = data.variables['climatology'][:];

#grab January 31, 2000 data and convert from C to F
data = anomaly[31, :, :] + reference[31, :, :];
data = (1.8*data) + 32;

#plot global max temp
plt.figure(1)
plt.contourf(lon, lat, data)
plt.colorbar()
plt.ylabel('latitude')
plt.xlabel('longitude')
plt.title('Max Temp (F) on January 31, 2000')

#plot US max temp
plt.figure(2)
plt.contourf(lon[50:125], lat[115:135], data[115:135, 50:125])
plt.colorbar()
plt.ylabel('latitude')
plt.xlabel('longitude')
plt.title('Max Temp (F) on January 31, 2000')
plt.show()



