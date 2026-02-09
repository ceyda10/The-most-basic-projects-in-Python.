def ogrenci_not_sistemi() : 
    ogrenci_notlari = {
        "John": 90,
        "Melissa": 95,
        "David": 70,
        "Sarah": 65,
}
    while True :
        print("ÖĞrenci Yönetim Sistemine Hoşgeldiniz!")
        print("1 - Not Sorgula")
        print("2 - Yeni Öğrenci Kaydet")
        print("3 - Çıkış ")
        secim = input("Lütfen istediğiniz işlemin numarasını giriniz: ")
        if secim == "1" :
            not_sorgula = input("Hangi öğrencinin notunu öğrenmek istiyorsun?").capitalize()
            if not_sorgula in ogrenci_notlari :
                print(f"{not_sorgula} adlı öğrencinin notu: {ogrenci_notlari[not_sorgula]}")
            else :
                print(f"{not_sorgula} üzgünüm bu isimde bir öğrenci bulunmamaktadır.")
        elif secim == "2" :
            yeni_ogrenci = input("Yeni öğrencinin ismini giriniz:").capitalize()
            yeni_not = int(input("Yeni öğrencinin notunu giriniz:"))
            ogrenci_notlari[yeni_ogrenci] = yeni_not
            print(f"{yeni_ogrenci} adlı öğrenci başarıyla kaydedildi.")
            print(f"Güncel Liste: {ogrenci_notlari}")
        elif secim == "3" :
            print("Sistemden çıkış yapılıyor...")
            break
        
    
ogrenci_not_sistemi()
    