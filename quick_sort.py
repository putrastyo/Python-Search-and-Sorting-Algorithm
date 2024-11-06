# Fungsi utama yang memulai proses QuickSort
def quickSort(alist):
    # Panggil helper function dengan parameter first dan last sebagai indeks awal dan akhir
    quickSortHelper(alist, 0, len(alist) - 1)

# Fungsi untuk membantu membagi dan menyortir bagian dari list
def quickSortHelper(alist, first, last):
    # Cek apakah first lebih kecil dari last untuk memastikan ada elemen untuk disortir
    if first < last:
        # Panggil partition untuk membagi list dan mendapatkan titik pemisah
        splitpoint = partition(alist, first, last)
        # Rekursif untuk bagian kiri dari pivot
        quickSortHelper(alist, first, splitpoint - 1)
        # Rekursif untuk bagian kanan dari pivot
        quickSortHelper(alist, splitpoint + 1, last)

# Fungsi partition untuk membagi list dan menempatkan pivot pada posisi yang benar
def partition(alist, first, last):
    # Tentukan pivot sebagai elemen pertama dari list
    pivotvalue = alist[first]
    # Tentukan penanda untuk kiri dan kanan
    leftmark = first + 1
    rightmark = last
    # Flag untuk mengetahui apakah proses pembagian sudah selesai
    done = False
    # Proses pembagian list berdasarkan pivot
    while not done:
        # Geser leftmark ke kanan selama nilai leftmark lebih kecil atau sama dengan pivot
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        # Geser rightmark ke kiri selama nilai rightmark lebih besar atau sama dengan pivot
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        # Jika rightmark lebih kecil dari leftmark, berarti pembagian selesai
        if rightmark < leftmark:
            done = True
        else:
            # Tukar elemen kiri dan kanan jika belum selesai
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    # Tempatkan pivot pada posisi yang benar setelah pembagian
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    # Kembalikan posisi pivot yang baru
    return rightmark


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)