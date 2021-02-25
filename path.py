from graph import Graph, ler
from sys import exit

if __name__ == '__main__':
    file_name = input('Nome do arquivo: ')

    g = ler(file_name)

    vertex_index = int(input('Indice do vertice: '))

    negative_cycle_check, Dv, Av = g.bellman_ford(vertex_index)

    if not negative_cycle_check:
        print('Ciclo de peso negativo encontrado! Saindo...')
        exit()

    for i in range(g.qtdVertices()):
        # recupera o caminho da origem ate i comecando por i

        current = g.vertices[i]
        path = [current.label]

        # None apenas na origem
        while Av[current.number-1]:
            previous = Av[current.number-1]
            path.insert(0, previous.label)
            current = previous
        
        print(f'{i+1}: {", ".join(path)}; d={Dv[i]}')
