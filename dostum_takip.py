
class Hayvan():
    TOPLAM_HAYVAN_SAYISI=0
    CINS_KATEGORILERI = {
        "memeli": "Memeli",
        "kus": "Kuş",
        "balik": "Balık",
        "surungen": "Sürüngen",
        "amfibi": "Amfibi"
    }

    SAGLIK_DURUMLARI = {
        "saglikli": "Sağlıklı",
        "hasta": "Hasta",
        "tedavi_alti": "Tedavi Altı",
        "izlem_alti": "İzlem Altı"
    }

    def __init__(self, isim, yas, cins, kategori="bilinmiyor", sahip="Bilinmiyor", saglik_durumu="saglikli"):
        self.isim = isim
        self.yas = yas
        self.cins = cins
        self.kategori = kategori
        self.sahip = sahip
        self.saglik_durumu = saglik_durumu
        self.asi_kayitlari = []
        self.veteriner_muayeneleri = []
        self.ozel_notlar = []
        self.kilo = 0.0
        self.mikrochip_no = None
    def temel_bilgiler(self):
        """ Hayvanın temel bilgilerini döndürür"""
        return f"ID: {self.id}, İsim: {self.isim}, Yaş: {self.yas}, Cins: {self.cins}"
    def detayli_bilgiler(self):
        """Hayvanın detaylı bilgilerini döndürür"""
        kategori_adi = self.CINS_KATEGORILERI.get(self.kategori, "Bilinmiyor")
        saglik_adi = self.SAGLIK_DURUMLARI.get(self.saglik_durumu, "Bilinmiyor")
    def yas_kategorisi(self):
        """Yaşa göre kategori belirler"""
        if self.yas < 1:
            return "Yavru"
        elif self.yas < 3:
            return "Genç"
        elif self.yas < 8:
            return "Yetişkin"
        else:
            return "Yaşlı"
    def asi_ekle(self, asi_adi, tarih=None, veteriner="Bilinmiyor"):
        if tarih is None:
            tarih="Bugün"
        asi_kaydi = {
            'asi_adi' : asi_adi,
            'tarih' : tarih,
            'veteriner': veteriner
        }
        self.asi_kayitlari.append(asi_kaydi)
        print(f"✓ {self.isim} için {asi_adi} aşısı kaydedildi.")

    def asi_listesi(self):
        """ Tüm aşıları listeler """
        if not self.asi_kayitlari:
            print(f"{self.isim} için aşı kaydı bulunamadı.")

            print(f"\n=== {self.isim} - AŞI KAYITLARI ===")
        for i,asi in enumerate(self.asi_kayitlari,1):
            print(f"{i} {asi['asi_adi']} - {asi['tarih']} - {"Dr". asi['veteriner']}")
            
    def muayene_ekle(self,teshis="Bilinmiyor",tedavi="Bilinmiyor",veteriner="Bilinmiyor"):
        """Veteriner muayene kaydı ekler"""
        muayene={
            'teshis':teshis,
            'tedavi':tedavi,
            'veteriner':veteriner
        }

        self.veteriner_muayeneleri.append(muayene)
        print(f"✓ {self.isim} için muayene kaydı eklendi.")
    def muayene_listesi(self):
        """Tüm muayeneleri listeler"""
        if not self.veteriner_muayeneleri:
            print(f"{self.isim} icin muayene kaydı bulunamadı")
        for i,muayene in enumerate(self.veteriner_muayeneleri,1):
            print(f"{i}.Teşhis = {muayene['teshis']}")
            if muayene['tedavi']:
                print(f"Tedavi: {muayene['tedavi']}")
            print(f"Veteriner : {muayene['veteriner']}")
    def saglik_durumu_guncelle(self, yeni_durum):
        """Sağlık durumunu günceller"""
        if yeni_durum not in self.SAGLIK_DURUMLARI:
            print(f"Gecersiz saglik durumu! Gecerli saglik durumlari = {list(self.SAGLIK_DURUMLARI.keys())}")
        eski_durum = self.SAGLIK_DURUMLARI[self.saglik_durumu]
        self.saglik_durumu=yeni_durum
        yeni_durum_adi = self.SAGLIK_DURUMLARI[yeni_durum]
        print(f"✓ {self.isim} sağlık durumu güncellendi: {eski_durum} → {yeni_durum_adi}")
    def not_ekle(self,not_metni):
        """Özel not ekler"""
        self.ozel_notlar.append(not_metni)
        print(f"✓ {self.isim} için not eklendi.")
    def notlari_goster(self):
        """Tüm notları gösterir"""
        if(not self.ozel_notlar):
            print(f"{self.isim} için not bulunamadı.")
        else:
            for i,not_metni in enumerate(self.ozel_notlar,1):
                print(f"{i}.{not_metni}")
    def kilo_guncelle(self,yeni_kilo):
        """Kilo bilgisini günceller"""
        eski_kilo = self.kilo
        self.kilo = yeni_kilo
        if eski_kilo>0:
            fark = self.kilo-eski_kilo
            if fark>0:
                print(f"{self.isim} kilo aldı.Fark = {fark}")
            else:
                print(f"{self.isim} kilo verdi.Fark = {fark}")
        print(f"✓ {self.isim} kilo bilgisi kaydedildi: {yeni_kilo}kg")
    def yas_arttir(self):
        """Yaşını bir arttırır"""
        self.yas += 1
        print(f"🎂 {self.isim} yaşı güncellendi: {self.yas}")
    def sahip_degistir(self, yeni_sahip):
        eski_sahip = self.sahip
        self.sahip = yeni_sahip
        print(f"{self.isim} sahibi degisti. Eski sahip = {eski_sahip} yeni sahip = {self.sahip}")


class Kopek(Hayvan):
    """Köpek sınıfı - Hayvan sınıfından türetilmiş"""
    
    # Köpek spesifik sınıf değişkenleri
    EGITIM_SEVIYELERI = {
        "yok": "Eğitim almamış",
        "temel": "Temel eğitim",
        "orta": "Orta seviye",
        "ileri": "İleri seviye",
        "profesyonel": "Profesyonel"
    }
    
    KARAKTER_TIPLERI = {
        "sakin": "Sakin",
        "enerjik": "Enerjik",
        "oyuncu": "Oyuncu",
        "koruyucu": "Koruyucu",
        "sosyal": "Sosyal",
        "cekingen": "Çekingen",
        "ice donuk":"ice donuk",
        "disa donuk":"disa donuk"
    }
    
    def __init__(self, isim, yas, cins, kategori="memeli", sahip="Bilinmiyor", saglik_durumu="saglikli",karakter="bilinmiyor",egitim_durumu="bilinmiyor"):
        super().__init__(isim, yas, cins, kategori, sahip, saglik_durumu)
        self.egitim_durumu = egitim_durumu
        self.karakter = karakter
        self.komutlar = []
        self.oyun_alanlari = []
        self.favori_oyuncaklar = []
        self.yuruyus_suresi = 0  # dakika
        self.ogrenilen_komutlar = []
    def detayli_bilgiler(self):
        temel_bilgi = super().detayli_bilgiler()
        kopek_bilgi = f"""---KOPEK OZELLIKLERI---
        Egitim Durumu = {self.egitim_durumu}
        Karakter = {self.karakter}
        Bildigi komutlar = {self.komutlar}
        Favori oyuncaklar = {self.favori_oyuncaklar}
        Gunluk yuruyus = {self.yuruyus_suresi}
        """
    def havla(self):
        """Köpek havlama sesi"""
        print(f"🐕 {self.isim}: Hav hav!")
    def komut_ogret(self,komut):
        if(komut not in self.komutlar):
            self.komutlar.append(komut)
            print(f"✓ {self.isim} '{komut}' komutunu öğrendi!")
        else:
            print(f"{self.isim} '{komut}' komutunu zaten biliyor.")
    def komut_uygula(self,komut):
        if(komut in self.komutlar):
            print(f"🐕 {self.isim} '{komut}' komutunu uyguladı!")
        else:
            print(f"{self.isim} '{komut}' komutunu bilmiyor. Önce öğretmelisiniz.")
    def komutlari_listele(self):
        if not self.komutlar:
            print(f"{self.isim} henüz hiç komut öğrenmedi.")
        else:
            for i,komut in enumerate(self.komutlar,1):
                print(f"{i}.komut = {komut}")
    def oyuncak_ekle(self,oyuncak):
        self.favori_oyuncaklar.append(oyuncak)
        print(f"✓ {self.isim} için '{oyuncak}' oyuncağı eklendi.")
    def oyuncaklari_listele(self):
        """Favori oyuncakları listeler"""
        if not self.favori_oyuncaklar:
            print(f"{self.isim} için kayıtlı oyuncak yok.")
        else:
            for i,oyuncak in enumerate(self.favori_oyuncaklar,1):
                print(f"{i}.oyuncak = {oyuncak}")
    def yuruyus_suresi_ayarla(self, dakika):
        """Günlük yürüyüş süresini ayarlar"""
        self.yuruyus_suresi = dakika
        print(f"✓ {self.isim} için günlük yürüyüş süresi {self.yuruyus_suresi } dakika olarak ayarlandı.")
    def oyun_oyna(self,oyun_turu):
        """Köpekle oyun oynar"""
        oyun_turleri = {
            "top": f" {self.isim} top koşturuyor!",
            "ip": f" {self.isim} ip çekme oyunu oynuyor!",
            "saklambaç": f" {self.isim} saklambaç oynuyor!",
            "koşu": f" {self.isim} koşu yapıyor!"
        }
        if(oyun_turu in oyun_turleri.keys()):
            print(f"{oyun_turleri[oyun_turu]}")    
    def uyu(self,kac_saat):
        print(f"{self.isim} {kac_saat} uyudu.")
    def yemek_ye(self,yemek_adi):
        print(f"{self.isim} {yemek_adi} yemegini yedi.")
    def yasa_gore_durum(self):
        pass
    def kos(self):
        pass
    def enerji_seviyesi(self,seviye):
        print(f"{self.isim} enerji seviyesi = {seviye}")
    def egitilme_durumu(self):
        pass
    def komutu_biliyor_mu(self):
        pass
    def saglik_durumu(self):
        pass
    def sahibi_var_mi(self):
        pass
    def kuyruk_salla(self):
        pass
    def koku_al(self):
        pass
    def diger_kopeklerle_tanis(self):
        pass
    def ates_olc(self):
        pass
    def temel_egitim_ver(self,komutlar=None):
        if komutlar is None:
            komut_listesi  = ["otur", "dur", "gel", "yat", "bekle"]
        print(f"{self.isim} icin temel egitim basliyor.")
        for komut in komut_listesi:
            self.ogrenilen_komutlar.append(komut)
        print(f"{self.isim} temel egitimi tamamladi.")
        print(self.ogrenilen_komutlar)




kopek1 = Kopek(isim="Boncuk", yas=2, cins="Golden Retriever", sahip="Ahmet")
kopek1.havla()
kopek1.oyun_oyna("top")
kopek1.temel_egitim_ver()
