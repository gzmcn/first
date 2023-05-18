from sekil import Sekil

class Ucgen(Sekil):
    
    def __init__(self, kenar1, kenar2, kenar3, taban, yukseklik):

        # degiskenlere sinir kosulu
        assert kenar1 >=0, f"Kenar {kenar1} 0'dan buyuk bir deger olmali!"
        assert kenar2 >=0, f"Kenar {kenar2} 0'dan buyuk bir deger olmali!"
        assert kenar3 >=0, f"Kenar {kenar3} 0'dan buyuk bir deger olmali!"
        assert taban >=0, f"Kenar {taban} 0'dan buyuk bir deger olmali!"
        assert yukseklik >=0, f"Kenar {yukseklik} 0'dan buyuk bir deger olmali!"
       
        self.__kenar1 = kenar1
        self.__kenar2 = kenar2
        self.__kenar3 = kenar3
        self.__taban = taban
        self.__yukseklik = yukseklik

        # get metodlari
    def get_kenar1(self):
            return self.__kenar1
    def get_kenar2(self):
            return self.__kenar2
    def get_kenar3(self):
            return self.__kenar3
    def get_taban(self):
            return self.__taban
    def get_yukseklik(self):
            return self.__yukseklik

        # set metodlari
    def set_kenar1(self, kenar1):
            self.__kenar1 = kenar1
    def set_kenar2(self, kenar2):
            self.__kenar2 = kenar2
    def set_kenar3(self, kenar3):
            self.__kenar3 = kenar3
    def set_taban(self, taban):
            self.__taban = taban
    def set_yukseklik(self, yukseklik):
            self.__yukseklik = yukseklik
    def set_taban(self, taban):
        self.__taban = taban
    def set_taban(self, yukseklik):
        self.__yukseklik = yukseklik

    # alan ve cevre hesabi
    def alan(self):
           return self.__yukseklik * self.__taban * 0.5
    def cevre(self):
           return self.__kenar1 + self.__kenar2 + self.__kenar3
    
    
    def ciz(self):
        print("ucgen icin:")
        self.set_kenar1(int(input("kenar1 icin deger giriniz: ")))
        self.set_kenar2(int(input("kenar2 icin deger giriniz: ")))
        self.set_kenar3(int(input("kenar3 icin deger giriniz: ")))
        self.set_taban(int(input("taban icin deger giriniz: ")))
        self.set_yukseklik(int(input("yukseklik icin deger giriniz: ")))

    def __str__(self):
        return f"Ucgen icin sirasiyla cevre, alan {self.cevre()}, {self.alan()}"

    """
        # degiskenlere sinir kosulu
        assert kenar1 >=0, f"Kenar {kenar1} 0'dan buyuk bir deger olmali!"
        assert kenar2 >=0, f"Kenar {kenar2} 0'dan buyuk bir deger olmali!"
        assert kenar3 >=0, f"Kenar {kenar3} 0'dan buyuk bir deger olmali!"

        #self
        self.__kenar1 = kenar1
        self.__kenar2 = kenar2
        self.__kenar3 = kenar3
    """