from graph import Graph, ler

if __name__ == '__main__':
    file_name = input('Nome do arquivo: ')

    g = ler(file_name)

    vertex_index = int(input('Indice do vertice: '))

    print(g.bellman_ford(vertex_index))