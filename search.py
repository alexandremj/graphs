from graph import Graph, ler

if __name__ == '__main__':
    file_name = input('Nome do arquivo: ')

    g = ler(file_name)

    vertex_index = int(input('Indice do vertice: '))

    levels = g.breadth_first_search(vertex_index)

    d = dict()

    for i in range(len(levels)):
        if not levels[i] in d.keys():
            d[levels[i]] = str(i+1) + ' '
        else:
            d[levels[i]] += str(i+1) + ' '
    
    for key in sorted(d.keys()):
        print(f'{key}: {d[key]}')