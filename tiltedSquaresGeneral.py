# Import stuff
import numpy as np
import zigzagsum as zs
import pyvista as pv  # for 3D rendering

# Define reference unit cell
# of "tilted squares" pattern
gamma = np.pi / 3
c = np.cos(gamma)
s = np.sin(gamma)
u0 = np.array([1, 0, 0])
v0 = np.array([-s, c, 0])
w0 = np.array([[0, 1, 0], [c, s, 0]])
sgnop = 1

# opening angle at initial zigzag
theta = np.pi / 2

# inclination angle at initial zigzag
beta = -np.pi / 6

# number of cells per parallel
N = 30

# number of cells per meridian
cells = 20

# Define initial zigzag
# opening theta, inclination beta
u, v, _, _ = zs.zigcircle(theta, beta, N=N, u0=u0, v0=v0, w0=w0, sgnop=sgnop)

# define rotational symmetry by a general rotation
# axis
p = np.array([1, 1, 1])
p = p / np.sqrt(3)
P = np.array([[0, -p[2], p[1]], [p[2], 0, -p[0]], [-p[1], p[0], 0]])

# angle
dphi = 2 * np.pi / N

# rotation
rot = np.eye(3) + np.sin(dphi) * P + (1 - np.cos(dphi)) * np.dot(P, P)

# Build pattern: crease vectors and vertices
U, V, W, _ = zs.manysteps(u, v, u0, v0, w0, cells, sgnop=sgnop, rot=rot)
X, Y, Z = zs.integrate(U, V, W, N, per=False, rot=rot)

# plot
pl = pv.Plotter()
pl.set_background("black", top="white")
grid = pv.StructuredGrid(X, Y, Z)
pl.add_mesh(grid, show_edges=True, line_width=3, color=[193, 225, 193])
pl.show()
