
import fdtd
import numpy as np
import matplotlib as plt
import os

fdtd.set_backend("numpy")
FREQUENCY = 2.4e9
SPEED_LIGHT: float = 299_792_458.0  # [m/s] speed of light
WAVELENGTH = SPEED_LIGHT / FREQUENCY
grid = fdtd.Grid(
    (1000, 1000, 1),
    grid_spacing=0.01 * WAVELENGTH,
    permittivity=1.0,
    permeability=1.0,
)

simfolder = grid.save_simulation("Lenses")  # initializing environment to save simulation data
print(simfolder)


#grid[60:72, 30:84, 0] = fdtd.Object(permittivity=1.7**2, name="object")
#grid[13e-6:18e-6, 5e-6:8e-6, 0] = fdtd.Object(permittivity=1.5**2)

grid[200, 500, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source1")
grid[200, 550, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source2")
grid[200, 450, 0] = fdtd.PointSource(period = 1 /FREQUENCY, name="source3")

#grid[12e-6, :, 0] = fdtd.LineDetector(name="detector")

x, y = np.arange(-100, 100, 1), np.arange(50, 100, 1)
X, Y = np.meshgrid(x, y)
lens_mask = X ** 2 + Y ** 2 <= 10000
for j, col in enumerate(lens_mask.T):
    for i, val in enumerate(np.flip(col)):
        if val:
            grid[ 350 : 400-i, j+400 : j + 401, 0] = fdtd.Object(permittivity=2 ** 2, name=str(i) + "," + str(j))
            break

#grid[600, :, 0] = fdtd.LineDetector(name="detector")
grid[300:500,400:600, 0] = fdtd.BlockDetector(name="detector")
# x boundaries
# grid[0, :, :] = fdtd.PeriodicBoundary(name="xbounds")
grid[0:10, :, :] = fdtd.PML(name="pml_xlow")
grid[-10:, :, :] = fdtd.PML(name="pml_xhigh")

# y boundaries
# grid[:, 0, :] = fdtd.PeriodicBoundary(name="ybounds")
grid[:, 0:10, :] = fdtd.PML(name="pml_ylow")
grid[:, -10:, :] = fdtd.PML(name="pml_yhigh")



grid.run(total_time=1000)

grid.save_data()
grid.visualize(z=0, show=True)
#import matplotlib.pyplot as plt

df = np.load(os.path.join(simfolder, "detector_readings.npz"))
fdtd.dB_map_2D(df["detector (E)"])
