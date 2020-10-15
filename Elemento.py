class Elemento:
    def __init__(self, num):
        self.__num = num
        self.__anterior = None
        self.__proximo = None

    def __str__(self):
        return str(self.__num)

    def _get_numero(self):
        return self.__num

    def _get_anterior(self):
        return self.__anterior

    def _set_anterior(self, elemento):
        if isinstance(elemento, Elemento):
            self.__anterior = elemento
        else:
            raise Exception('O parâmetro não é da classe Elemento!')

    def _get_proximo(self):
        return self.__proximo

    def _set_proximo(self, elemento):
        if isinstance(elemento, Elemento):
            self.__proximo = elemento
        else:
            raise Exception('O parâmetro não é da classe Elemento!')