from Raton import Raton
from Teclado import Teclado
from monitor import Monitor


class Computadora:
    contador_computadoras = 0

    def __init__(self,nombre,teclado,raton,monitor):
        Computadora.contador_computadoras += 1

        self._id_computadoras = Computadora.contador_computadoras
        self._nombre = nombre
        self._teclado = teclado
        self._raton = raton
        self._monitor = monitor

    def __str__(self):
        return f'''
        Computadora : {self._nombre} | ID : {self._id_computadoras}
        {self._teclado}
        {self._raton}
        {self._monitor}
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
    print(computadora1)
    print(computadora2)
    print(computadora3)