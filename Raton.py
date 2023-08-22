from dispositivos_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_raton = 0
    def __init__(self,tipo_entrada, marca):
        Raton.contador_raton += 1
        self._id_raton = Raton.contador_raton
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'ID Raton : {self._id_raton} | Tipo de Entrada : {self._tipo_entrada} | Marca : {self._marca}'




