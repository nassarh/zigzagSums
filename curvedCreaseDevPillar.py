# Import stuff
import numpy as np
import zigzagsum as zs
import pyvista as pv  # for 3D rendering

# Define reference unit cell
# of "curved crease Miura ori-esque" pattern
# alternative orientation
period = 40
gamma = np.linspace(-np.pi, np.pi, period)
s = np.sin(gamma)
u0 = np.array([1, 0, 0])
v0 = np.array([-1, 0, 0])
w0 = np.vstack([s, np.ones(period), np.zeros(period)]).T / period * 2

sgnop = -1

# opening angle at initial zigzag
theta = np.pi * 0.96

# inclination angle at initial zigzag
beta = -np.pi/5

# number of cells per parallel
N = 120

# number of cells per meridian
cells = 30 * period // 2

# Define initial zigzag
# opening theta, inclination beta, rotational symmetry of step  2 pi / N
u, v, rot, _ = zs.zigcircle(theta, beta, N, u0=u0, v0=v0, w0=w0, sgnop=sgnop)

# Build pattern: crease vectors and vertices
U, V, W, _ = zs.manysteps(u, v, u0, v0, w0, cells, sgnop=sgnop, rot=rot)
X, Y, Z = zs.integrate(U, V, W, N, per=True, rot=rot)

# plot
pl = pv.Plotter()
pl.set_background("black", top="white")
grid = pv.StructuredGrid(X, Y, Z)
pl.add_mesh(grid, show_edges=True, line_width=3, color=[193, 225, 193])
pl.show()
