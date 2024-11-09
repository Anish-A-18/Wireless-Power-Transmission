
from lib import fdtd
import numpy as np
import matplotlib as plt
import os

fdtd.set_backend("numpy")
FREQUENCY = 2.4e9
SPEED_LIGHT: float = 299_792_458.0  # [m/s] speed of light
WL = SPEED_LIGHT / FREQUENCY
grid = fdtd.Grid(
    (500, 300, 1),
    grid_spacing=0.01 * WL,
    permittivity=1.0,
    permeability=1.0,
)

simfolder = grid.save_simulation("Lenses")  # initializing environment to save simulation data
print(simfolder)


#grid[60:72, 30:84, 0] = fdtd.Object(permittivity=1.7**2, name="object")
#grid[13e-6:18e-6, 5e-6:8e-6, 0] = fdtd.Object(permittivity=1.5**2)

grid[0.5*WL, 1.5*WL, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source1")
grid[0.5*WL, 1*WL, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source2")
grid[0.5*WL, 2*WL, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source3")

#grid[12e-6, :, 0] = fdtd.LineDetector(name="detector")


x1, y1 = np.arange(-120, 120, 1), np.arange(0, 17, 1)
X1, Y1 = np.meshgrid(x1,y1)

#a1,b1,c1,d1 = 6e-7, 3e-5, 0.1506, -8.6706  #grid spacing 1000
a1,b1,c1,d1 = 8e-5, -2.8e-3, +2.67e-1, -1.7339

offset1,x1a = 0,23 # 0-340
offset2,x2a = 2,32 # 0-340
offset3,x3a = 4,40 # 0-340
offset4,x4a = 8,48 # 0-340
offset5,x5a = 12,56 # 0-340
offset6,x6a = 18,64 # 0-340
offset7,x7a = 24,72 # 0-340
offset8,x8a = 32,80 # 0-340
offset9,x9a = 44,88 # 0-340
offset10,x10a = 56,96 # 0-340
offset11,x11a = 68,100 # 1060-1140
offset12,x12a = 76,104 # 1140-1200
offset13,x13a = 86,108 # 0-340
offset14,x14a = 96,112 # 1060-1140
offset15,x15a = 107,116 # 1140-1200
offset16,x16a = 120,120 # 1140-1200



# Piecewise linear conditions
conditions = [
     (abs(X1) <= x1a),
     (abs(X1) > x1a) & (abs(X1) <= x2a),
     (abs(X1) > x2a) & (abs(X1) <= x3a),
     (abs(X1) > x3a) & (abs(X1) <= x4a),
     (abs(X1) > x4a) & (abs(X1) <= x5a),
     (abs(X1) > x5a) & (abs(X1) <= x6a),
     (abs(X1) > x6a) & (abs(X1) <= x7a),
     (abs(X1) > x7a) & (abs(X1) <= x8a),
     (abs(X1) > x8a) & (abs(X1) <= x9a),
     (abs(X1) > x9a) & (abs(X1) <= x10a),
     (abs(X1) > x10a) & (abs(X1) <= x11a),
     (abs(X1) > x11a) & (abs(X1) <= x12a),
     (abs(X1) > x12a) & (abs(X1) <= x13a),
     (abs(X1) > x13a) & (abs(X1) <= x14a),
     (abs(X1) > x14a) & (abs(X1) <= x15a),
     (abs(X1) > x15a)
]

choices = [
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1),
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset2),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset3),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset4),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset5),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset6),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset7),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset8),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset9),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset10),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset11),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset12),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset13),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset14),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset15),  # Second condition: X - Y
    Y1 <= 17 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset16)  # Second condition: X - Y
]
# Use np.select to apply the piecewise function
lens_mask1 = np.select(conditions, choices)

loc1 = 150

for j, col1 in enumerate(lens_mask1.T):
    for i, val1 in enumerate(np.flip(col1)):
        if val1:
            grid[ loc1 : loc1+17-i, j+30 : j + 31, 0] = fdtd.Object(permittivity=4, name=str(i) + "," + str(j)+ "1")
            break

#lens_mask1a = np.select(conditions, choices)
#
#loc1a = 170
#for j, col1a in enumerate(lens_mask1a.T):
#    for i, val1a in enumerate(np.flip(col1a)):
#        if val1a:
#            grid[ loc1a : loc1a+17-i, j+30 : j + 31, 0] = fdtd.Object(permittivity=4, name=str(i) + "," + str(j)+ "1a")
#            break

x2, y2 = np.arange(-30, 30, 1), np.arange(0, 9, 1)
X2, Y2 = np.meshgrid(x2,y2)

# a2,b2,c2 = 0.001,-2e-7,6e-6 #grid 1000
a2,b2,c2 = 0.01,-2e-7,6e-7 #grid 100 3.5cm 9,30
#a2,b2,c2 = 0.01,-5e-7,2e-6 #grid 100 5cm wide 16,40

lens_mask2 = Y2 <= 9 - (a2 * X2 ** 2 - b2 * np.abs(X2)  + c2 )

#for j, col2 in enumerate(lens_mask2.T):
#    for i, val2 in enumerate(np.flip(col2)):
#        if val2:
#            grid[ 241+i : 250, j+120 : j + 121, 0] = fdtd.Object(permittivity=4, name=str(i) + "," + str(j)+ "2")
#            break

#grid[ 250 : 270, 124 :128, 0] = fdtd.Object(permittivity=2, name= "block3")
#grid[ 250 : 270, 128 :132, 0] = fdtd.Object(permittivity=3, name= "block4")
#grid[ 250 : 270, 132 :138, 0] = fdtd.Object(permittivity=4, name= "block5")
#grid[ 250 : 270, 138 :162, 0] = fdtd.Object(permittivity=4.5, name= "block6")
#grid[ 250 : 270, 162 :168, 0] = fdtd.Object(permittivity=4, name= "block7")
#grid[ 250 : 270, 168 :172, 0] = fdtd.Object(permittivity=3, name= "block8")
#grid[ 250 : 270, 172 :176, 0] = fdtd.Object(permittivity=2, name= "block9")



#grid[600, :, 0] = fdtd.LineDetector(name="detector1")
grid[100:450,25:275, 0] = fdtd.BlockDetector(name="detector")
# x boundaries
# grid[0, :, :] = fdtd.PeriodicBoundary(name="xbounds")
grid[0:10, :, :] = fdtd.PML(name="pml_xlow")
grid[-10:, :, :] = fdtd.PML(name="pml_xhigh")

# y boundaries
# grid[:, 0, :] = fdtd.PeriodicBoundary(name="ybounds")
grid[:, 0:10, :] = fdtd.PML(name="pml_ylow")
grid[:, -10:, :] = fdtd.PML(name="pml_yhigh")



grid.run(total_time=2000)

grid.save_data()
grid.visualize(z=0, show=True)
#import matplotlib.pyplot as plt

df = np.load(os.path.join(simfolder, "detector_readings.npz"))
fdtd.dB_map_2D(df["detector (E)"])

#fdtd.plot_detection(df["detector (E)"])
