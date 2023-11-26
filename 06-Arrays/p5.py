import matplotlib.pyplot as plt

transport = [["Car",25],["Public",19],["Bike",32],["Foot",7]]

xpoints = ["Car", "Public","Bike","Foot"]
ypoints = [25,19,32,7]

plt.bar(xpoints, ypoints)
plt.show()