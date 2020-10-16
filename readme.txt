Universidade Federal de Santa Catarina
INE5609-03238A (20201) - Estruturas de Dados
Aluno: Gustavo Coelho da Costa (19100860)
Trabalho 1 - Lista Duplamente Encadeada


Implementação de Lista duplamente encadeada


Criação de uma classe chamada Lista que armazena exclusivamente objetos da classe Elemento.
A lista é cíclica por isso o próximo elemento depois do último é o primeiro elemento.

A classe Elemento possui os seguintes atributos:

num --> número do elemento em si.
anterior --> elemento anterior ao elemento em si.
próximo --> elemento posterior ao elemento em si.

geters de todos os atributos são privados.
get_numero --> retorna o número do elemento em si.
get_anterior --> retorna o elemento anterior ao número.
get_proximo --> retorna o elemento posterior ao número.

setters de todos os atributos são privados.
set_numero --> altera o número do elemento em si.
set_anterior --> altera o elemento anterior ao número. verifica se o elemento alterado é da classe Elemento, se não levanta exceção.
set_proximo --> altera a elemento posterior ao número. verifica se o elemento alterado é da classe Elemento, se não levanta exceção.


Para a Lista ser instanciada é necessário fornecer o número de elementos máximo que a lista pode conter e a lista começa vazia.

A classe lista contém os seguintes atributos:
- limite --> o número máximo de elementos que uma lista pode conter.
- número de elementos --> o número de elementos que contem na lista. inicia em 0.
- inicio --> o primeiro elemento da lista. inicia em None.
- cursor --> um indicador que pode apontar para qualquer um dos elementos da lista. inicia em None.
- posição do cursor --> a posição do cursor em relação ao primeiro elemento ( o primeiro elemento tem posição igual a 0) inicia em None.


MÉTODOS

geters de todos os atributos são privados.

_get_inicio --> retorna o primeiro elemento da lista.
_get_fim --> retorna o último elemento da lista.
_get_cursor --> retorna o elemento que o cursor está apontado.
_get_posicao_cursor --> retorna a posição do elemento que o cursor está apontado.
_get_numero_de_elementos --> retorna o número total de elementos da lista.
_get_limite --> retorna o número máximo de elementos da lista.


setters de todos os atributos são privados.

_set_inicio --> altera o primeiro elemento da lista.
_set_fim --> altera o último elemento da lista.
_set_cursor --> altera o elemento que o cursor está apontado.
_set_posicao_cursor --> altera a posição do elemento que o cursor está apontado.
_set_numero_de_elementos --> altera o número total de elementos da lista.
_set_limite --> altera o número máximo de elementos da lista.



# Operações Básicas Atômicas

ir_para_inicio
Aponta o cursor para o primeiro elemento da lista.

_ir_para_fim
Aponta o cursor para o último elemento da lista.

_avancar
avança o cursor pela lista.
pede o número de avanços a serem realizados.
seta o cursor pelo próximo elemento dele mesmo um número definido de vezes.

_retroceder
retrocede o cursor pela lista.
pede o número de retrocessos a serem realizados.
seta o cursor pelo elemento anterior a ele mesmo um número definido de vezes.

# consultas

vazia
Verifica se a lista está vazia a partir do atributo número de elementos.
Retorna Verdadeiro ou Falso

cheia
Verifica se a lista está cheia comparando o número de elementos com o limite.
Retorna Verdadeiro ou Falso

contem
Verifica se um elemento está na lista a partir da chave.
invoca o método “busca” e caso encontre o elemento retorna Verdadeiro se não encontrar retorna Falso.

posicao_de
Retorna a posição de um elemento a partir de uma chave
invoca método “busca” caso ache o elemento retorna sua posição.
caso não encontre levanta exceção


#estrutura#
acessar_atual
retorna o elemento apontado pelo cursor
caso a lista estiver vazia levanta uma exceção

listar
retorna um string contendo os valores de todos elementos da lista, ordenadamente, a partir do início até o fim e separados por vírgula.
caso a lista esteja vazia levanta exceção

inserir_vazio
Inseri o primeiro elemento da lista
Se o parâmetro não for da classe Elemento levanta uma exceção.

inserir_apos_atual
Inseri um elemento após o elemento que o cursor estiver apontando.
se a lista estiver vazia invoca o método “inserir_vazio”
se o cursor estiver apontando para o último elemento, o elemento inserido se torna o novo fim da lista.
Se o parâmetro não for da classe Elemento levanta uma exceção.
Se a lista estiver cheia levanta uma exceção.

inserir_antes_atual
Inseri um elemento antes o elemento que o cursor estiver apontando.
se a lista estiver vazia invoca o método “inserir_vazio”
se o cursor estiver apontando para o primeiro elemento, o elemento inserido se torna o novo início da lista.
Se o parâmetro não for da classe Elemento levanta uma exceção.
Se a lista estiver cheia levanta uma exceção.

buscar
Busca elemento na lista a partir de uma chave através de busca linear, retorna verdadeiro ou falso.
caso a lista esteja vazia retorna falso
inseri um elemento falso ao fim da lista com a mesma chave a ser procurada.
Aponta o cursor para o início da lista, e percorre ela apontando o cursor e comparando a chave do elemento procurado com a chave do cursor.
Ao encontrar verifica se o elemento encontrado não é o fake inserido no final da lista, se não for, retorna verdadeiro, se for, retorna falso.


#Operações “sofisticadas”

inserir_na_frente
Inseri um elemento no início da lista.
invoca o método “ir_para_inicio”
invoca o método “inserir_antes_atual”

inserir_no_final
Inseri um elemento no final da lista.
invoca o método “ir_para_fim”
invoca o método “inserir_apos_atual”

inserir_na_posicao
Inseri um elemento na posição informada através de um inteiro.
verifica se a posição informada é um inteiro, se não for levanta exceção
verifica se a posição informada existe na lista, se não existir levanta exceção
aponta o cursor para o início, avança o número de posições solicitadas menos um e invoca o método “inserir_apos_atual”

remove_atual
Exclui elemento que está apontado pelo cursor da lista.
Se o cursor estiver apontando para o início da lista seta o início para o elemento posterior ao cursor.
Se o cursor estiver apontando para o fim da lista seta o fim para o elemento anterior ao cursor.
Após a exclusão aponta o cursor para o primeiro elemento restante da lista.
No caso da lista conter apenas um elemento seta a alista numa lista vazia.
No caso da lista estar vazia, levanta uma exceção.

remover_primeiro
remove o primeiro elemento da lista
invoca o método “ir_para_inicio”
invoca o método “remove_atual”

remover_ultimo
Remove o último elemento da lista
invoca o método “ir_para_fim”
invoca o método “remove_atual”

remover_elemento
remove um elemento a partir de uma chave
Invoca o método “buscar” pela chave
invoca o método “remove_atual”

remover_da_posicao
Remove o elemento na posição solicitada.
verifica se a posição informada é um inteiro, se não for, levanta exceção
verifica se a posição informada existe na lista, se não existir levanta exceção
invoca o método “ir_para_inicio”
invoca o método “avançar” o número de posições solicitadas menos um.
invoca o método invoca o método “remove_atual”