import function as f
import divideAndConquer as dnc
import bruteForce as bf
import time
import showGraph as sg
import splashScreen as ss
import os

def main():
    os.system('cls')
    ss.splashScreen()
    euclideanCount = 0
    n, d, matriks = f.inputan()
    matriks = f.sortByX(matriks, n)
    detik1 = time.time()
    jarak, titik, count = dnc.FindClosestPair(matriks, n, d, euclideanCount)
    print('''
_________________________________________________________________________

                        ALGORITMA DIVIDE AND CONQUER
    ''')
    print("\n")
    print("jarak terdekat = ",jarak)
    print("titik = ",titik)
    detik2 = time.time()
    print("execute time = ",detik2-detik1, " seconds")
    print("euclidean count = ",count)
    print("\n")
    print("_________________________________________________________________________")
    print('''
                            ALGORITMA BRUTE FORCE
    ''')

    detikBF1 = time.time()
    jarak1, titik1, count = bf.bruteForce(matriks, n, d, 0)
    print("jarak brute force = ",jarak1)
    print("titik brute force = ",titik1)
    detikBF2 = time.time()
    print("execute time brute force = ",detikBF2-detikBF1, " seconds")
    print("euclidean count = ",count)
    print("\n")
    print("_________________________________________________________________________")

    print('''
                                 VISUALISASI
    ''')

    if (d==2 or d==3):
        y = str(input("Apakah anda ingin memvisualisasikan hasil pengerjaan? (y/n) "))
        while (y!='y' and y!='n'):
            print("masukan salah")
            y = str(input("Apakah anda ingin memvisualisasikan hasil pengerjaan? (y/n) "))
        if (y == 'y'):
            print("Visualisasi akan ditampilkan. Titik merah menunjukkan pasangan titik terdekat")
            print("Harap menutup layar visualisasi setelah selesai untuk melanjutkan program")
            sg.visualisasi(matriks, titik, n, d)
            
    else:
        print("Anda tidak dapat memvisualisasikan hasil pengerjaan karena bukan dalam dimensi 2 (dua) atau 3 (tiga)")
    
    print("\n")
    print("_________________________________________________________________________")

    y = str(input("Apakah anda ingin mencoba kembali? (y/n) "))
    while (y!='y' and y!='n'):
        print("masukan salah")
        y = str(input("Apakah anda ingin mencoba kembali? (y/n) "))
    if (y == 'y'):
        main()
    elif (y == 'n'):
        os.system('cls')
        ss.splashScreen()
        print("                         🙏Terima kasih telah menggunakan program ini 🙏")
        print('''
        
        ------------------------------------------------------------------------------
                Rasa ingin menyerah itu wajar, tetapi menyerah bukan keputusan 
                 yang tepat untuk seorang manusia super tangguh sepertimu.
                       Tetaplah melangkah, walau harus merubah arah

                                -Martabak Legit Group-
        ------------------------------------------------------------------------------

        
        ''')
        d = input("tekan enter untuk menutup program...")
        
if __name__ == "__main__":
    main()