from Elemento import Elemento

class Lista:
    def __init__(self, limite):
        self.__limite = limite
        self.__numero_de_elementos = 0
        self.__inicio = None
        self.__cursor = None
        self.__posicao_cursor = None

    def _get_inicio(self):
        return self.__inicio

    def _get_fim(self):
        return self._get_inicio()._get_anterior()

    def _get_cursor(self) -> object:
        return self.__cursor

    def _get_posicao_cursor(self):
        return self.__posicao_cursor

    def _get_numero_de_elementos(self):
        return self.__numero_de_elementos

    def _get_limite(self):
        return self.__limite

    def _set_inicio(self, elemento):
        self.__inicio = elemento

    def _set_fim(self, elemento):
        self.__fim = elemento

    def _set_cursor(self, elemento):
        self.__cursor = elemento

    def _set_posicao_cursor(self, posicao):
        self.__posicao_cursor = posicao

    def _set_numero_de_elementos(self, numero):
        self.__numero_de_elementos = numero

    def _set_limite(self, limite):
        self.__limite = limite

# Operações Básicas Atômicas

    def _ir_para_inicio(self):
        self._set_cursor(self._get_inicio())
        self._set_posicao_cursor(0)


    def _ir_para_fim(self):
        self._ir_para_inicio()
        self._retroceder(1)
        self._set_posicao_cursor(self._get_numero_de_elementos()-1)


    def _avancar(self, posicoes):
        contador = 0
        while contador < posicoes:
            self._set_cursor(self._get_cursor()._get_proximo())
            contador += 1
            self._set_posicao_cursor((self._get_posicao_cursor()+1)&(self._get_numero_de_elementos()-1))



    def _retroceder(self, posicoes):
        contador = 0
        while contador < posicoes:
            self._set_cursor(self._get_cursor()._get_anterior())
            contador += 1
            self._set_posicao_cursor((self._get_posicao_cursor()-1)&(self._get_numero_de_elementos()-1))

# consultas

    def _vazia(self):
        return self.__numero_de_elementos == 0

    def _cheia(self):
        return self.__numero_de_elementos == self._get_limite()

    def _contem(self, chave):
        if self.buscar(chave):
            return True
        else:
            return False

    def _posicao_de(self, chave):
        if self._contem(chave):
            return self._get_posicao_cursor()
        else:
            raise Exception('elemento não foi encontrado na lista')

    def _eh_elemento(self, elemento):
        return isinstance(elemento, Elemento)

    def _eh_inteiro(self, numero):
        return isinstance(numero, int)


#estrutura#

    def acessar_atual(self):
        if self._vazia():
            raise Exception('Não foi possivel acessár o cursor pois a lista está vazia')
        else:
            return self._get_cursor()

    def remove_atual(self):
        if self._vazia():
            raise Exception('Não foi possivel exluir o cursor pois a lista está vazia')
        elif self._get_numero_de_elementos() == 1:
            self._set_numero_de_elementos(0)
            self._set_inicio(None)
            self._set_fim(None)
            self._set_cursor(None)
            self._set_posicao_cursor(None)
        else:
            cursor = self._get_cursor()
            proximo = cursor._get_proximo()
            anterior = cursor._get_anterior()

            if cursor == self._get_inicio():
                self._set_inicio(proximo)
            if cursor == self._get_fim():
                self._set_fim(anterior)

            cursor._get_anterior()._set_proximo(proximo)
            cursor._get_proximo()._set_anterior(anterior)
            self._set_numero_de_elementos(self._get_numero_de_elementos() - 1)
            self._ir_para_inicio()

    def _inserir_vazio(self, elemento):
        if self._eh_elemento(elemento):
            elemento._set_anterior(elemento)
            elemento._set_proximo(elemento)
            self._set_cursor(elemento)
            self._set_posicao_cursor(0)
            self._set_inicio(elemento)
            self._set_numero_de_elementos(1)
        else:
            raise Exception("Parâmetro não é da classe Elemento")

    def inserir_apos_atual(self, elemento):
        cursor = self._get_cursor()
        if not self._eh_elemento(elemento):
            raise Exception("Parâmetro não é da classe Elemento")
        if self._cheia():
            raise Exception("Não foi possível inserir pois a lista esta cheia")
        if self._vazia():
            self._inserir_vazio(elemento)
            return None
        if cursor == self._get_fim():
            self._set_fim(elemento)
        elemento._set_anterior(cursor)
        elemento._set_proximo(cursor._get_proximo())
        cursor._get_proximo()._set_anterior(elemento)
        cursor._set_proximo(elemento)
        self._set_numero_de_elementos( self._get_numero_de_elementos() + 1)
        return None

    def inserir_antes_atual(self, elemento):
        cursor = self._get_cursor()
        if not self._eh_elemento(elemento):
            raise Exception("Parâmetro não é da classe Elemento")
        if self._cheia():
            raise Exception("Não foi possível inserir pois a lista esta cheia")
        if self._vazia():
            self._inserir_vazio(elemento)
            return None
        if cursor == self._get_inicio():
            self._set_inicio(elemento)
        elemento._set_proximo(cursor)
        elemento._set_anterior(cursor._get_anterior())
        cursor._get_anterior()._set_proximo(elemento)
        cursor._set_anterior(elemento)
        self._set_numero_de_elementos(self._get_numero_de_elementos() + 1)
        return None

    def buscar(self, chave):
        if self._vazia():
            return False
        else:
            fake = Elemento(chave)
            self.inserir_no_final(fake)
            self._ir_para_inicio()
            contador = 0
            while self._get_cursor()._get_numero() != chave:
                self._avancar(1)
            if self._get_cursor() == fake:
                self.remover_ultimo()
                return False
            else:
                self.remover_ultimo()
                self._ir_para_inicio()
                return True


    def lista(self):
        if not self._vazia():
            contador = 1
            self._ir_para_inicio()
            lista = str(self._get_cursor())
            while contador < self._get_numero_de_elementos():
                self._avancar(1)
                lista = lista + "," + str(self._get_cursor())
                contador += 1
            return lista

        else:
            raise Exception('não foi possivel imprimir a lista pois ela está vazia')


#Operações “sofisticadas”

    def inserir_na_frente(self, elemento):
        if self._vazia():
            self._inserir_vazio(elemento)
        else:
            self._ir_para_inicio()
            self.inserir_antes_atual(elemento)

    def inserir_no_final(self, elemento):
        if self._vazia():
            self._inserir_vazio(elemento)
        else:
            self._ir_para_fim()
            self.inserir_apos_atual(elemento)

    def inserir_na_posicao(self, posicao, elemento):
        if self._eh_inteiro(posicao):
            if posicao < (self._get_numero_de_elementos()-1):
                self._ir_para_inicio()
                self._avancar(posicao-1)
                self.inserir_apos_atual(elemento)
            else:
                raise Exception('Posição informada não existe na lista')
        else:
            raise Exception('Parâmetro posição não é um inteiro')

    def remover_da_posicao(self, posicao):
        if isinstance(posicao, int):
            if posicao < (self._get_numero_de_elementos()-1):
                self._ir_para_inicio()
                self._avancar(posicao)
                self.remove_atual()
            else:
                raise Exception('Posição informada não existe na lista')
        else:
            raise Exception('Parâmetro posição não é um inteiro')

    def remover_primeiro(self):
        self._ir_para_inicio()
        self.remove_atual()

    def remover_ultimo(self):
        self._ir_para_fim()
        self.remove_atual()

    def remover_elemento(self, chave):
        self.buscar(chave)
        self.remove_atual()