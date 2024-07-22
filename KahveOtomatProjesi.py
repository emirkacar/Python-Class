fiyat = {
    "Espresso": [20, 23, 27],
    "Americano": [25, 27, 30],
    "Latte": [30, 32, 35]
}

class Otomat:
    def __init__(self,otomatDurum="Kapali",kahveListesi=["Espresso","Americano","Latte"],miktar=0,seker=0):
        self.otomatDurum = otomatDurum
        self.kahveListesi=kahveListesi
        self.miktar = miktar
        self.seker = seker
        self.fatura = 0
        self.kurabiye = 20
        self.kurabiyeDurumu = 0
    
    def otomatAc(self):
        if(self.otomatDurum=="Kapali"):
            print("Otomat aciliyor.")
            self.otomatDurum="Acik"
        elif(self.otomatDurum=="Acik"):
            print("Otomat zaten acik.")
            self.otomatDurum="Acik"
    
    def otomatKapat(self):
        if(self.otomatDurum=="Kapali"):
            print("Otomat zaten kapali")
            self.otomatDurum="Kapali"
        elif(self.otomatDurum=="Acik"):
            print("Otomat kapatiliyor.")
            self.otomatDurum="Kapali"
    
    def kahveEkle(self):
        if(self.otomatDurum=="Kapali"):
            print("Once otomati aciniz")
        else:
            for k,v in fiyat.items():
                print(k,v)
            veri = input("Eklemek istediginiz kahvenin adini giriniz: ")
            kucukBoyFiyati=int(input("Kucuk boy fiyatini giriniz: "))
            ortaBoyFiyati= int(input("Orta boy fiyati giriniz: "))
            buyukBoyFiyati= int(input("Buyuk boy fiyati giriniz: "))
            fiyat[veri]=[kucukBoyFiyati,ortaBoyFiyati,buyukBoyFiyati]
            print(f"{veri} kahvesi eklendi.")

    def kahveFiyati(self):
        if(self.otomatDurum=="Kapali"):
            print("Once otomati aciniz.")
        else:
            for k,v in fiyat.items():
                print(k,v)
            secim = input("Alacaginiz kahvenizi seciniz: ")
            if(secim=="Espresso"):
                boyBuyuklugu = input("Hangi boyu istersiniz? (Kucuk,Orta,Buyuk)")
                if(boyBuyuklugu=="Kucuk"):
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Espresso"][0]
                    else:
                        self.fatura = fiyat["Espresso"][0]
                elif(boyBuyuklugu=="Orta"):
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Espresso"][1]
                    else:
                        self.fatura = fiyat["Espresso"][1]
                else:
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Espresso"][2]
                    else:
                        self.fatura = fiyat["Espresso"][2]
                
            elif(secim=="Americano"):
                boyBuyuklugu = input("Hangi boyu istersiniz? (Kucuk,Orta,Buyuk)")
                if(boyBuyuklugu=="Kucuk"):
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Americano"][0]
                    else:
                        self.fatura = fiyat["Americano"][0]
                elif(boyBuyuklugu=="Orta"):
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Americano"][1]
                    else:
                        self.fatura = fiyat["Americano"][1]
                else:
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Americano"][2]
                    else:
                        self.fatura = fiyat["Americano"][2]
            else:
                boyBuyuklugu = input("Hangi boyu istersiniz? (Kucuk,Orta,Buyuk)")
                if(boyBuyuklugu=="Kucuk"):
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Latte"][0]
                    else:
                        self.fatura = fiyat["Latte"][0]
                elif(boyBuyuklugu=="Orta"):
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Latte"][1]
                    else:
                        self.fatura = fiyat["Latte"][1]
                else:
                    kurabiyeDurumu = input("Kurabiye ister misiniz? (Evet,Hayir)")
                    if(kurabiyeDurumu=="Evet"):
                        self.fatura = self.kurabiye + fiyat["Latte"][2]
                    else:
                        self.fatura = fiyat["Latte"][2]
            print(f"Faturaniz = {self.fatura}")
    
    def menuyuGoster(self):
        if(self.otomatDurum=="Kapali"):
            print("Once otomati aciniz")
        else:
            for k,v in fiyat.items():
                print(k,v)
            
otomat = Otomat()
main = True
while(True):
    if(main):
            
            print("""
                Kahve Otomati
                1. Otomati ac
                2. Otomati kapat
                3. Menuyu yazdir
                4. Kahve ekle
                5. Kahvenizi secin
                6.Menuye tekrar bak
                7.Cikis""")
            secim = int(input("1-7 arasi secim yapiniz: "))
            if(secim==1):
                 otomat.otomatAc()
                 main=True
            elif(secim==2):
                otomat.otomatKapat()
                main=True
            elif(secim==3):
                otomat.menuyuGoster()
                main=True
            elif(secim==4):
                otomat.kahveEkle()
                main=True
            elif(secim==5):
                otomat.kahveFiyati()
                main=True
            elif(secim==6):
                main=True
            elif(secim==7):
                break   
            else:
                print("1-7 arasinda secim yapiniz.")
print("Tesekkurler.")
