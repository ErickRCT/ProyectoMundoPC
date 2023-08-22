from Raton import Raton
from Teclado import Teclado
from computadora import Computadora
from monitor import Monitor


class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def AgregarComputadora(self, computadora):
        self._computadoras.append(computadora)


    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        Orden : {self._id_orden}
        Computadoras : {computadoras_str}
        '''


if __name__ == '__main__':
    monitor1 = Monitor('Acer', 28)
    monitor2 = Monitor('Lenovo', 17)
    teclado1 = Teclado('USB', 'Samsung')
    teclado2 = Teclado('Bluetooth', 'Apple')
    raton1 = Raton('USB', 'Acer')
    raton2 = Raton('Bluetooth', 'Apple')

    computadora1 = Computadora('Gamer', monitor1, teclado1, raton1)
    computadora2 = Computadora('Asus', monitor2, teclado2, raton2)
    computadora3 = Computadora('Apple', monitor1, teclado2, raton1)

    computadoras1 = [computadora1, computadora2 , computadora3]
    computadoras2 = [computadora3, computadora2]
    computadoras3 = [computadora2, computadora1, computadora3]



    orden1 = Orden(computadoras1)
    orden2 = Orden(computadoras2)
    orden3 = Orden(computadoras3)
    print(orden1)
    print(orden2)
    print(orden3)