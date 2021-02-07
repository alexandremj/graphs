from sys import maxsize
from vertex import Vertex
from typing import List

# um grafo nao-dirigido e ponderado eh definido como a tripla G(V, E, w), onde:
#   V eh o conjunto de vertices
#   E eh o conjunto de arestas
#   w eh uma funcao que define o peso das arestas
#
# como utilizamos um dicionario para representar w, uma vez que essa eh uma
# funcao discreta e varias vezes descontinua, podemos receber o E do grafo 
# simplesmente pegando as chaves do dicionario que representa w
class Graph:

    def __init__(self, vertices=list(), weight_function=dict()):
        self.vertices = vertices
        self.weight_function = weight_function


    # quantidade de vertices do grafo
    def qtdVertices(self):
        return len(self.vertices)


    # quantidade de arestas do grafo
    def qtdArestas(self):
        return len(self.weight_function.keys())


    # grau do vértice v
    # como o grafo eh nao-dirigido, podemos apenas listar as adjacencias de v
    # sabendo que, matricialmente, aij = aji
    def grau(self, v):
        return len(self.vizinhos(v))


    # rotulo do vertice v
    # retorna acesso ao ultimo item se um indice menor do que 1 for usado
    def rotulo(self, v):
        return self.vertices[v-1].label


    # vizinhos do vertice v
    # retorna acesso ao ultimo item se um indice menor do que 1 for usado
    def vizinhos(self, v):
        neighbors = set()

        for (edge_1, edge_2) in self.weight_function.keys():
            if v == edge_1:
                neighbors.add(edge_2)
            elif v == edge_2:
                neighbors.add(edge_1)
        
        return neighbors


    # retorna verdadeiro se existe uma aresta que conecta u a v; do contrario falso
    def haAresta(self, u, v):
        return ((u, v) in self.weight_function.keys()
                or (v, u) in self.weight_function.keys())


    # se existe uma aresta que conecta u e v retorna o peso dela; do contrario
    # retorna o maior inteiro representavel pelo Python na maquina
    def peso(self, u, v):
        if (u, v) in self.weight_function:
            return self.weight_function[(u, v)]
        elif (v, u) in self.weight_function:
            return self.weight_function[(v, u)]
        else:
            return maxsize


    def ler(arquivo):
        g = Graph()

        with open(arquivo) as f:
            # joga fora a primeira linha, listas encadeadas sao incriveis
            f.readline()

            # flag para verificar se terminamos leitura dos vertices
            finished_vertices = False

            for line in f.readlines():
                print(line)
                words = line.split()

                # linha *edges
                if len(words) == 1:
                    finished_vertices = True
                    continue
                elif finished_vertices:
                    edge_1, edge_2, weight = words
                    g.weight_function[int(edge_1), int(edge_2)] = float(weight)
                else:
                    g.vertices.append(Vertex(int(words[0]), words[1]))

            return g
                



