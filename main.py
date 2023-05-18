from sekil import Sekil
from dikdortgen import Dikdortgen
from ucgen import Ucgen
from cember import Cember

def main():
    dikdortgen = Dikdortgen(3,5)
    ucgen = Ucgen(2,3,4,2,2)
    cember = Cember(5)

    print(dikdortgen)
    print(ucgen)
    print(cember)

    dikdortgen.ciz()
    ucgen.ciz()
    cember.ciz()

    print(dikdortgen)
    print(ucgen)

    dikdortgen = Dikdortgen(22,3)
    print(dikdortgen)

main()
