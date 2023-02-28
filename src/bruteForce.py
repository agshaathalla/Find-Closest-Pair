import function as f

def bruteForce(array, n, d, count):
    a = 9999999999999999

    titik = []
    for i in range (n):
        for j in range (n):
            if (i!=j):
                matriks = f.buatPembanding(array, i, j, d)
                eucledian, matriks, count = f.nilaiEuclidean(matriks, d, count)
                if (eucledian < a):
                    a = eucledian
                    titik = [array[i], array[j]]
    return a, titik, count