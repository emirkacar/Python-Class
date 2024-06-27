import random 
import time

class Kumanda():

    def __init__(self,tv_durum="Kapali",tv_ses = 0 , kanal_listesi = ["Trt"], kanal = "Trt"):

        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Acik"):
            print("Televizyon zaten acik.")
        else:
            print("Televizyon aciliyor.....")
            self.tv_durum = "Acik"
    def tv_kapat(self):
        if(self.tv_durum == "Acik"):
            print("Televizyon kapaniyor....")
            self.tv_durum = "Kapali"
        else:
            print("Televizyon zaten kapali.")
    def ses_ayarlari(self):

        while(True):

            cevap = input("Sesi acmak isterseniz '>' tusuna basin,kapatmak isterseniz '<' tusuna basin.Cikmak isterseniz cikis tusuna basiniz")

            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses : ",self.tv_ses)
            elif (cevap == ">"):
                if(self.tv_ses < 30 ):
                    self.tv_ses += 1
                    print("Ses : ",self.tv_ses)
            elif (cevap.lower() == "cikis" ):
                print("Ses guncellendi: ",self.tv_ses)
                break
            else:
                print("Gecersiz islem yaptiniz.")
    
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi.......")
    
    def rastgele_Kanal(self):

        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Su anki kanal : ",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self):
        return (f"Tv durumu : {self.tv_durum}\nTv ses {self.tv_ses}\nKanal Listesi : {self.kanal_listesi}\n Su anki kanal : {self.kanal}\n")




kumanda = Kumanda()
print("""
      
TELEVİZYON UYGULAMASİ       

      1-Tv Ac
      2-Tv Kapat
      3-Ses Ayarlari
      4-Kanal Ekle
      5-Kanal Sayisini Ogrenme
      6-Rastgele Kanala Gecme
      7-Televizyon Bilgileri   
      
      Cikmak icin q'ye basiniz.
      """)
        

while (True):
    islem = input("İslemi seciniz")

    if(islem == 'q'):
        print("Program sonlandiriliyor.")
        break
    elif(islem == '1'):
        kumanda.tv_ac()
    elif (islem == '2'):
        kumanda.tv_kapat()
    elif(islem == '3'):
        kumanda.ses_ayarlari()
    elif(islem == '4'):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayirarak giriniz : ")

        kanal_Listesi = kanal_isimleri.split(",")

        for i in kanal_Listesi:
            kumanda.kanal_ekle(i)

        
    elif (islem == '5' ):
        print("Kanal sayisi = ",len(kumanda))
    
    elif ( islem == '6'):
        kumanda.rastgele_Kanal()
    
    elif(islem == '7'):
        print(kumanda)
    else:
        print("Gecersiz islem yaptiniz.")