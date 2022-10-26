from pprint import pprint, pformat
from dataclasses import dataclass
from typing import Any, List


@dataclass(unsafe_hash=True)
class Vertice:
    dato: Any
    # def __init__(self, dato) -> None:
    #     self.dato = dato
    #
    # def __eq__(self, other):
    #     return self.dato == other.dato
    #
    # def __str__(self):
    #     return f"dato: {self.dato}"
    #
    # def __repr__(self) -> str:
    #     return f"Vertice({self.dato})"
    #
    # def __hash__(self):
    #     return hash(self.dato)

@dataclass(unsafe_hash=True)
class AristaNoDirigida:
    origen: Vertice
    destino: Vertice
    ponderacion: Any
    # def __init__(self, origen: Vertice, destino: Vertice, ponderacion) -> None:
    #     self.origen = origen
    #     self.destino = destino
    #     self.ponderacion = ponderacion
    #
    # def __str__(self):
    #     return f"({self.origen} ---- {self.ponderacion} ---- ({self.destino}))"
    #
    # def __eq__(self, other):
    #     return self.origen == other.origen and \
    #     self.destino == other.destino

    # def __repr__(self) -> str:
    #     return f"{repr(self.origen)} ---- {self.ponderacion} ---- {repr(self.destino)}"

# class AristaNoDirigida(Arista):
#     def dirigido(self):
#         return False
#
# class AristaDirigida(Arista):
#     def dirigido(self):
#         return True

    # def __str__(self):
    #     return f"({self.origen} ---- {self.ponderacion} ---> ({self.destino}))"

@dataclass()
class Adyacente:
    vertice: Vertice
    ponderacion: Any
class GrafoNoDirigido:
    def __init__(self) -> None:
        self.aristas: List[AristaNoDirigida] = []
        self.ady = {}

    def agregar_arista(self, arista: AristaNoDirigida):
        if arista in self.aristas:
            print(f'La arista {arista} no se agregó porque ya fue agregada ')
        self.aristas.append(arista)

    def eliminar_arista(self, arista: AristaNoDirigida):
        self.aristas.remove(arista)

    def __repr__(self):
        return pformat([arista for arista in self.aristas])

    def get_lista_adyacencia(self):
        self.ady.clear()

        grafo_no_dirigido = {
            "Vertice origen": [ ["Vertice destino", 'ponderacion'] ],
            "Vertice destino": [ ["Vertice origen", 'ponderacion'] ]
        }

        grafo_dirigido = {
            "Vertice origen": [ ["Vertice destino", 'ponderacion'], ["Vertice destino", 'ponderacion']]
        }

        for arista in self.aristas:
            vertice_origen = arista.origen
            vertice_destino = arista.destino
            ponderacion = arista.ponderacion

            self.agregar_dict(vertice_origen, vertice_destino, ponderacion)
            self.agregar_dict(vertice_destino, vertice_origen, ponderacion)

        return self.ady

    def agregar_dict(self, vertice_origen: Vertice, vertice_destino: Vertice, ponderacion):
        if vertice_origen not in self.ady:
            self.ady[vertice_origen] = [Adyacente(vertice=vertice_destino, ponderacion=ponderacion)]
        else:
            self.ady[vertice_origen].append(Adyacente(vertice=vertice_destino, ponderacion=ponderacion))

    def print_lista_adyacencia(self):
        self.ady.clear()
        self.get_lista_adyacencia()
        pprint(self.ady)

    def grafo_to_str(self):
        self.ady.clear()
        self.get_lista_adyacencia()
        s = pformat(self.ady)
        return s

    