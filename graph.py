from sys import maxsize
from vertex import Vertex
from typing import List
from collections import OrderedDict

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
        vertex = self.vertices[v-1]

        neighbors = set()

        for (edge_1, edge_2) in self.weight_function.keys():
            if vertex == edge_1:
                neighbors.add(edge_2)
            elif vertex == edge_2:
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


    # algoritmo para resolucao da questao 2
    def breadth_first_search(self, vertex_index):
        vertex = self.vertices[vertex_index-1]

        Cv = [False for x in range(self.qtdVertices())]
        Dv = [maxsize for x in range(self.qtdVertices())]
        Av = [None for x in range(self.qtdVertices())]

        Cv[vertex.number-1] = True
        Dv[vertex.number-1] = 0

        queue = list()
        queue.append(vertex)

        while len(queue):
            current = queue.pop(0)

            for neighbor in self.vizinhos(current.number):
                if not Cv[neighbor.number-1]:
                    Cv[neighbor.number-1] = True
                    Dv[neighbor.number-1] = Dv[current.number-1] + 1
                    Av[neighbor.number-1] = current
                    queue.append(neighbor)

        return Dv


    # funcao auxiliar para implementar a verificacao da linha 4 do algoritmo
    # buscarSubcicloEuleriano, verifica se ainda existem arestas candidatas
    # para continuar o ciclo e retorna a primeira encontrada, do contrario
    # retorna None
    def check_valid_edges(self, v, Ce):
        for u in self.vizinhos(v):
                if not Ce[(u, v)]:
                    return (u, v)
        return None


    # funcao recursiva auxiliar do algoritmo de Hierholzer
    def search_eulerian_subcycle(self, v, Ce):
        cycle = [v]
        t = v

        while v == t:
            edge = self.check_valid_edges(v, Ce)
            if not edge:
                return (False, None)
            
            Ce[edge] = True
            v = edge[0]
            cycle.append(v)
        
        # IMPLEMENTAR linhas 12 a 17



    # algoritmo para busca de ciclos eulerianos em um grafo
    def hierholzer(self):
        # utilizaremos um dicionário ordenado para que possamos indexar
        Ce = OrderedDict()

        for edge in self.weight_function.keys():
            Ce[edge] = False
        
        v = self.vertices[0]

        # Python passa implicitamente o objeto self que chamou a funcao,
        # que no algoritmo seria o grafo G de entrada
        (r, cycle) = self.search_eulerian_subcycle(v, Ce)

        if not r:
            return (False, None)
        else:
            if False in Ce.values():
                return (False, None)
            else:
                return (True, cycle)

    
    # algoritmo de Bellman-Ford para encontrar caminhos mínimos do vértice de
    # origem a cada outro vértice no grafo
    def bellman_ford(self, origin_index: int):
        origin = self.vertices[origin_index-1]

        Dv = [maxsize for x in range(self.qtdVertices())]
        Av = [None for x in range(self.qtdVertices())]

        Dv[origin.number-1] = 0

        for i in range(self.qtdVertices() - 1):
            for (u, v) in self.weight_function.keys():
                if Dv[v.number-1] > (Dv[u.number-1] + self.weight_function[(u,v)]):
                    Dv[v.number-1] = Dv[u.number-1] + self.weight_function[(u,v)]
                    Av[v.number-1] = u
        
        for (u, v) in self.weight_function.keys():
            if Dv[v.number-1] > (Dv[u.number-1] + self.weight_function[(u, v)]):
                return (False, None, None)
        
        return (True, Dv, Av)
    
    



def ler(arquivo):
    g = Graph()
    # por algum motivo isso aqui ja ta chegando com o setup todo wtf


    with open(arquivo) as f:
        # joga fora a primeira linha, listas encadeadas sao incriveis
        f.readline()

        # flag para verificar se terminamos leitura dos vertices
        finished_vertices = False

        for line in f.readlines():
            words = line.split()

            # linha *edges
            if len(words) == 1:
                
                finished_vertices = True
                continue
            elif finished_vertices:
                edge_1, edge_2, weight = words
                g.weight_function[g.vertices[int(edge_1)-1], g.vertices[int(edge_2)-1]] = float(weight)
            else:                    
                g.vertices.append(Vertex(int(words[0]), words[1]))

    return g
                