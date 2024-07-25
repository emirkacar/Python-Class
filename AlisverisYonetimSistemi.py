


class alisverisYonetimSistemi:
    def __init__(self):
        self.urunListesi = []
        self.ID = []
        self.favoriUrunler = []
        self.siparisSayisi = 0

    def urunEkle(self,urun):   
        if(len(self.urunListesi) < 20 ):
            if(urun in self.urunListesi):
                print("Urun zaten listenizde.")
            else:
                self.urunListesi.append(urun)
                self.ID.append(len(self.ID) + 1)
                print(f"{urun} eklendi.")
        else:
            print("Urun ekleyemezsiniz.")

    def urunSil(self,urun):       
        if(urun in self.urunListesi):
            index=self.urunListesi.index(urun)
            self.urunListesi.revome(urun)
            self.ID.pop(index)
            print(f"{urun} silindi")
        else:
            print("Urun listenizde yok.Silinemiyor.")

    def urunArama(self,urun):   
        if(urun in self.urunListesi):
            print("Urun listenizde var.")
        else:
            print("Urun listenizde yok.")

    def siparisOlustur(self): 
        self.siparisSayisi += 1
        print("Siparis olusturuldu.")

    def siparisIptalEt(self): 
        if(self.siparisSayisi > 1):
            self.siparisSayisi -= 1
            print("Sipariş iptal edildi.")
        else:
            print("İptal edilecek sipariş yok.")

    def stokDurumunuGuncelle(self,yeniStok):  
        urunId=int(input("Stoku guncellenecek urunun idsi: "))
        if(urunId in self.ID):
            index=self.ID.index[urunId]
            yeniStok=int(input("Yeni stok miktarini giriniz: "))
            print(f"{self.urunListesi[index]} ürününün stok miktari {yeniStok} olarak güncellendi.")
        else:
            print("Urun bulunamadi")


    def favoriUrunlerEkle(self):  
        eklenecekUrun=input("Eklenecek urunu giriniz: ")
        if(eklenecekUrun in self.favoriUrunler):
            print(f"{eklenecekUrun} zaten favori urunlerde")
        else:
            self.favoriUrunler.append(eklenecekUrun)
            print(f"{eklenecekUrun} favori ürünlere eklendi.")

    def dusukStokluUrunleriListele(self):  
        print("Bu ozellik henuz uygulanmadi.")

    def tumUrunleriListele(self):   
        if(self.urunListesi):
            print("Tum urunler:")
            for i,urun in enumerate(self.urunListesi):
                print(f"ID:{self.ID[i]},Urun:{urun}")
        else:
            print("Urun listesi bos.") 


    def favoriUrunlerimiGoruntule(self):
        if self.favoriUrunler:
            print("Favori Ürünler:")
            for urun in self.favoriUrunler:
                print(urun)
        else:
            print("Favori ürün listeniz boş.")
        

    def istatistikler(self):
        print(f"Toplam Ürün Sayisi: {len(self.urunListesi)}")
        print(f"Toplam Sipariş Sayisi: {self.siparisSayisi}")
        print(f"Favori Ürün Sayisi: {len(self.favoriUrunler)}")

alisveris = alisverisYonetimSistemi()
main=True
while(True):
    if(main):
        print("""
              1-Urun Ekle
              2-Urun Sil
              3-Urun Ara
              4-Siparis Olustur
              5-Siparis İptal Et
              6-Stok Durumunu Guncelle
              7-Favori Urun Ekle
              8-Dusuk Stoklu Urunleri Listele
              9-Tum Urunleri Listele
              10-Favori Urunlerimi Goruntule
              11-İstatistikler
              12-Menuye Geri Don
              13-Cikis
              """)
        main=False
        secim=int(input("1-12 arasi bir secim yapiniz: "))
        if(secim==1):
            urun=input("Urun giriniz: ")
            alisveris.urunEkle(urun)
            main=True
        elif(secim==2):
            urun=input("Silinecek urunu giriniz: ")
            alisveris.urunSil(urun)
            main=True
        elif(secim==3):
            urun=input("Aranacak urunu giriniz: ")
            alisveris.urunArama(urun)
            main=True
        elif(secim==4):
            alisveris.siparisOlustur()
            main=True
        elif(secim==5):
            alisveris.siparisIptalEt()
            main=True
        elif(secim==6):
            alisveris.stokDurumunuGuncelle()
            main=True
        elif(secim==7):
            alisveris.favoriUrunlerEkle()
            main=True
        elif(secim==8):
            alisveris.dusukStokluUrunleriListele()
            main=True
        elif(secim==9):
            alisveris.tumUrunleriListele()
            main=True
        elif(secim==10):
            alisveris.favoriUrunlerimiGoruntule()
            main=True
        elif(secim==11):
            alisveris.istatistikler()
            main=True
        elif(secim==12):
            main=True
        elif(secim==13):
            break
        else:
            print("Lutfen 1-12 arasinda secim yapiniz.")


        