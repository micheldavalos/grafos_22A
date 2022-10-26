from grafo import Vertice, AristaNoDirigida
from grafo import GrafoNoDirigido
from particula import Punto
from pprint import pprint

n1 = Vertice(dato=Punto(x=10, y=10))
n2 = Vertice(dato=Punto(x=20, y=20))
n3 = Vertice(dato=Punto(x=30, y=30))
n4 = Vertice(dato=Punto(x=40, y=40))

# print(n1, n2, n3)

# arista01 = Arista(n1, n2, 10)
# print(arista01)

arista_01 = AristaNoDirigida(n1, n2, 1)
arista_02 = AristaNoDirigida(n2, n3, 15)
arista_03 = AristaNoDirigida(n3, n4, 30)

g = GrafoNoDirigido()
g.agregar_arista(arista_01)
g.agregar_arista(arista_02)
g.agregar_arista(arista_03)
pprint(g)
print(g.get_lista_adyacencia())
g.print_lista_adyacencia()
s = g.grafo_to_str()
print(s)