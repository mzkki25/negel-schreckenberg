import random as rd
from matplotlib import pyplot as plt
import numpy as np

# Membuat fungsi algoritma negel schreckenberg
def negel_schreckenberg(M, prob, num_of_car, vmax, tmax):
    # inisiasi jumlah kendaraan 
    initial = [0] * num_of_car + [-1] * (M - num_of_car)
    # membuat iterasi berdasarkan jumlah kendaraan
    iteratons = [initial]
    # membuat iterasi perulangan berdasarkan waktu maksimum
    for t in range(tmax):
        # inisiasi iterasi sebelum dan sesudah kendaraan bergerak
        previous, current = iteratons[-1], [-1] * M
        # membuat perulangan berdasarkan nilai M (panjang jalan)
        for x in range(M):
            # jika nilai iterasi sebelumnya pada indeks x lebih besar -1 maka nilai kecepatan ke i adalah nilai iterasi sebelumnya pada indeks x
            if previous[x] > -1:
                vi = previous[x]
                d = 1
                # membuat perulangan berdasarkan nilai M (panjang jalan) dengan kondisi jika nilai x + d di modulo dengan M lebih kecil dari 0 maka nilai d akan bertambah
                while previous[(x + d) % M] < 0:
                    d += 1
                # inisiasi kecepatan minimum dari nilai d, nilai vi dan nilai vmax
                vTemp = min(vi + 1, d - 1, vmax)
                # penetuan nilai kecepatan baru dengan menggunakan rumus v = vTemp - 1 jika nilai random lebih kecil dari probabilitas
                if rd.uniform(0, 1) < prob:
                    vTemp = max(vTemp - 1, 0)
                # nilai kecepatan pada indeks x adalah nilai vTemp dan disimpan didalam list current
                current[(x + vTemp) % M] = vTemp
        # iterasi sebelumnya adalah iterasi saat ini
        iteratons.append(current)
    
    # membuat plot
    a = np.zeros(shape=(tmax, M))
    # membuat perulangan berdasarkan nilai tmax
    for i in range(M):
        for j in range(tmax):
            # jika nilai iterasi pada indeks i dan j lebih besar dari -1 maka nilai a pada indeks i dan j adalah 1 dan sebaliknya
            if iteratons[j][i] > -1:
                a[j][i] = 1
            else:
                a[j][i] = 0
    return a

# membuat main function untuk menjalankan fungsi negel schreckenberg dan membuat plot grafik dengan menggunakan matplotlib
def main():
    M = 100
    p = 0.3
    nc = 70
    tmax = 1000
    vmax = 5
    print(negel_schreckenberg(M, p, nc, vmax, tmax))
    plt.xlabel('Location')
    plt.ylabel('Time')
    plt.imshow(negel_schreckenberg(M, p, nc, vmax, tmax), cmap='Greys', interpolation='nearest')
    plt.show()
    
if __name__ == '__main__':
    main()