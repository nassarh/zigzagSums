# Import stuff
import numpy as np
import zigzagsum as zs
import pyvista as pv  # for 3D rendering

# Define reference unit cell
# of an "oblique" pattern
gamma = np.pi / 3
c = np.cos(gamma)
s = np.sin(gamma)
u0 = np.array([s, c, s])
v0 = np.array([-s, c, 0])
w0 = np.array([[0, 1, 0], [c, 1, 0]])
sgnop = 1

# opening angle
theta = np.pi / 2 * 1.2

# number of cells per parallel
N = 5

# number of cells per meridian
cells = 5

# Define zigzag: two vectors + invariance by translation (the default)
u, v, _ = zs.zigzag(theta, u0=u0, v0=v0, w0=w0, sgnop=sgnop)

# Build pattern: crease vectors and vertices
U, V, W, _ = zs.manysteps(u, v, u0, v0, w0, cells, sgnop=sgnop)
X, Y, Z = zs.integrate(U, V, W, N, per=False)

# plot
pl = pv.Plotter()
pl.set_background("black", top="white")
grid = pv.StructuredGrid(X, Y, Z)
pl.add_mesh(grid, show_edges=True, line_width=3, color=[193, 225, 193])
pl.show()
