class Elemento:
    def __init__(self, num):
        self.__num = num
        self.__anterior = None
        self.__proximo = None

    def __str__(self):
        return str(self.__num)

    def get_numero(self):
        return self.__num

    def get_anterior(self):
        return self.__anterior

    def set_anterior(self, elemento):
        self.__anterior = elemento

    def get_proximo(self):
        return self.__proximo

    def set_proximo(self, elemento):
        self.__proximo = elemento