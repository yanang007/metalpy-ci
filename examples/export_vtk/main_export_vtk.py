import numpy as np
import pyvista as pv
from discretize import TensorMesh

from metalpy.scab.modelling.scene import Scene
from metalpy.scab.modelling.shapes import Cuboid, Prism, Ellipsoid, Tunnel, Obj2


def main():
    scene = Scene.of(
        Cuboid([1, 1, 1], size=2),
        Prism([[0, 0], [-2, 0], [-2, 1], [-1, 1]], 1, 3),
        Prism([[0, 0], [-2, 0], [-2, 1], [-1, 1]], 1, 3).rotated(90, 0, 0),
        Ellipsoid.spheroid(1, 3, 0).translated(0, -2, 2),
        Tunnel([-3, 2, 2], 0.5, 1, 3),
        Obj2('../obj/stl_models/mine.stl', scale=0.03).translated(1, -2, -1),
    )

    mesh = TensorMesh([[(0.2, 50)], [(0.2, 50)], [(0.2, 50)]], origin=(-5, -5, -5))
    ind_active = scene.build(mesh)
    grids = mesh.to_vtk(models={'active': ind_active.astype(np.int32)})
    grids.set_active_scalars('active')

    p = pv.Plotter(shape=(1, 3))

    models = scene.to_multiblock()
    active_grids = grids.threshold([1, 1])

    p.subplot(0, 0)
    p.add_mesh(models)
    p.show_grid()
    p.show_axes()

    c = p.camera.position

    p.subplot(0, 1)
    p.add_mesh(active_grids, show_edges=True)
    p.show_grid()
    p.show_axes()

    p.subplot(0, 2)
    p.add_mesh(models, opacity=0.2)
    p.add_mesh(active_grids, show_edges=True)
    p.show_grid()
    p.show_axes()

    p.link_views()
    p.renderers[0].camera.position = c
    p.show()


if __name__ == '__main__':
    main()