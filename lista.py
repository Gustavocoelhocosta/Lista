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


class Lista:
    def __init__(self, limite):
        self.__limite = limite
        self.__numero_de_elementos = 0
        self.__inicio = None
        self.__cursor = None
        self.__posicao_cursor = None

    def get_inicio(self):
        return self.__inicio

    def get_fim(self):
        return self.get_inicio().get_anterior()

    def get_cursor(self):
        return self.__cursor

    def get_posicao_cursor(self):
        return self.__posicao_cursor

    def get_numero_de_elementos(self):
        return self.__numero_de_elementos

    def get_limite(self):
        return self.__limite

    def set_inicio(self, elemento):
        self.__inicio = elemento

    def set_fim(self, elemento):
        self.__fim = elemento

    def set_cursor(self, elemento):
        self.__cursor = elemento

    def set_posicao_cursor(self, posicao):
        self.__posicao_cursor = posicao

    def set_numero_de_elementos(self, numero):
        self.__numero_de_elementos = numero

    def set_limite(self, limite):
        self.__limite = limite

# Operações Básicas Atômicas

    def ir_para_inicio(self):
        self.set_cursor(self.get_inicio())
        self.set_posicao_cursor(0)

    def ir_para_fim(self):
        self.ir_para_inicio()
        self.retroceder(1)
        self.set_posicao_cursor(self.get_numero_de_elementos()-1)

    def avancar(self, posicoes):
        contador = 0
        while contador < posicoes:
            self.set_cursor(self.get_cursor().get_proximo())
            contador += 1
            self.set_posicao_cursor((self.get_posicao_cursor()+1)&(self.get_numero_de_elementos()-1))

    def retroceder(self, posicoes):
        contador = 0
        while contador < posicoes:
            self.set_cursor(self.get_cursor().get_anterior())
            contador += 1
            self.set_posicao_cursor((self.get_posicao_cursor()-1)&(self.get_numero_de_elementos()-1))

# consultas

    def vazia(self):
        return self.__numero_de_elementos == 0

    def cheia(self):
        return self.__numero_de_elementos == self.get_limite()

    def contem(self, chave):
        if self.vazia():
            return False
        else:
            self.ir_para_inicio()
            contador = 0
            while self.get_cursor().get_numero() != chave:
                if contador == self.get_numero_de_elementos() - 1:
                    self.ir_para_inicio()
                    return False
                self.avancar(1)
                contador += 1
            return True

    def posicao_de(self, chave):
        self.contem(chave)
        return self.get_posicao_cursor()

    def eh_elemento(self, elemento):
        return isinstance(elemento, Elemento)

#estrutura#

    def acessar_atual(self):
        return get_cursor()

    def remove_atual(self):
        cursor = self.get_cursor()
        proximo = cursor.get_proximo()
        anterior = cursor.get_anterior()

        if cursor == self.get_inicio():
            self.set_inicio(proximo)
        if cursor == self.get_fim():
            self.set_fim(anterior)

        cursor.get_anterior().set_proximo(proximo)
        cursor.get_proximo().set_anterior(anterior)
        self.set_numero_de_elementos(self.get_numero_de_elementos() - 1)
        self.ir_para_inicio()

    def inserir_vazio(self, elemento):
        if self.eh_elemento(elemento):
            elemento.set_anterior(elemento)
            elemento.set_proximo(elemento)
            self.set_cursor(elemento)
            self.set_posicao_cursor(0)
            self.set_inicio(elemento)
            self.set_numero_de_elementos(1)
        else:
            return print("Objeto não é da classe Elemento")

    def inserir_apos_atual(self, elemento):
        cursor = self.get_cursor()
        if not self.eh_elemento(elemento):
            return print("Objeto não é da classe Elemento")
        if self.cheia():
            return print("Não foi possível inserir pois a lista esta cheia")
        if self.vazia():
            self.inserir_vazio(elemento)
            return None
        if cursor == self.get_fim():
            self.set_fim(elemento)
        elemento.set_anterior(cursor)
        elemento.set_proximo(cursor.get_proximo())
        cursor.get_proximo().set_anterior(elemento)
        cursor.set_proximo(elemento)
        self.set_numero_de_elementos( self.get_numero_de_elementos() + 1)
        return None

    def inserir_antes_atual(self, elemento):
        cursor = self.get_cursor()
        if not self.eh_elemento(elemento):
            return ("Objeto não é da classe Elemento")
        if self.cheia():
            return print("Não foi possível inserir pois a lista esta cheia")
        if self.vazia():
            self.inserir_vazio(elemento)
            return None
        if cursor == self.get_inicio():
            self.set_inicio(elemento)
        elemento.set_proximo(cursor)
        elemento.set_anterior(cursor.get_anterior())
        cursor.get_anterior().set_proximo(elemento)
        cursor.set_anterior(elemento)
        self.set_numero_de_elementos(self.get_numero_de_elementos() + 1)
        return None

    def buscar(self, chave):
        if self.contem(chave):
            return self.get_cursor()
        else:
            print("elemento não encontrado")
            return None

    def lista(self):
        contador = 1
        self.ir_para_inicio()
        lista = str(self.get_cursor())
        while contador < self.get_numero_de_elementos():
            self.avancar(1)
            lista = lista + "," + str(self.get_cursor())
            contador += 1
        return lista


#Operações “sofisticadas”

    def inserir_na_frente(self, elemento):
        if self.vazia():
            self.inserir_vazio(elemento)
        else:
            self.ir_para_inicio()
            self.inserir_antes_atual(elemento)

    def inserir_no_final(self, elemento):
        if self.vazia():
            self.inserir_vazio(elemento)
        else:
            self.ir_para_fim()
            self.inserir_apos_atual(elemento)

    def inserir_na_posicao(self, posicao, elemento):
        self.ir_para_inicio()
        self.avancar(posicao-1)
        self.inserir_apos_atual(elemento)

    def remover_da_posicao(self, posicao):
        self.ir_para_inicio()
        self.avancar(posicao)
        self.remove_atual()

    def remover_primeiro(self):
        self.ir_para_inicio()
        self.remove_atual()

    def remover_ultimo(self):
        self.ir_para_fim()
        self.remove_atual()

    def remover_elemento(self, chave):
        self.buscar(chave)
        self.remove_atual()

# teste ordenação:

    def passar_atual_para_frente(self):
        a = self.get_cursor().get_anterior()
        b = self.get_cursor()
        c = self.get_cursor().get_proximo()
        d = self.get_cursor().get_proximo().get_proximo()
        if b == self.get_inicio():
            self.set_inicio(c)
        a.set_proximo(c)

        c.set_anterior(a)
        c.set_proximo(b)

        b.set_anterior(c)
        b.set_proximo(d)

        d.set_anterior(b)




    def ordenar(self):
        self.ir_para_inicio()
        teste = 0
        contador = 0
        while contador != (self.get_numero_de_elementos()-1):
            for i in range(self.get_numero_de_elementos()-1):
                print(self.get_cursor())
                print(self.get_cursor().get_proximo())
                if self.get_cursor().get_numero() > (self.get_cursor().get_proximo().get_numero()):
                    print('troca')
                    self.passar_atual_para_frente()
                    teste += 1
                else:
                    contador += 1
                    self.avancar(1)
                    print('avança')
            self.ir_para_inicio()
        return None




a = Elemento(1)
b = Elemento(2)
c = Elemento(3)
d = Elemento(4)
e = Elemento(5)
f = Elemento(6)



l = Lista(8)
l.inserir_no_final(a)
l.inserir_no_final(b)
l.inserir_no_final(c)
l.inserir_no_final(d)
l.inserir_no_final(e)
l.inserir_no_final(f)
print(l.lista())

l.ir_para_inicio()


l.ordenar()
print(l.lista())
