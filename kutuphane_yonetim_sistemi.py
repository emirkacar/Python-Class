
class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunclu_kitaplar={}
        self.kutuphanedeki_kitaplar = {}
    
    def kitap_siparis_ver(self,kargo):
        print("KITAP SIPARISI ALINMISTIR.")
        return kargo

    def kitap_ekle(self,kitap_ismi):
        if(isinstance(kitap_ismi,str) and kitap_ismi.strip()):
            kitap_ismi=kitap_ismi.strip().upper()
            if kitap_ismi in self.kitaplar:
                print("Kitap zaten listede")
            else:
                kitap_ismi = str(kitap_ismi).upper()
                print(f"{kitap_ismi} kitapliga eklendi.")
                self.kitaplar.append(kitap_ismi)
                self.kutuphanedeki_kitaplar[kitap_ismi]="Mevcut"
        else:
            print("Kitap eklemek icin bir deger giremezsiniz.Kitap ismini dogru giriniz lutfen.")

    def kitap_sil(self,kitap_ismi):
        kitap_ismi = str(kitap_ismi.upper())
        kitap_ismi=kitap_ismi.strip().upper()
        if kitap_ismi in self.kitaplar:
            self.kitaplar.remove(kitap_ismi)
            print(f"{kitap_ismi} listeden silindi.")
            self.kutuphanedeki_kitaplar[kitap_ismi] = "Mevcut Degil"
        else:
            print(f"{kitap_ismi} listede mevcut degil.Silemiyoruz.")

    def kitap_sayisini_goster(self):
        print(f"KITAP SAYISI = {len(self.kitaplar)}")
    
    def odunc_kitap_al(self,kitap_ismi):
        kitap_ismi=str(kitap_ismi).upper().strip()
        kontrol = 1
        for kitap in self.kitaplar:
            if(kitap == kitap_ismi):
                print(f"{kitap_ismi} kitabı odunc alabilirsiniz.")
                self.odunclu_kitaplar[kitap_ismi] = "Odunc Verildi"
                self.kitaplar.remove(kitap_ismi)
                self.kutuphanedeki_kitaplar[kitap_ismi] = "Odunc Verildi"
                kontrol = 0
                break
        if(kontrol==1):
            print(f"{kitap_ismi} kitabi kutuphanede bulunmamaktadir.Isterseniz siparis verebiliriz.")
            siparis_verilsin_mi = input("Siparis verilsin mi? (E/H)").upper()
            if(siparis_verilsin_mi=='E'):
                kargo = self.kitap_siparis_ver(kitap_ismi)
                print(f"{kargo} kitabi kutuphaneye geldi.Odunc alabilirsiniz.")
                self.odunclu_kitaplar[kargo] = "Odunc Verildi"
                self.kitaplar.remove(kargo)
                self.kutuphanedeki_kitaplar[kargo] ="Odunc Verildi"
            else:
                print(f"Daha sonra tekrar gelebilirsiniz.{kitap_ismi} kitabi odunc verilmemistir.")
        else:
            return
        
        if(kitap_ismi in self.odunclu_kitaplar):
            print("Kitap odunc verilmistir.Kitap suanda kutuphanede mevcut degildir.Isterseniz kargo siparisi verebiliriz.")
            siparis_verilsin_mi = input("Siparis verilsin mi? (E/H)").upper()
            if(siparis_verilsin_mi=='E'):
                kargo = self.kitap_siparis_ver(kitap_ismi)
                print(f"{kargo} kitabi kutuphaneye geldi.Odunc alabilirsiniz.")
                self.odunclu_kitaplar[kargo] = "Odunc Verildi"
                self.kitaplar.remove(kitap_ismi)
                self.kutuphanedeki_kitaplar[kitap_ismi] = "Odunc Verildi"
            else:
                print(f"Daha sonra tekrar gelebilirsiniz.{kitap_ismi} kitabi odunc verilmemistir.")

        else:
            self.odunclu_kitaplar[kitap_ismi] = "Odunc Verildi"
            print(f"{kitap_ismi} kitabi size odunc verilmistir.")
            self.kitaplar.remove(kitap_ismi)
            self.kutuphanedeki_kitaplar[kitap_ismi] = "Odunc Verildi"

    
    def kitabi_geri_ver(self,kitap_ismi):
        print(f"Odunc aldigim kitaplar = {self.odunclu_kitaplar}")
        kitap_ismi=str(kitap_ismi).upper().strip()
        kontrol=1
        for kitap_adi,durum in self.odunclu_kitaplar.items():
            if kitap_ismi == kitap_adi:
                if durum == "Odunc Verildi":
                    self.kitaplar.append(kitap_ismi)
                    self.kutuphanedeki_kitaplar[kitap_ismi] ="Mevcut"
                    kontrol=0
                    break
        if(kontrol==1):
            print(f"{kitap_ismi} kutuphaneye geri verilmistir...")
            self.kitaplar.append(kitap_ismi)
            self.kutuphanedeki_kitaplar[kitap_ismi] = "Mevcut"
            self.kutuphanedeki_kitaplar[kitap_ismi] = "Mevcut"
            kontrol=1
            for kitap in self.kitaplar:
                if(kitap == kitap_ismi):
                    kontrol=0
                    break
            if(kontrol==1):
                self.kitaplar.append(kitap_ismi)
                self.kutuphanedeki_kitaplar[kitap_ismi] = "Mevcut"
    def kutuphanedeki_kitaplari_goster(self):
        print("\n")
        print(40 * "-")
        print("KUTUPHANEDEKI KITAPLAR GOSTERILIYOR.")
        for index,kitap in enumerate(self.kitaplar,1):
            print(f"{index}. kitabim : {kitap}")

        print(f"{self.kutuphanedeki_kitaplar}")
    

    def odunc_verilen_kitaplari_goster(self):
        print("\n")
        print(40 * "-")
        print("Odunclu kitaplar gosteriliyor.")
        print("\n")
        print(40 * "-")
        print(f"{self.odunclu_kitaplar}")

kutuphane=Kutuphane()

while(True):
    print("""
KUTUPHANE YONETIM SISTEMINE HOSGELDINIZ.
1-KITAP EKLE
2-KITAP SIL
3-KITAP SAYISINI GOSTER
4-ODUNC KITAP AL
5-KITABI GERİ VER
6-ODUNC VERILEN KITAPLARI GOSTER
7-KUTUPHANEDEKI MEVCUT KITAPLARI GOSTER
8-CIKIS
""")
    secim=int(input("1-8 arasi secim yapiniz: "))

    if(secim==1):
        kac_tane = int(input("Kac tane kitap eklemek istiyorsunuz: "))
        for i in range(kac_tane):
            kitap_adi = input("Kitap adi giriniz: ").upper()
            kutuphane.kitap_ekle(kitap_adi)

    elif(secim==2):
        kutuphane.kutuphanedeki_kitaplari_goster()
        kitap_adi = input("Istediginiz kitabi kutuphaneden cikartiniz yani siliniz: ").upper()
        kutuphane.kitap_sil(kitap_adi)

    elif(secim==3):
        kutuphane.kitap_sayisini_goster()

    elif(secim==4):
        kutuphane.kutuphanedeki_kitaplari_goster()
        kitap_adi = input("Odunc almak istediginiz kitabın sadece ismini giriniz: ").upper()
        kutuphane.odunc_kitap_al(kitap_adi)

    elif(secim==5):
        kutuphane.odunc_verilen_kitaplari_goster()
        kitap_adi = input("Geri vermek istediginiz kitabın sadece ismini giriniz: ").upper()
        kutuphane.kitabi_geri_ver(kitap_adi)

    elif(secim==6):
        kutuphane.odunc_verilen_kitaplari_goster()

    elif(secim==7):
        kutuphane.kutuphanedeki_kitaplari_goster()

    elif(secim==8):
        print("Cikis yapiliyor...")
        break
    else:
        print("Gecersiz secim yaptiniz tekrar deneyiniz.")

