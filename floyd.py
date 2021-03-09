from graph import Graph, ler

if __name__ == '__main__':
    file_name = input('Nome do arquivo: ')

    g = ler(file_name)

    distances = g.floyd_warshall()

    print(distances)

    for i in range(g.qtdVertices()):
        
        print(f'{i+1}: {",".join([str(int(x)) for x in distances[i]])}')
