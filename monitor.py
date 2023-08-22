class Monitor:
    contador_monitor = 0
    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'ID Monitor : {self._id_monitor} | Marca : {self._marca} | Tamaño : {self._tamaño}'

if __name__ == '__main__':
    monitor1 = Monitor('Acer' , 28)
    print(monitor1)
    monitor2 = Monitor('Lenovo', 17)
    print(monitor2)
