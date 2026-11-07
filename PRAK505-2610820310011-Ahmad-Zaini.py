def Biodata(tahunLahir, Namaku, Asal):
    tahun_sekarang = 2020
    umur = tahun_sekarang - tahunLahir
    print(f"Perkenalkan Nama Saya: {Namaku}")
    print(f"Umur Saya: {umur}")
    print(f"Saya Adalah Angkatan : {tahun_sekarang}")
    print(f"Asal Saya dari : {Asal}")

def main():
    tahunLahir = int(input())
    A = input()
    B = input()
    Biodata(tahunLahir, A, B)

if __name__ == "__main__":
    main()