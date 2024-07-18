
#Bir music player classi

class MusicPlayer:
    #ses seviyesi 0-10 arasindadir.
    def __init__(self,durum=False,sarkilistesi=[],ses=0):
        self.durum = durum
        self.sarkiListesi = sarkilistesi
        self.ses = ses
    
    def bilgileriGoster(self):
        print(f"Durum:{self.durum}  Sarki Listesi: {self.sarkiListesi} Ses:{self.ses}")

    def sesArttir(self):
        if(self.ses < 10):
            self.ses += 1
            print(f"Ses arttirildi.Ses seviyesi:{self.ses}")
        else:
            print("Ses zaten maksimum seviyede.")
        
    def sesAzalt(self):
        if(self.ses>0):
            self.ses -= 1
            print(f"Ses azaltildi.Ses seviyesi:{self.ses}")
        else:
            print(f"Ses zaten minimum seviyede")

    def sesKis(self):
        self.ses = 0
        print("Ses tamamen kisildi.")
    
    def powerOnOff(self):
        if(self.durum):
            self.durum = False
        else:
            self.durum = True
    def sarkiListesiOlustur(self,sarkilar):
        self.sarkiListesi = sarkilar

    def sarkiListesiniGoster(self):
        for i in self.sarkiListesi:
            print(i)
    
    def sarkiListesiniGuncelle(self,sarkilar):
        for i in sarkilar:
            self.sarkiListesi.append(i)
    
    def sarkiListesiniSil(self):
        self.sarkiListesi = []

    def sarkiSayisiniKiyasla(self,music1,music2):
        if(len(music1.sarkiListesi) > len(music2.sarkiListesi)):
            print("Music1'in sarki listesi music2'nin sarki listesinden daha fazla")
        else:
            print("Music2'nin sarki listesi music1'in sarki listesinden daha fazla")


m1=MusicPlayer(sarkilistesi=["V","x","y","z"],ses=5)
m1.bilgileriGoster()
m2 = MusicPlayer(True,["A","B","C"],2)

m2.bilgileriGoster()
m2.sesArttir()
m2.sesAzalt()
m2.bilgileriGoster()
m2.sesKis()
m2.bilgileriGoster()
m2.powerOnOff()
m2.bilgileriGoster()
m3=MusicPlayer()
m3.bilgileriGoster()
m3.sarkiListesiOlustur(['H','J','K'])
m3.bilgileriGoster()
m3.sarkiListesiniGoster()
m3.sarkiListesiniGuncelle(['T','Y','P'])
m3.sarkiListesiniGoster()
m3.sarkiListesiniSil()
m3.bilgileriGoster()
m3.sarkiListesiniGoster()
print(len(m3.sarkiListesi))
m3.sarkiSayisiniKiyasla(m1,m2)

