import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def visualisasi(titikAsal, titikAkhir, n, d):
    fig = plt.figure(figsize=(12,15))
    if(n>2):
        titikAsal.remove(titikAkhir[0])
        titikAsal.remove(titikAkhir[1])

    titikAsal = np.array(titikAsal)
    titikAkhir = np.array(titikAkhir)

    if(d==3):
        ax = plt.axes(projection='3d')

        x = titikAsal[:,0]
        y = titikAsal[:,1]
        z = titikAsal[:,2]
        x1 = titikAkhir[:,0]
        y1 = titikAkhir[:,1]
        z1 = titikAkhir[:,2]

        ax.scatter(x,y,z, s=10, color='grey')
        ax.scatter(x1, y1, z1, s=20, color='red')

        plt.show()

    elif (d==2):

        x = titikAsal[:,0]
        y = titikAsal[:,1]
        x1 = titikAkhir[:,0]
        y1 = titikAkhir[:,1]

        plt.scatter(x,y, s = 10, color='grey')
        plt.scatter(x1, y1, s = 20, color='red')

        plt.show()