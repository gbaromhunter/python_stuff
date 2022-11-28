def convert_km():
    """converts kilometers to meters"""
    kms = int(input("Inserisci il numero di chilometri: "))
    metri = kms*1000
    return print(f"Questi sono i metri risultanti: {metri}")


def convert_m():
    """converts meters to kilometers"""
    metri = int(input("Inserisci il numero di metri: "))
    kilometri = metri/1000
    return print(f"Questi sono i kilometri risultanti: {kilometri}")