def bubble_sort(alist):
    # perulangan dari nilai list terakhir sampai awal
    for passnum in range(len(alist) - 1, 0, -1):
        # perulangan hingga nilai passnum (passnum pasti nilai terbesar di list)
        for i in range(passnum):
            # cek nilai alist dengan index sebelah kanannya apakah lebih besar
            if alist[i] > alist[i + 1]:
                # temporary (menyimpan nilai alist sementara)
                temp = alist[i]
                # tukar dengan nilai sebelahnya
                alist[i] = alist[i + 1]
                # maka nilai temp diubah agar cek nya nanti dari nilai temp
                alist[i + 1] = temp


alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)
print(alist)
