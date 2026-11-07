def hitung(nilai1, nilai2):
    return nilai1 - nilai2

def mutlak(angka):
    if angka < 0:
        return -angka
    return angka

def main():
    masukan = list(map(int, input().split()))
    a, c, b, d = masukan[0], masukan[1], masukan[2], masukan[3]
    Hasil = mutlak(hitung(a, b)) + mutlak(hitung(c, d))
    print(Hasil)
    
if __name__ == "__main__":
    main()