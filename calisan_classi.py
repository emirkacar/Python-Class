
class Employees:
    def __init__(self):
        self.calisanlar = {}
        self.max_employees = 10
    
    def yeni_calisan_ekle(self,miktar,ad,soyad,yas,ID):
        kontrol = 1
        if(miktar<self.max_employees):
            for calisan,bilgisi in self.calisanlar.items():
                if(ad == calisan):
                    print(f"{calisan} zaten listemizde.Yeni biri olarak ekleyemezsiniz.")
                    kontrol=0
                    
            if(kontrol==1):
                print(f"{ad} listeye eklenmistir.")
                self.calisanlar[ad] = [soyad,yas,ID]
        else:
            print("Maksimum calisan sayisi 20.20'den az calisan eklemelisiniz.")
        
            
    def calisan_sil(self,ad,soyad,yas,ID):
        kontrol = 1
        if(len(self.calisanlar)==0):
            print("Calisan yok.Calisan silinemez.")
        for calisan,bilgisi in self.calisanlar.items():
            if(ad == calisan):
                print(f"{calisan} basarili bir sekilde silinmistir.")
                self.calisanlar.pop(calisan)
                kontrol=0
                break
        if(kontrol==1):
            print(f"{calisan} diye bir calisanimiz yoktur.Silinemez.")
        
        
    
    def calisan_bilgilerini_getir(self):
        print("\nCALİSAN BİLGİLERİ")
        print(40 * "-")
        print(f"{self.calisanlar}")
        print("\n")
        for ad,bilgi in self.calisanlar.items():
            print(ad,bilgi)
        if(len(self.calisanlar)==0):
            return 0
        
    def calisan_sayisini_getir(self):
        print("\nCALİSAN SAYISI")
        print(40 * "-")
        print(f"{len(self.calisanlar)}")
    
    def maksimum_calisan_sayisini_gor(self):
        print(f"Maksimum calisan sayisi : {self.max_employees}")
    
    def calisan_ID_getir(self,ad,soyad):
        for k,v in self.calisanlar.items():
            if(ad==k):
                print(ad,calisanlar[ad][-1])
                print("--------------------------------------------------")
        
    
calisan = Employees()

while(True):
    print("""
1-Yeni calisan ekleyiniz
2-Calisan siliniz
3-Calisan bilgilerini getiriniz
4-Calisan sayisini getiriniz
5-Maksimum calisan sayisini gor
6-Cikis""")
    secim=int(input("1-6 arasi secim yapiniz: "))
    if(secim==1):
        adet = int(input("Kac adet calisan eklemek istiyorsunuz: "))
        for i in range(adet):
            ad=input("Ad giriniz: ").upper()
            soyad=input("Soyad giriniz: ").upper()
            yas=int(input("Yas giriniz: "))
            ID=int(input("ID giriniz: "))
            calisan.yeni_calisan_ekle(adet,ad,soyad,yas,ID)
            
    elif(secim==2):
        veri = calisan.calisan_bilgilerini_getir()
        if(veri==0):
            print("Calisan yok.")
        else:
            adet = int(input("Kac adet calisan silmek istiyorsunuz: "))
            for i in range(adet):
                ad=input("Ad giriniz: ").upper()
                soyad=input("Soyad giriniz: ").upper()
                yas=int(input("Yas giriniz: "))
                ID=int(input("ID giriniz: "))
                calisan.calisan_sil(ad,soyad,yas,ID)
            
    elif(secim==3):
        calisan.calisan_bilgilerini_getir()
        
    elif(secim==4):
        calisan.calisan_sayisini_getir()
        
    elif(secim==5):
        calisan.maksimum_calisan_sayisini_gor()
        
    elif(secim==6):
        print("Cikis yapiliyor...")
        break
    
    else:
        print("1-5 arasi secim yapiniz.")
       
        
    
    
    