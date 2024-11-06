def short_bubble_sort(alist):
    # Variabel untuk memeriksa apakah ada pertukaran yang terjadi
    exchanges = True
    # Menghitung jumlah elemen dalam list
    passnum = len(alist) - 1

    # Selama passnum lebih besar dari 0 dan ada pertukaran
    while passnum > 0 and exchanges:
        # Setel exchanges ke False sebelum memulai perulangan baru
        exchanges = False
        # Perulangan untuk membandingkan elemen yang berdekatan
        for i in range(passnum):
            # Cek apakah elemen yang ada lebih besar daripada elemen berikutnya
            if alist[i] > alist[i + 1]:
                # Tandakan bahwa ada pertukaran
                exchanges = True
                # Simpan nilai alist[i] sementara
                temp = alist[i]
                # Tukar dengan nilai alist[i+1]
                alist[i] = alist[i + 1]
                # Simpan nilai sementara di alist[i+1]
                alist[i + 1] = temp
                # Kurangi passnum untuk memfokuskan perbandingan pada bagian yang belum terurut
                passnum = passnum - 1


alist=[20,30,40,90,50,60,70,80,100,110]
short_bubble_sort(alist)
print(alist)