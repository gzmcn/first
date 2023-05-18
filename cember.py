from sekil import Sekil

class Cember(Sekil):
    pi = 3.14
    def __init__(self, yaricap):
        # degiskenlere sinir kosulu
        assert yaricap >=0, f"Kenar {yaricap} 0'dan buyuk bir deger olmali!"

        self.__yaricap = yaricap

    def get_yaricap(self):
            return self.__yaricap
    
    def set_yaricap(self, yaricap):
            self.__kenar3 = yaricap


    def cember_ciz(self):
        self.set_yaricap = float(input("yaricap giriniz: "))
    
    # alan ve cevre hesabi
    def alan(self):
         return self.pi * self.__yaricap**2
    def cevre(self):
         return 2* self.pi * self.__yaricap

    def __str__(self):
        return f"Cember icin sirasiyla cevre, alan {self.cevre()}, {self.alan()}"