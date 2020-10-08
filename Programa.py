import Elemento
import Lista


a = Elemento(4)
b = Elemento(2)
c = Elemento(3)
d = Elemento(1)
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
