

class Kutuphane:
    def __init__(self,kutuphaneAdi,yil,kitaplar):
        self.kutuphaneAdi = kutuphaneAdi
        self.yil = yil
        self.kitaplar = kitaplar
        self.bilgisayar = 0


    def kitapOduncAl(self,kitapAdi):
        if(kitapAdi in self.kitaplar):
            if(self.kitaplar[kitapAdi] != 0):
                print(f"{kitapAdi} kitabi odunc alinmistir.")
                self.kitaplar[kitapAdi]=0
        else:
            print(f"{kitapAdi} kitabi kutuphanemizde bulunmamaktadir.")

    def kitapAra(self,kitapAdi):
        if(kitapAdi in self.kitaplar[kitapAdi]):
            if(self.kitaplar[kitapAdi != 0]):
                print(f"{kitapAdi} kitabi mevcuttur.")
        else:
            print(f"{kitapAdi} kitabi kutuphanemizde bulunmamaktadir.")
        

    def kitabiGeriVer(self,kitapAdi):
        if(kitapAdi in self.kitaplar[kitapAdi]):
            self.kitaplar[kitapAdi] += 1
        else:
            print(f"{kitapAdi} kitabi kutuphanemizde bulunmamaktadir.")    

    def kitaplarinListesi(self):
        for k,v in self.kitaplar.items():
            print(f"{k} kitabindan {v} tane bulunmaktadir.")


    def kitapEkle(self,kitapAdi):
        if(kitapAdi in self.kitaplar[kitapAdi]):
            self.kitaplar[kitapAdi] += 1
        else:
            self.kitaplar[kitapAdi] = 1


    def kitapSil(self,kitapAdi):
        if(kitapAdi in self.kitaplar[kitapAdi]):
            self.kitaplar.pop(kitapAdi)
        else:
            print("Kitap kutuphanemizde bulunmamaktadir.İslem gecersiz.")
        

    def bilgisayarKullan(self):
        secim = input("Kutuphanemizde bilgisayar kullanmak istiyor musunuz?(Evet,Hayir):")
        if(secim=="Evet"):
            print("Bilgisayari kullanabilirsiniz.")
            self.bilgisayar=1
        elif(secim=="Hayir"):
            print("Bilgisayari kullanamazsiniz..")
            self.bilgisayar=0


kitap = Kutuphane("Bursa Kutuphanesi",4,{'A':1,'V':1,'Y':1,'Z':1,'D':1,'O':1})
main=True

while(True):
    if(main):
        print("""
              ***KUTUPHANEYE HOSGELDINIZ.***
                1-Kitap Odunc Al
                2-Kitap Ara
                3-KitabiGeriVer
                4-Kitaplarin Listesini Goruntule
                5-Kitap Ekle
                6-Kitap Sil
                7-Bilgisayar Kullanmak İstiyor musunuz?
                8-Menuye geri don.
                9-Cikis yap.
                """)
                
        secim = int(input("Secim yapiniz: "))
        main=False
        if(secim==1):
            kitapAdi = input("Hangi kitabi odunc almak istiyorsunuz ?:")
            kitap.kitapOduncAl(kitapAdi)
            main=True
        elif(secim==2):
            kitapAdi = input("Hangi kitabi ariyorsunuz?")
            kitap.kitapAra(kitapAdi)
            main=True
        elif(secim==3):
            kitapAdi=input("Hangi kitabi geri vermek istiyorsunuz?")
            kitap.kitabiGeriVer(kitapAdi)
            main=True
        elif(secim==4):
            kitap.kitaplarinListesi()
            main=True
        elif(secim==5):
            kitapAdi=input("Hangi kitabi eklemek istiyorsunuz? ")
            kitap.kitapEkle(kitapAdi)
            main=True
        elif(secim==6):
            kitapAdi=input("Hangi kitabi silmek istiyorsunuz?")
            kitap.kitapSil(kitapAdi)
            main=True
        elif(secim==7):
            kitap.bilgisayarKullan()
        elif(secim==8):
            main=True
        elif(secim==9):
            break
        else:
            print("1-10 arasinda secim yapiniz.")
print("Tesekkurler.")


                          
