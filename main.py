from grafo import Nodo, Arista, AristaDirigida, AristaNoDirigida
from grafo import Grafo

n1 = Nodo('A')
n2 = Nodo('B')
n3 = Nodo('C')

# print(n1, n2, n3)

# arista01 = Arista(n1, n2, 10)
# print(arista01)

arista_01 = AristaNoDirigida(n1, n2, 1)
arista_02 = AristaNoDirigida(n2, n3, 15)

g = Grafo()
g.agregar_arista(arista_01)
g.agregar_arista(arista_02)
print(g.get_lista_adyacencia())
g.print_lista_adyacencia()
s = g.grafo_to_str()
print(s)