import function as f

def Sstrip(distance, array, n, d, titikSebelumnya, count):
    if (len(array) % 2 == 0):
        mid = len(array) // 2
        t = (array[mid][0] + array[mid+1][0])/2
    else:
        mid = len(array) // 2
        t = array[mid+1][0]
    A = []
    for i in range(n):
        if ((array[i][0] >= (t-distance)) and (array[i][0] <= (distance+t))):
            A.append(array[i])
    
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if(abs(A[i][0]-A[j][0])<distance):
                B = [A[i], A[j]]
                jarakBaru, titikBaru, count = f.nilaiEuclidean(B,d,count)
                if (jarakBaru < distance):
                    distance = jarakBaru
                    titikSebelumnya = B
    return distance, titikSebelumnya, count

def FindClosestPair(array, n, d, count):
    if n==2:
        distance, titik, count = f.nilaiEuclidean(array, d, count)
    elif n==3:
        arr1 = [array[0], array[1]]
        arr2 = [array[0], array[2]]
        arr3 = [array[1], array[2]]
        d1, titik1, count = f.nilaiEuclidean(arr1, d, count)
        d2, titik2, count = f.nilaiEuclidean(arr2, d, count)
        d3, titik3, count = f.nilaiEuclidean(arr3, d, count)

        if (d1 <= d2 and d1 <= d3):
            distance = d1
            titik = titik1
        elif (d2 <= d1 and d2 <= d3):
            distance = d2
            titik = titik2
        elif (d3 <= d1 and d3 <= d2):
            distance = d3
            titik = titik3

    else:
        kiri, kanan = f.divide(array, n, d)
        dKiri, titikKiri, count = FindClosestPair(kiri, len(kiri), d, count)
        dKanan, titikKanan, count = FindClosestPair(kanan, len(kanan), d, count)
        distance = f.minimum(dKiri, dKanan)
        titik = []
        if (distance == dKiri):
            titik = titikKiri
        elif (distance == dKanan):
            titik = titikKanan
        distance, titik, count = Sstrip(distance, array, n, d, titik, count)
    return distance, titik, count