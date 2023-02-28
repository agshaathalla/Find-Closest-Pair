import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import bruteForce as t

def inputan():
    n = int(input("Masukkan banyaknya titik: "))
    while (n<=1):
        print("Banyaknya titik tidak boleh kurang dari 2!")
        n = int(input("Masukkan banyaknya titik: "))
    d = int(input("Masukkan banyaknya dimensi: "))
    while (d<1):
        print("Banyaknya dimensi tidak boleh kurang dari 1!")
        d = int(input("Masukkan banyaknya dimensi: "))

    matriks = [[float(0) for j in range(d)]for i in range(n)]
    for i in range(n):
        for j in range(d):
            matriks[i][j] = round(random.uniform(-100, 100),3)
    return n, d, matriks

def buatPembanding(array, pertama, kedua, d):
    arrayPembanding = [[0 for j in range(d)]for i in range(2)]
    for j in range(d):
        arrayPembanding[0][j] = array[pertama][j]
        arrayPembanding[1][j] = array[kedua][j]
    return arrayPembanding

def nilaiEuclidean(array,d,euclideanCount):
    sum = 0
    arrayPembanding = array
    for j in range(d):
        sum += (array[0][j] - array[1][j])**2
    sum = math.sqrt(sum)
    euclideanCount += 1
    return sum, arrayPembanding, euclideanCount

def nilaiEuclidean3(array,d, count):
    shortest = 99999999
    titik = [[0 for i in range(d)] for i in range(2)]
    for i in range(3):
        for j in range(3-i):
            if (i!=j):
                bandingkan = buatPembanding(array, i, j, d)
                eucledian, a, count = nilaiEuclidean(bandingkan, d, count)
                if (eucledian < shortest):
                    shortest = eucledian
                    titik = a
    return shortest, titik
    
def sortByX(array, n):
    for i in range(n):
        for j in range(n-i-1):
            if array[j][0] > array[j+1][0]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def minimum(a,b):
    if (a<b):
        return a
    else:
        return b

def divide(array, n, d):
    M1 = []
    M2 = []
    for i in range(n):
        if (i < n//2):
            M1.append(array[i])
        else:
            M2.append(array[i])
    return M1, M2