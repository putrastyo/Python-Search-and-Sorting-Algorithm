def binary_search(alist, item):
    # inisialisasi nilai awal
    first = 0
    # inisialisasi nilai akhir
    last = len(alist) - 1
    # inisialisasi data ditemukan (defaltnya false)
    found = False

    # pencarian dengan looping
    while first <= last and not found:
        # inisialisasi nilai tengah
        midpoint = (first + last) // 2

        # jika nilai tengah sama dengan target
        if alist[midpoint] == item:
            # data ditemukan, perulangan berhenti
            found = True
        # jika tidak
        else:
            # jika target lebih kecil dari nilai tengah
            if item < alist[midpoint]:
                # nilai akhir dibuah menjadi nilai tengah dikurangi 1
                last = midpoint - 1
            else:
                # nilai awal dibuah menjadi nilai tengah ditambah 1
                first = midpoint + 1

    # kembalikan nilai found (bool)
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))