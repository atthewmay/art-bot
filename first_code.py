import matplotlib.pyplot as plt

class ArtCart():
    def __init__(self):
        self.position = [5,5]
        self.diameter = 10
        self.color = 'b'

ac = ArtCart()

size = [10,10]
fig = plt.figure(figsize = (size[0],size[1]))
ax = fig.add_subplot(111)
for i in range(1000):
    ac.position[0] +=0.1
    ac.position[1] +=0.1
    ax.clear()
    # self.ax.autoscale(enable = False)
    ax.set_xlim(left = 0, right = size[0],auto = False)
    ax.set_ylim(0,size[1], auto = False)
    ax.scatter(ac.position[0],ac.position[1], c=ac.color)

    plt.pause(0.01)
