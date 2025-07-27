
class Tesla:
    sis_fari = 2   #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    tekerlek_sayisi = 4 #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    tesla_count  = 0 #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    tork = 1500 #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    GECERLI_RENKLER = ["KIRMIZI","BEYAZ","SIYAH"] #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    SARJ_TIPLERI = ["AC", "DC", "SUPERCHARGER"] #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    MEVCUT_MODELLER = ["MODEL S", "MODEL 3", "MODEL X", "MODEL Y"] #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    hiz_limiti = 322  #Sınıf değişkeni.Her teslada olan özellikler bunlardir.
    hiz_seviyesi = 0 #Sınıf değişkeni.Her teslada olan özellikler bunlardir.

    def __init__(self,renk,sarj,jant):
        if renk in Tesla.GECERLI_RENKLER:
            self.__renk = renk    #"__" kullanma sebebim güvenlik içindir.Dışarıdan değiştirilemesin diye.
        else:
            self.__renk = "BEYAZ"
        
        if sarj in Tesla.SARJ_TIPLERI:
            self.__sarj = sarj
        else:
            print(f"{sarj} {Tesla.SARJ_TIPLERI} listemizde yoktur.Tekrar deneyiniz.")
        self.tork = Tesla.tork
        Tesla.tesla_count += 1
        self._jant = jant
        print("init cagrildi.")

    def torku_yukselt(self,tork_miktari):
        if tork_miktari < 0:
            print("Sifirdan buyuk deger giriniz. ")
        else:
            tesla.tork += tork_miktari

    def torku_azalt(self,tork_miktari):
        if tork_miktari > self.tork:
            print("Girilen tork miktari mevcut tork miktarindan buyuk.Azaltilamaz.")
        else:
            self.tork -= tork_miktari
        if self.tork < 0:
            self.tork = 0
    
    def goster_bilgi(self):
        print(f"{self.tork}",
              f" {self.__renk}")
    
    def tesla_sayisi_goster(self):
        print(f"Tesla sayisi = {Tesla.tesla_count}")

    def renk_degistir(self,renk_adi):
        if renk_adi.upper() == self.__renk:
            print(f"Değiştirmek istediginiz renk zaten şuanki arabanizin rengi.Değiştirilemez.")
        else:
            renk_adi = renk_adi.upper()
            if renk_adi != self.__renk:
                if renk_adi in Tesla.GECERLI_RENKLER:
                    self.__renk = renk_adi
                    print(f"{self.__renk} olarak değiştirildi.")
                else:
                    print(f"{renk_adi} {Tesla.GECERLI_RENKLER} listesinde olmadigi için değiştirilemez.")

    def hizlan(self,hiz_miktari):
        if hiz_miktari > Tesla.hiz_limiti:
            print("Hizlanamaz.Cunku girdiginiz hiz miktari hiz limitinden buyuk.")
        else:
            Tesla.hiz_seviyesi += hiz_miktari
            if Tesla.hiz_seviyesi >  Tesla.hiz_limiti:
                print("Gecersiz.Hiz limitinden kucuk olmalidir.")
            else:
                print(f"{hiz_miktari} km hizlanmistir.Yeni hiz seviyeniz: {Tesla.hiz_seviyesi}")   
    
    def yavasla(self,hiz_miktari):
        if hiz_miktari > Tesla.hiz_seviyesi:
            print(f"{hiz_miktari} {Tesla.hiz_seviyesi}'nden buyuktur.Yavaslayamaz")
        else:
            Tesla.hiz_seviyesi -= hiz_miktari

    def jant_getir(self,yeni_jant):
        if 19<=yeni_jant<=22:
            self._jant = yeni_jant
        else:
            print("Yanlis jant degeri girdiniz.")
    def hiz_seviyesini_goster(self):
        print(f"{Tesla.hiz_seviyesi}")

tesla = Tesla("TURUNCU","DC",30)

renk_ismi = input("Renk ismi girin:z ") 
tesla.renk_degistir(renk_ismi)
hiz = int(input("Hizlanmak istediginiz seviyeyi giriniz: "))
tesla.goster_bilgi()
tesla.hizlan(hiz)
tesla.hiz_seviyesini_goster()
