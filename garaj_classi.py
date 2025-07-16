
class Garaj:
    def __init__(self, isim,kapasite=10, adres="Bilinmiyor"):
        self.isim = isim
        self.kapasite = kapasite
        self.adres = adres
        self.arabalar = []
        self.park_yerleri = {i: None for i in range(1, kapasite + 1)}
        self.giris_kayitlari = []
        self.cikis_kayitlari = []
        self.bakım_alani = []
        self.temizlik_programi = []
        self.guvenlik_sistemi = True
        self.aydinlatma = True
        self.sicaklik = 20
        
    def arac_park_et(self,marka,plaka,park_yeri = None):
        if len(self.arabalar) >= self.kapasite:
            print("Garajda yer yok.")
        else:
            for arac,yer in self.park_yerleri.items():
                if yer is None:
                    self.park_yerleri[yer] = {"marka": marka, "plaka": plaka}
                    self.arabalar.append({"marka": marka, "plaka": plaka, "yer": yer})
                    print(f"{marka} aracı {yer}. park yerine park edildi.")
                    break
    
    def garajdaki_arabalar(self):
        print("Garajdaki arabalar")
        for araba in self.arabalar:
            print(araba)
    
    def arac_cikar(self,verilen_plaka,marka):
        for araba in self.arabalar:
            if araba["plaka"] == verilen_plaka and araba["marka"] == marka:
                yer=araba["yer"]
                self.park_yerleri["yer"] = None
                self.arabalar.remove(araba)
                print(f"{marka} - {verilen_plaka} aracı garajdan çıkarıldı.")

                
garaj_sistemi = Garaj("Emir OTO")
garaj_sistemi.arac_park_et("Audi","16 BJ 187")
garaj_sistemi.arac_park_et("Ferrari","34 NHJNBV 18")        
garaj_sistemi.garajdaki_arabalar()
garaj_sistemi.arac_cikar('16 BJ 187',"Audi")