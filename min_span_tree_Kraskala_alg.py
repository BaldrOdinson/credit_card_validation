def find_cycle_in_graph(min_span_tree):
    base_graph = []
    base_graph_nodes = []
    path_list = []
    # create list of graph edges
    for span in min_span_tree.keys():
        base_graph.append(span)
    # create list of nodes
    for (a, b) in base_graph:
        base_graph_nodes.append(a)
        base_graph_nodes.append(b)
    #print(f'___BEGIN___\nbase_graph: {base_graph}\nbase_graph_nodes: {base_graph_nodes}\n\
#set(base_graph_nodes): {set(base_graph_nodes)}')
    # delete hanging nodes
    for node in set(base_graph_nodes):
        if base_graph == []:
            break
        if base_graph_nodes.count(node) == 1:
            for (a, b) in base_graph:
                if a == node or b == node:
                    span_4_del = (a, b)
                    #print(f'__HANGING NODE__\nspan_4_del: {span_4_del}')
            #print(f'__BEFORE DELETE HANGING NODE__\nbase_graph: {base_graph}\nspan_4_del: {span_4_del}')
            base_graph.remove(span_4_del)
            base_graph_nodes.remove(span_4_del[0])
            base_graph_nodes.remove(span_4_del[1])
    # create path list
    while True:
        if len(base_graph) == 0:
            if len(path_list) == 0:
                result = 'non cycled graph'
            elif path_list.count(from_) > 1 or path_list.count(to_) > 1:
                result = 'cycled graph'
            else:
                result = 'non cycled graph'
            break
        (from_, to_) = base_graph[0]
        #print(f'__IN WHILE__\n(from_, to_): {from_, to_}')
        if len(path_list) == 0:
            path_list.append(from_)
            path_list.append(to_)
            base_graph.remove((from_, to_))
            continue
        if from_ == path_list[-1]:
            path_list.append(to_)
            base_graph.remove((from_, to_))
        elif to_ == path_list[-1]:
            path_list.append(from_)
            base_graph.remove((from_, to_))
        elif from_ == path_list[0]:
            path_list.insert(0, to_)
            base_graph.remove((from_, to_))
        elif to_ == path_list[0]:
            path_list.insert(0, from_)
            base_graph.remove((from_, to_))
        else:
            remove = base_graph[0]
            base_graph.remove((from_, to_))
            base_graph.insert(len(base_graph), remove)
        if path_list.count(from_) > 1 or path_list.count(to_) > 1:
            result = 'cycled graph'
            break
        #print(f'__PATH LIST__\npath_list: {path_list}\nbase_graph: {base_graph}')
        
    #print(f'___FINAL___\nbase_graph: {base_graph}\nbase_graph_nodes: {base_graph_nodes}\n\
#set base_graph_nodes: {set(base_graph_nodes)}\nresult: {result}')
    return result
    
def find_min_weight(edges_weight, min_weight = -1):
    for spin, weight in edges_weight.items():
        if min_weight == -1:
            min_weight = weight
        else:
            min_weight = min(min_weight, weight)
    return min_weight

def find_max_weight(edges_weight, max_weight = -1):
    for spin, weight in edges_weight.items():
        if max_weight == -1:
            max_weight = weight
        else:
            max_weight = max(max_weight, weight)
    return max_weight

def del_double(edges_weight):
    '''
    Удаляем дубликаты
    '''
    for spin, weight in edges_weight.items():
        for comp_spin, comp_weight in edges_weight.items():
            if spin[0] == comp_spin[1] and spin[1] == comp_spin[0] and edges_weight[spin] != 'double':
                edges_weight[comp_spin] = 'double'
    temp_edges_weight = {}
    for spin, weight in edges_weight.items():
        if weight != 'double':
            temp_edges_weight[spin] = weight
    edges_weight = temp_edges_weight
    return edges_weight

def spin_weight_dict(graph):
    '''
    формируем словарь edges_weight с ребрами и весом
    '''
    edges_weight = {}
    for nodes in graph.items():
        for spin in nodes[1]:
            edges_weight[(nodes[0], spin[0])] = spin[1]
    return edges_weight

def min_span_tree_Kraskala(graph):
    # формируем словарь с ребрами и весом
    min_span_tree = {}
    preorder_spins = {}
    edges_weight = spin_weight_dict(graph)
    # Удаляем дубликаты
    edges_weight = del_double(edges_weight)
    #print(f'edges_weight: {edges_weight}')
    # Ищем ребра минимального веса, ну и максимального
    max_weight = find_max_weight(edges_weight)
    min_weight = find_min_weight(edges_weight, min_weight = -1)
    while min_weight <= max_weight:
        # Отбираем ребра минимального веса
        for spin, weight in edges_weight.items():
            if weight == min_weight:
                preorder_spins[spin] = min_weight
        for spin, weight in preorder_spins.items():
            min_span_tree[spin] = weight
            # Если цикл замкнулся удаляем из дерева последнее ребро
            curr_min_span_tree = {}
            for key in min_span_tree:
                curr_min_span_tree = {}
                curr_min_span_tree[key] = min_span_tree[key]
                for key_in, weight in min_span_tree.items():
                    if min_span_tree[key_in] != min_span_tree[key]:
                        curr_min_span_tree[key_in] = min_span_tree[key_in]
            #print(f'__IN KRASKALA WHILE__\ncurr_min_span_tree: {curr_min_span_tree}')
            check_result = find_cycle_in_graph(curr_min_span_tree)
            if check_result == 'cycled graph':
                min_span_tree.pop(spin)
        # Выбираем следующий минимальный вес
        min_weight += 1
    #print(f'___BOTTOM___\nedges_weight: {edges_weight}\nmin weight: {min_weight}, max weight: {max_weight}\npreorder_spins: {preorder_spins}\n\
#min_span_tree: {min_span_tree}\n{min_span_tree.keys()}\ncheck result: {check_result}')
    return min_span_tree
    
if __name__ == '__main__':
    graph = {1: [(7, 9), (3, 3), (2, 6)], 2: [(1, 6), (3, 4), (4, 2), (5, 9)],\
3: [(1, 3), (7, 9), (8, 9), (4, 2), (2, 4)], 4: [(3, 2), (2, 2), (5, 9), (8, 8)],\
5: [(2, 9), (4, 9), (8, 7), (9, 5), (6, 4)], 6: [(5, 4), (9, 1), (10, 4)],\
7: [(1, 9), (3, 9), (8, 8), (10, 18)], 8: [(3, 9), (7, 8), (4, 8), (5, 7), (9, 9), (10, 10)],\
9: [(8, 9), (5, 5), (6, 1), (10, 3)], 10: [(7, 18), (8, 10), (9, 3), (6, 4)]}
    print(f'Min spanning tree for the given graph:\n{min_span_tree_Kraskala(graph)}')
