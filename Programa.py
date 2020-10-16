from Elemento import Elemento
from Lista import Lista


a = Elemento(1)
b = Elemento(2)
c = Elemento(3)
d = Elemento(4)
e = Elemento(5)
f = Elemento(6)



l = Lista(10)
l.inserir_na_frente(a)
print(l.lista())

l.inserir_na_frente(b)
print(l.lista())

l.inserir_no_final(c)
print(l.lista())


l.inserir_apos_atual(d)
print(l.lista())

l.inserir_antes_atual(e)
print(l.lista())

l.inserir_na_posicao(1,f)
print(l.lista())

print(l._contem(5))

l.remover_elemento(4)
print(l.lista())


l.remover_da_posicao(2)
print(l.lista())


l.remover_ultimo()
print(l.lista())


l.remover_primeiro()
print(l.lista())


l.remove_atual()
print(l.lista())

