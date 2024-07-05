


class Buzdolabi:

    def __init__(self,marka,model,kapasite,sicaklik = 5):
        self.marka = marka
        self.model = model
        self.kapasite = kapasite
        self.sicaklik = sicaklik
        self.kapiAcikMi = False
        self.urunler = []
    
    def BilgileriGoster(self):
        print(f"{self.marka} {self.model} {self.kapasite} {self.sicaklik} {self.kapiAcikMi} {self.urunler}")
    def sicaklikAyarlari(self,yeniSicaklik):

        if(yeniSicaklik < -10 or yeniSicaklik > 10):
            print("Gecersiz sicaklik degeri.")
        self.sicaklik = yeniSicaklik
        print("Yeni sicaklik = ",self.sicaklik)

    def kapiDurumunuDegistir(self,kapiDurumu):
        if(kapiDurumu == True):
            self.kapiAcikMi = True
        else:
            self.kapiAcikMi = False
    def urunEkle(self,urun):
        if(len(self.urunler) >= self.kapasite):
            print("Buzdolabi dolu,urun eklenemiyor.")
        print("Urun eklenmistir.")
        self.urunler.append(urun)
        
    def urunKontrolEt(self,urun):
        if(urun in self.urunler):
            print("Urun buzdolabinda mevcut.")
        else:
            print("Urun buzdolabinda bulunamadi.")
    def urunCikar(self,urun):
        if(urun in self.urunler):
            self.urunler.remove(urun)
            print("Urun buzdolabindan cikarildi.")
        else:
            print("Urun buzdolabinda bulunamadi.")

buzdolabi1 = Buzdolabi("Bosch", "KDN56", 50)        

buzdolabi1.BilgileriGoster()
buzdolabi1.sicaklikAyarlari(7)
buzdolabi1.kapiDurumunuDegistir("True")
buzdolabi1.urunEkle("Süt")
buzdolabi1.urunKontrolEt("Süt")
buzdolabi1.urunCikar("Süt")
buzdolabi1.urunKontrolEt("Süt")
buzdolabi1.sicaklikAyarlari(15)


        
