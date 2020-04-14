import matplotlib.pyplot as plt

class ArtCart():
    def __init__(self):
        self.position = [0,0]

ac = ArtCart()
plt.figure()
plt.scatter(ac.position[0],ac.position[1])
plt.show()
