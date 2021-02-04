from sys import maxsize

# um grafo nao-dirigido e ponderado eh definido como a tripla G(V, E, w), onde:
#   V eh o conjunto de vertices
#   E eh o conjunto de arestas
#   w eh uma funcao que define o peso das arestas
#
# como utilizamos um dicionario para representar w, uma vez que essa eh uma
# funcao discreta e varias vezes descontinua, podemos receber o E do grafo 
# simplesmente pegando as chaves do dicionario que representa w
def __init__(self, vertices, edges, weight_function={(x,y):1 for (x, y) in edges}):
    self.vertices = vertices
    self.weight_function = weight_function

# quantidade de vertices do grafo
def qtdVertices(self):
    return len(self.vertices)

# quantidade de arestas do grafo
def qtdArestas(self):
    return len(self.weight_function.keys())

# grau do vértice v
def grau(self, v):
    pass

# rotulo do vertice v
def rotulo(self, v):
    pass

# vizinhos do vertice v
def vizinhos(self, v):
    pass

# retorna verdadeiro se existe uma aresta que conecta u a v; do contrario falso
def haAresta(self, u, v):
    pass

# se existe uma aresta que conecta u e v retorna o peso dela; do contrario
# retorna o maior inteiro r
def peso(self, u, v):
    pass

def ler(self, arquivo):
    pass


# funcao auxiliar nao especificada no escopo da atividade. Transforma o grafo
# em uma matriz de adjacencias para facilitar usos em que essa representacao
# eh a mais adequada
def to_matrix(self):
    matrix = [0 for i in range(self.qtdArestas())]
            [0 for i in range(self.qtdArestas())]

    for edge in edges:
        pass # precisa de mais informacoes sobre a relacao entre os indices da
             # matriz e os rotulos
        # como o grafo eh nao direcionado, aij = aji = peso da aresta
        # verificar como serao incluidos os valores nos dicionarios


