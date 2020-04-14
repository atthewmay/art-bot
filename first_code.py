import matplotlib.pyplot as plt

class ArtCart():
    def __init__(self):
        self.position = [0,0]

ac = ArtCart()
for i in range(10):
    ac.position[0] +=1
    ac.position[1] +=1
    plt.figure()
    plt.scatter(ac.position[0],ac.position[1])
    plt.show()
    plt.close()
