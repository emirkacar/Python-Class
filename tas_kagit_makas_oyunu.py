import random


def game(you,computer):
    if you==computer:
        return -1
    elif(you=='T' and computer=='M') or (you=='K' and computer=='T') or (you=='M' and computer=='K'):
        return 1
    else:
        return 0

def secimim(you):

    return {"T":"Tas",
            "M":"Makas",
            "K":"Kagit"}.get(you,"Bilinmiyor")

def bilgisayarin_secimi(computer):
    return {"T":"Tas",
            "M":"Makas",
            "K":"Kagit"}.get(computer,"Bilinmiyor")

computer = random.choice(['T','K','M'])
print("\n\nTas kagit makas oyununa hosgeldiniz.")
print("\nTas icin 'T', kagit icin 'K',makas icin 'M' giriniz ")

you = input("Seciminizi giriniz: ").upper()
liste = ['T','K','M']

if you not in liste:
    print("\n\nGecersiz secim yaptiniz.Lutfen 'T','K','M' degerlerinden birini giriniz. ")
else:
    result=game(you,computer)

    print(f"Senin secimin = {secimim(you)}")
    print(f"Bilgisayarin secimi = {bilgisayarin_secimi(computer)}")
    if(result==-1):
        print("Berabere")
    elif(result==1):
        print("Oyunu Kazandiniz tebrikler.")
    else:
        print(f"Kaybettiniz.Bilgisayarin tercihi = {computer}")






