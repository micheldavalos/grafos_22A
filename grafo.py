from pprint import pprint, pformat

class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato

    def __eq__(self, other):
        return self.dato == other.dato

    def __str__(self):
        return f"dato: {self.dato}"

    def __repr__(self) -> str:
        return f"Nodo({self.dato})"

    def __hash__(self):
        return hash(self.dato)


class Arista:
    def __init__(self, origen: Nodo, destino: Nodo, ponderacion) -> None:
        self.origen = origen
        self.destino = destino
        self.ponderacion = ponderacion

    def __str__(self):
        return f"({self.origen} ---- {self.ponderacion} ---- ({self.destino}))"

    def __eq__(self, other):
        return self.origen == other.origen and \
        self.destino == other.destino

    def __repr__(self) -> str:
        return f"{repr(self.origen)} ---- {self.ponderacion} ---- {repr(self.destino)}"

class AristaNoDirigida(Arista):
    def dirigido(self):
        return False

class AristaDirigida(Arista):
    def dirigido(self):
        return True

    def __str__(self):
        return f"({self.origen} ---- {self.ponderacion} ---> ({self.destino}))"

class Grafo:
    def __init__(self) -> None:
        self.aristas = []
        self.ady = {}

    def agregar_arista(self, arista: Arista):
        if arista not in self.aristas:
            self.aristas.append(arista)

    def eliminar_arista(self, arista: Arista):
        self.aristas.remove(arista)

    def __str__(self):
        return str([arista for arista in self.aristas])

    def get_lista_adyacencia(self):
        self.ady.clear()

        grafo_no_dirigido = {
            "Nodo origen": [ ["Nodo destino", 'ponderacion'] ],
            "Nodo destino": [ ["Nodo origen", 'ponderacion'] ]
        }

        grafo_dirigido = {
            "Nodo origen": [ ["Nodo destino", 'ponderacion'], ["Nodo destino", 'ponderacion']]
        }

        for arista in self.aristas:
            nodo_origen = arista.origen
            nodo_destino = arista.destino
            ponderacion = arista.ponderacion

            if arista.dirigido():
                self.agregar_dict(nodo_origen, nodo_destino, ponderacion)
            elif not arista.dirigido():
                self.agregar_dict(nodo_origen, nodo_destino, ponderacion)
                self.agregar_dict(nodo_destino, nodo_origen, ponderacion)

        return self.ady

    def agregar_dict(self, nodo_origen, nodo_destino, ponderacion):
        if nodo_origen not in self.ady:
            self.ady[nodo_origen] = [ [nodo_destino, ponderacion] ]
        else:
            self.ady[nodo_origen].append([nodo_destino, ponderacion])

    def print_lista_adyacencia(self):
        self.ady.clear()
        self.get_lista_adyacencia()
        pprint(self.ady)

    def grafo_to_str(self):
        self.ady.clear()
        self.get_lista_adyacencia()
        s = pformat(self.ady)
        return s

    