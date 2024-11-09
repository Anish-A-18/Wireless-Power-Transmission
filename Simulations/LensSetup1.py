
import fdtd
import numpy as np
import matplotlib as plt
import os

fdtd.set_backend("numpy")
FREQUENCY = 2.4e9
SPEED_LIGHT: float = 299_792_458.0  # [m/s] speed of light
WAVELENGTH = SPEED_LIGHT / FREQUENCY
grid = fdtd.Grid(
    (5000, 3000, 1),
    grid_spacing=0.001 * WAVELENGTH,
    permittivity=1.0,
    permeability=1.0,
)

#simfolder = grid.save_simulation("Lenses")  # initializing environment to save simulation data
#print(simfolder)


#grid[60:72, 30:84, 0] = fdtd.Object(permittivity=1.7**2, name="object")
#grid[13e-6:18e-6, 5e-6:8e-6, 0] = fdtd.Object(permittivity=1.5**2)

grid[500, 1500, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source1")
grid[500, 1000, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source2")
grid[500, 2000, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source3")

#grid[12e-6, :, 0] = fdtd.LineDetector(name="detector")


x1, y1 = np.arange(-1200, 1200, 1), np.arange(0, 160, 1)
X1, Y1 = np.meshgrid(x1,y1)

a1,b1,c1,d1 = 6e-7, 3e-5, 0.1506, -8.6706

offset1,x1a = 0,230 # 0-340
offset2,x2a = 16,320 # 0-340
offset3,x3a = 40,400 # 0-340
offset4,x4a = 80,480 # 0-340
offset5,x5a = 120,560 # 0-340
offset6,x6a = 176,640# 0-340
offset7,x7a = 240,720 # 0-340
offset8,x8a = 320,800 # 0-340
offset9,x9a = 440,880 # 0-340
offset10,x10a = 560,960 # 0-340
offset11,x11a = 680,1000 # 1060-1140
offset12,x12a = 760,1040 # 1140-1200
offset13,x13a = 856,1080 # 0-340
offset14,x14a = 960,1120 # 1060-1140
offset15,x15a = 1072,1160 # 1140-1200
offset16,x16a = 1200,1200 # 1140-1200



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
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1),
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset2),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset3),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset4),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset5),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset6),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset7),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset8),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset9),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset10),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset11),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset12),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset13),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset14),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset15),  # Second condition: X - Y
    Y1 <= 160 - (a1 * np.abs(X1 ** 3) + b1 * X1 ** 2 + c1 * np.abs(X1) + d1 - offset16)  # Second condition: X - Y
]
# Use np.select to apply the piecewise function
lens_mask1 = np.select(conditions, choices)

for j, col1 in enumerate(lens_mask1.T):
    for i, val1 in enumerate(np.flip(col1)):
        if val1:
            grid[ 1500 : 1660-i, j+300 : j + 301, 0] = fdtd.Object(permittivity=4, name=str(i) + "," + str(j)+ "1")
            break


x2, y2 = np.arange(-300, 300, 1), np.arange(0, 90, 1)
X2, Y2 = np.meshgrid(x2,y2)

a2,b2,c2 = 0.001,-2e-7,6e-6

lens_mask2 = Y2 <= 90 - (a2 * X2 ** 2 - b2 * np.abs(X2)  + c2 )

for j, col2 in enumerate(lens_mask2.T):
    for i, val2 in enumerate(np.flip(col2)):
        if val2:
            grid[ 3160+i : 3250, j+1200 : j + 1201, 0] = fdtd.Object(permittivity=4, name=str(i) + "," + str(j)+ "2")
            break

grid[ 3251 : 3450, 1240 :1280, 0] = fdtd.Object(permittivity=2, name= "block3")
grid[ 3251 : 3450, 1281 :1320, 0] = fdtd.Object(permittivity=3, name= "block4")
grid[ 3251 : 3450, 1321 :1380, 0] = fdtd.Object(permittivity=4, name= "block5")
grid[ 3251 : 3450, 1381 :1620, 0] = fdtd.Object(permittivity=4.5, name= "block6")
grid[ 3251 : 3450, 1621 :1680, 0] = fdtd.Object(permittivity=4, name= "block7")
grid[ 3251 : 3450, 1680 :1720, 0] = fdtd.Object(permittivity=3, name= "block8")
grid[ 3251 : 3450, 1721 :1760, 0] = fdtd.Object(permittivity=2, name= "block9")
#grid[600, :, 0] = fdtd.LineDetector(name="detector")
grid[4000:4500,1000:2000, 0] = fdtd.BlockDetector(name="detector")
# x boundaries
# grid[0, :, :] = fdtd.PeriodicBoundary(name="xbounds")
grid[0:100, :, :] = fdtd.PML(name="pml_xlow")
grid[-100:, :, :] = fdtd.PML(name="pml_xhigh")

# y boundaries
# grid[:, 0, :] = fdtd.PeriodicBoundary(name="ybounds")
grid[:, 0:100, :] = fdtd.PML(name="pml_ylow")
grid[:, -100:, :] = fdtd.PML(name="pml_yhigh")



grid.run(total_time=1000)

#grid.save_data()
grid.visualize(z=0, show=True)
#import matplotlib.pyplot as plt

#df = np.load(os.path.join(simfolder, "detector_readings.npz"))
#fdtd.dB_map_2D(df["detector (E)"])