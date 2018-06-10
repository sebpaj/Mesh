import numpy as np
import pylab
from PIL import Image

r_a = 0.50
r_b = 0.75
circles = 10
lines   = 100
origin = (0, 0)

for r in np.linspace(r_a,r_b,circles):
    pylab.gca().add_patch(pylab.Circle(origin, radius=r,fill=False, color='black'))

r_ab = np.array([r_a,r_b])
for theta in np.linspace(0, 2 * np.pi, lines):
    pylab.plot(np.cos(theta) * r_ab,
               np.sin(theta) * r_ab, color='red')



pylab.axis('scaled')
pylab.plot()
pylab.savefig('circle_mesh_2d.png')
