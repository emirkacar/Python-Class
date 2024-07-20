
meyveler = {"Elma":50,"Armut":100,"Cilek":90}

def meyveVeStokDurumunuGoster():
    global meyveler
    for k,v in meyveler.items():
        print(k,v)

def yeniMeyveEkle(meyveAdi,adet):
    global meyveler
    if(meyveAdi in meyveler):
        meyveler[meyveAdi] += adet
    else:
        meyveler[meyveAdi] = adet


def meyveSat(meyveAdi,satilacakMeyveSayisi):
    global meyveler
    if(meyveAdi in meyveler):
        if(satilacakMeyveSayisi>=meyveler[meyveAdi]):
            meyveler[meyveAdi] -= satilacakMeyveSayisi
        else:
            print(f"{meyveAdi} meyvemizden {satilacakMeyveSayisi} kadar meyve bulunmamaktadir.")
    else:
        print(f"Reyonumuzda {meyveAdi} meyvesi bulunmamaktadir.")

def meyveBilgileriniGuncelle():
    global meyveler
    print(f"Reyonumuzdaki meyve sayisi = {meyveler}")

def meyveAra(meyveAdi):
    global meyveler
    if(meyveAdi in meyveler):
        print(f"{meyveAdi} meyvesi reyonumuzda vardir.")
    else:
        print(f"{meyveAdi} meyvesi reyonumuzda yoktur.")


main=True
while(True):
    if(main):
        print("""
              MEYVE REYONUMUZA'A HOSGELDINIZ.
              1:MEYVE VE STOK DURUMUNU GOSTER
              2:YENI MEYVE EKLE
              3:MEYVE SAT
              4:MEYVE BILGILERINI GUNCELLE
              5:MEYVE ARA(VAR MI YOK MU DIYE)
              6:MENUYE DON
              7:CİKİS  
              """)
        
        try:
            secim = int(input("Lutfen bir secim yapiniz: "))
        except ValueError:
            print("İnteger bir deger giriniz.")

        main=False
        if(secim==1):
            meyveVeStokDurumunuGoster()
            main=True

        elif(secim==2):
            yeniMeyve=input("Hangi meyveyi eklemek istiyorsunuz? : ")
            adet = int(input("Kac adet eklemek istiyorsunuz? : "))
            yeniMeyveEkle(yeniMeyve,adet)
            main=True

        elif(secim==3):
            satilacakMeyve = input("Hangi meyveyi satmak istiyorsunuz? : ")
            adet = int(input("Kac adet satmak istiyorsunuz?"))
            meyveSat(satilacakMeyve,adet)
            main=True

        elif(secim==4):
            meyveBilgileriniGuncelle()
            main=True

        elif(secim==5):
            aranilanMeyve = input("Hangi meyveyi ariyorsunuz ? : ")
            meyveAra(aranilanMeyve)
            main=True

        elif(secim==6):
            main=True

        elif(secim==7):
            break
print("Tesekkurler.")


