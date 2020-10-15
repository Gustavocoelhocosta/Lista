Implementação de Lista duplamente encadeada



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

vazia
Verifica se a lista está vazia retorna Verdadeiro ou Falso

cheia
Verifica se a lista está cheia retorna Verdadeiro ou Falso

contem
Verifica se um elemento está contido na lista a partir de uma chave através de busca linear, retorna verdadeiro ou falso.
caso a lista esteja vazia retorna falso
Aponta o cursor para o início da lista
compara a chave do cursor com a chave do parâmetro se for a mesma retorna verdadeiro.
Se for falso aponta o cursos para o próximo elemento da lista e faz nova comparação de chaves até encontrar o elemento retornando Verdadeiro ou chegar ao final da lista sem encontrar retornando falso.
No caso do elemento for encorntrado, Retorna falso e o cursosr permanece apontado para o elemento encontrado
Com um contador verifica se a busca foi feita até o final da lista.


posicao_de
Retorna a posição de um elemento a partir de uma chave
invoca método "contem"
se não encontrar
        self._contem(chave)
        return self._get_posicao_cursor()

    def _eh_elemento(self, elemento):
        return isinstance(elemento, Elemento)

    def _eh_inteiro(self, numero):
        return isinstance(numero, int)


#estrutura#

acessar_atual
retorna o elemento apontado pelo cursor
caso a lista estiver vasia levanta uma exceção


remove_atual
Exclui elemento que está apontado pelo cursor da lista.
Aponta o cursor para o primeiro elemento restante da lista.
No caso da lista conter apenas um elemento seta a alista numa lista vazia.
No caso da lista estar vazia, levanta uma exceção.

inserir_vazio
Inseri o primeiro elemento da lista
Se o parametro não for da classe Elemento levanta uma exceção.

inserir_apos_atual
Inseri um elemento após o elemento que o cursor estiver apontando.
se a lista estiver vazia invoca o método "inserir_vazio"
se o cursor estiver apontando para o útimo elemento, o elemento inserido se torna o novo fim da lista.
Se o parametro não for da classe Elemento levanta uma exceção.
Se a lista estiver cheia levanta uma exceção.



inserir_antes_atual
Inseri um elemento antes o elemento que o cursor estiver apontando.
se a lista estiver vazia invoca o método "inserir_vazio"
se o cursor estiver apontando para o primeiro elemento, o elemento inserido se torna o novo início da lista.
Se o parametro não for da classe Elemento levanta uma exceção.
Se a lista estiver cheia levanta uma exceção.

buscar
Busca um elemento a partir da chave, aponta o cursor para o elemento caso encontre, e retorna o cursor.
caso não encontre o elemento levanta exceção


listar
retorna um string contendo os valores de todos elementos da lista, ordenadamente, a partir do início até o fim e separados por vírgula.
caso a lista esteja vazia levanta exceção




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
        self._ir_para_inicio()
        self._avancar(posicao)
        self.remove_atual()

    def remover_primeiro(self):
        self._ir_para_inicio()
        self.remove_atual()

    def remover_ultimo(self):
        self._ir_para_fim()
        self.remove_atual()

    def remover_elemento(self, chave):
        self.buscar(chave)
        self.remove_atual()