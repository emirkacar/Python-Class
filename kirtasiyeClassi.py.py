
class Kirtasiye:
    def __init__(self,isim):
        self.isim = isim
        self.calisanSayisi = 3
        self.calisanlarVeSayilari={"Emir":1,"Rafet":1,"Alperen":1}
        self.favoriListem=[]
        self.urunler={"Kitap":50,"Kalem":30,"Silgi":10}
        self.fiyatlar ={"Kitap":20,"Kalem":10,"Silgi":5}
        self.alisverisSepeti = {}

    def urunEkle(self,urun,adet):
        if(urun in self.urunler):
            self.urunler[urun] += adet
            print("Urun eklenmistir.")
        else:
            self.urunler[urun] = self.urunler.get(urun, 0) + adet
            print("Urun eklenmistir.")
    
    def urunCikar(self,urun,adet):
        if(urun in self.urunler):
            if(adet <= self.urunler[urun]):
                self.urunler[urun] -= adet
                print(f"Urun {adet} tane cikarilmistir.")
            else:
                print("Urun cikaramazsiniz.")
        else:
            print(f"{urun} adli urun listemizde yoktur.Urun cikaramazsiniz.")
    
    def elemanEkle(self,ad):
        for eleman in self.calisanlarVeSayilari:
            if(ad==eleman):
                self.calisanlarVeSayilari[eleman] += 1
            else:
                self.calisanlarVeSayilari[eleman] = 1
    
    def elemanCikar(self,ad):
        if(ad in self.calisanlarVeSayilari):
            if(self.calisanlarVeSayilari[ad]>0):
                self.calisanlarVeSayilari[ad] -= 1
            elif(self.calisanlarVeSayilari==1):
                self.calisanlarVeSayilari[ad] = 0
        else:
            print("Boyle bir eleman bulunamadi.Silme ilsemi yapilamaz.")

    def favoriListemeEkle(self,urun):
        for k in self.urunler:
            print(k)
        if(urun in self.urunler.keys()):
            self.favoriListem.append(urun)
            print(f"{urun} favori listenize eklenmistir.")
        else:
            print("Boyle bir urun bulunamadi.")
    
    def favoriListedenCikar(self,urun):
        if(urun in self.urunler.keys()):
            if(self.urunler[urun] > 0):
                self.favoriListem.remove(urun)
                print(f"{urun} favori listenizden cikartildi.")
        else:
            print("Boyle bir urunumuz yok.Urun cikartilamaz.")
    def bilgileriGoster(self):
        print(f"{self.isim} kirtasiyemizde {self.calisanSayisi} calisan bulunmaktadir.{self.urunler} urunlerimiz var.Fiyatlar da {self.fiyatlar} bu sekilde.Alisveris sepetiniz:{self.alisverisSepeti}")
    
    
    def zamYap(self,urun,fiyat):
        if(urun in self.urunler):
            self.fiyatlar[urun] += fiyat
        else:
            print("Urun kirtasiyemizde bulunmamaktadir,tekrar giris yapiniz.")

    def indirimYap(self,urun,indirim):
        if(urun in self.urunler):
            if(self.fiyatlar[urun] > indirim):
                print("Indirim yapabilirsiniz.")
                self.fiyatlar[urun] -= indirim
        else:
            print("Urun kirtasiyemizde bulunmamaktadir,tekrar giris yapiniz.")

    def urunuSatinAl(self,urun,adet,paraMiktari):
        for k,v in self.fiyatlar.items():
            print(k,v)
        if(urun in self.urunler):
            if(paraMiktari >= self.fiyatlar[urun]*adet):
                self.alisverisSepeti[urun] = self.alisverisSepeti.get(urun, 0) + adet
                paraMiktari -= self.fiyatlar[urun]*adet
                print("Urun satin alindi.")
                self.urunler[urun] -= adet
                
            else:
                print("Bu urun icin yeterli miktarda bakiyeniz bulunmamaktadir.")
        else:
            print("Istediginiz uru kirtasiyemizde bulunmamaktadir.")

    def urunuSatinAlmaktanVazgec(self,urun,adet):
        if(urun in self.alisverisSepeti):
            self.alisverisSepeti[urun] -= adet
        else:
            print("Urun alisveris sepetinizde degildir.")

    def calisaniCagir(self):
        print("Cagiran cagiriliyor...")
    
    def favoriListeyiGoster(self):
        print(f"{self.favoriListem}")


kirtasiye=Kirtasiye("emirkacarKirtasiye")
main=True
kirtasiye.bilgileriGoster()

while(True):
    secim = input("Musteri mi calisan mi,patron mu?: ").lower()
    if(secim=="musteri"):
        print("""Kirtasiyeye hosgeldiniz.
              1-Favori Listeme Ekle
              2-Favori Listemden Cikar
              3-Urunu satin al
              4-Urunu satin almaktan vazgec
              5-Calisani cagir.
              6-Cikis""")
        secim=int(input("1-6 arasi secim yapiniz: "))
        
        if(secim==1):
            urun=input("Urun: ")
            kirtasiye.favoriListemeEkle(urun)
        elif(secim==2):
            kirtasiye.favoriListeyiGoster()
            urun=input("Urun: ")
            kirtasiye.favoriListedenCikar(urun)
        elif(secim==3):
            urun=input("Urun: ")
            adet=int(input("Adet: "))
            paraMiktari=int(input("Para Miktariniz: "))
            kirtasiye.urunuSatinAl(urun,adet,paraMiktari)
        elif(secim==4):
            urun=input("Urun: ")
            adet=int(input("Adet: "))
            kirtasiye.urunuSatinAlmaktanVazgec(urun,adet)
        elif(secim==5):
            kirtasiye.calisaniCagir()
        elif(secim==6):
            break
        else:
            print("1-6 arasi secim yapiniz.")

    if(secim=="calisan"):
        print("""
            1-Urun Ekle
            2-Urun Cikar
              3-Cikis
              """)
        secim=int(input("1-6 arasi secim yapiniz: "))
        
        if(secim==1):
            urun=input("Urun: ")
            adet=int(input("Adet: "))
            kirtasiye.urunEkle(urun,adet)
        elif(secim==2):
            urun=input("Urun: ")
            adet=int(input("Adet: "))
            kirtasiye.urunCikar(urun,adet)
        elif(secim==3):
            break
        else:
            print("1-3 arasi secim yapiniz.")

    if(secim=="patron"):
        print("""
            1-Zam Yap
            2-Indirim yap
            3-Bilgileri Goster
            4-Cikis""")
        secim=int(input("1-6 arasi secim yapiniz: "))
        
        if(secim==1):
            urun=input("Urun: ")
            fiyat=int(input("Urunun fiyati kac olsun?"))
            kirtasiye.zamYap(urun,fiyat)
        elif(secim==2):
            urun=input("Urun: ")
            indirim=int(input("Yuzde kac indirim olsun?"))
            kirtasiye.indirimYap(urun,indirim)
        elif(secim==3):
            kirtasiye.bilgileriGoster()
        elif(secim==4):
            break
        else:
            print("1-3 arasi secim yapiniz.")

    
   
        
    
        



        
