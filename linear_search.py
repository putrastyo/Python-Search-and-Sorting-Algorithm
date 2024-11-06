def sequential_search(alist, item):
    # nilai awal
    pos = 0

    # inisialisasi data ditemukan (defaultnya false)
    found = False

    # pencarian dengan looping dari nilai awal (pos)
    while pos < len(alist) and not found:
        # jika pos sama dengan target
        if alist[pos] == item:
            # found menjadi True, dan perulangan berhenti
            found = True
        # jika tidak,
        else:
            # maka nilai awal di increment satu untuk menyempitkan pencarian
            pos = pos + 1

    # kembalikan nilai found (bool)
    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))