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
theta = np.pi / 2

# number of cells per parallel
N = 3

# number of cells per meridian
cells = 3 * period // 2

# Define initial zigzag
# opening theta, inclination beta, rotational symmetry of step  2 pi / N
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
