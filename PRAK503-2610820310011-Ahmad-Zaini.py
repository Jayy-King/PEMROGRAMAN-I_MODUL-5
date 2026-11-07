def maksimal(a , b):
    return a if a > b else b

def minimal(a , b):
    return a if a < b else b

def main():
    bilangan = int(input())
    data = list(map(int, input().split()))

    batas = 0
    maks = -100000
    minim = 100000

    while batas < bilangan :
        nilai = data[batas]
        maks = maksimal(maks, nilai)
        minim = minimal(minim, nilai)
        batas += 1 
    print(f"{maks} {minim}")

if __name__ == "__main__":
    main()