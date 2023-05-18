from sekil import Sekil

class Dikdortgen(Sekil):
    
    def __init__(self, kenar1, kenar2):

        # degiskenlere sinir kosulu
        assert kenar1 >=0, f"Kenar {kenar1} 0'dan buyuk bir deger olmali!"
        assert kenar2 >=0, f"Kenar {kenar2} 0'dan buyuk bir deger olmali!"

        self.__kenar1 = kenar1
        self.__kenar2 = kenar2
        
        # get metodlari
    def get_kenar1(self):
        return self.__kenar1
    def get_kenar2(self):
        return self.__kenar2
        
        # set metodlari
    def set_kenar1(self, kenar1):
        self.__kenar1 = kenar1
    def set_kenar2(self, kenar2):
        self.__kenar2 = kenar2

    # alan ve cevre hesabi
    def alan(self):
        return self.__kenar1 * self.__kenar2
    def cevre(self):
        return 2*(self.__kenar1 + self.__kenar2)
    
    def ciz(self):
        print("dikdortgen icin:")
        self.set_kenar1(int(input("kenar1 icin deger giriniz: ")))
        self.set_kenar2(int(input("kenar2 icin deger giriniz: ")))

    def __str__(self):
        return f"Dikdortgen icin sirasiyla cevre, alan {self.cevre()}, {self.alan()}"
