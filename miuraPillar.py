# Import stuff
import numpy as np
import zigzagsum as qd
import pyvista as pv  # for 3D rendering

# Define reference unit cell
# of "equilateral" Miura ori
gamma = np.pi / 3
c = np.cos(gamma)
s = np.sin(gamma)
u0 = np.array([s, c, 0])
v0 = np.array([-s, c, 0])
w0 = np.array([0, 1, 0])
wb0 = np.array([0, 1, 0])
sgnop = 1

# opening angle at initial zigzag
theta = np.pi / 3

# inclination angle at initial zigzag
beta = -np.pi / 6

# number of cells per parallel
N = 30

# number of cells per meridian
cells = 20

# Define initial zigzag
# opening theta, inclination beta, rotational symmetry of step  2 pi / N
u, v, rot, _ = qd.zigcircle(theta, beta, N=N, u0=u0, v0=v0, w0=w0, wb0=wb0, sgnop=sgnop)

# Build pattern: crease vectors and vertices
U, V, W, _ = qd.manysteps(u, v, u0, v0, w0, wb0, cells, sgnop=sgnop, rot=rot)
X, Y, Z = qd.integrate(U, V, W, N, per=True, rot=rot)

# plot
pl = pv.Plotter()
pl.set_background("black", top="white")
grid = pv.StructuredGrid(X, Y, Z)
pl.add_mesh(grid, show_edges=True, line_width=3, color=[193, 225, 193])
pl.show()
