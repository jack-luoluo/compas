# no breakpoints

import compas
from compas.datastructures import FaceNetwork
from compas.datastructures import network_find_faces
from compas.visualization import NetworkPlotter

network = FaceNetwork.from_obj(compas.get_data('grid_irregular.obj'))

network_find_faces(network)

plotter = NetworkPlotter(network)

plotter.draw_vertices(radius=0.075, facecolor={key: '#cccccc' for key in network.leaves()})
plotter.draw_edges(color={(u, v): '#cccccc' for u, v in network.edges()})
plotter.draw_faces(facecolor={fkey: '#eeeeee' for fkey in network.faces()}, text={fkey: fkey for fkey in network.faces()})

plotter.show()