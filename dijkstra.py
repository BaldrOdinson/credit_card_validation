def dijksta_left_conn_node(graph, start_node, left_node_list = []):
    '''
    Build list of available transitions: left_node_list
    Using recursion
    '''
    #print(f'BEFORE\nleft_node_list: {left_node_list}')
    if graph[start_node] == []:
        return left_node_list
    for next_node in graph[start_node]:
        if next_node[0] not in left_node_list:
            left_node_list.append(next_node[0])
            #print(next_node)
            start_node = next_node[0]
            dijksta_left_conn_node(graph, start_node, left_node_list)
    return left_node_list

def dijkstra_compare(curr_spin, color_dict, node_weight_dict, curr_node):
    '''
    Compare currenc weight of the next node and new weight 
    consisted of weight of the current node and weight of the spin to the next node
    Finnaly we choose min one
    '''
    next_node = curr_spin[0]
    if color_dict[next_node] == 'black':
        pass
    else:
        if next_node in node_weight_dict and color_dict[next_node] != 'black':
            node_weight_dict[next_node] = min((node_weight_dict[curr_node] + curr_spin[1]), node_weight_dict[next_node])
            if color_dict[next_node] == 'white':
                color_dict[next_node] = 'grey'
        else:
            node_weight_dict[next_node] = node_weight_dict[curr_node] + curr_spin[1]
            if color_dict[next_node] == 'white':
                color_dict[next_node] = 'grey'

def dijkstra_step(graph, curr_node, color_dict, node_weight_dict, next_node_queue, left_node_list):
    '''
    Choose every transition for the current node
    '''
    #print(f'!!!_STEP_!!!\nnext_node_queue: {next_node_queue}\nnode_weight_dict: {node_weight_dict}')
    if len(next_node_queue) > 1:
        curr_spin = next_node_queue.pop(0)
        dijkstra_compare(curr_spin, color_dict, node_weight_dict, curr_node)
        dijkstra_step(graph, curr_node, color_dict, node_weight_dict, next_node_queue, left_node_list)
    else:
        curr_spin = next_node_queue.pop(0)
        dijkstra_compare(curr_spin, color_dict, node_weight_dict, curr_node)
        color_dict[curr_node] = 'black'
        if curr_node in left_node_list:
            left_node_list.remove(curr_node)
            
def dijkstra(graph, start_node):
    '''
    Computation weights of the attainable nodes from the start node
    '''
    color_dict = {} # white - new node, grey - visited node, black - processed node
    next_node_queue = []
    node_weight_dict = {}
    #left_node_list = []
    node_weight_dict[start_node] = 0
    curr_node = start_node
    left_node_list = dijksta_left_conn_node(graph, start_node, left_node_list = [])
    for node in left_node_list:
        color_dict[node] = 'white'
    while True:
        #print(f'!!!!_WHILE_1_!!!!\ncurr_node: {curr_node}\ngraph[curr_node]: {graph[curr_node]}')
        if graph[curr_node] != []:
            for node_spin in graph[curr_node]:
                next_node_queue.append(node_spin)
                #print(f'!!!_1_!!!\ncurr_node: {curr_node}\nnode_weight_dict: {node_weight_dict}\n\
#node spin: {node_spin}\ncolor_dict: {color_dict},\n\
#next_node_queue: {next_node_queue}\nleft_node_list: {left_node_list}')
                dijkstra_step(graph, curr_node, color_dict, node_weight_dict, next_node_queue, left_node_list)
        next_select = False
        shift = 1
        while next_select == False:
            if len(left_node_list) > 0:
                curr_node = left_node_list[0]
                while curr_node not in node_weight_dict:
                    try:
                        curr_node = left_node_list[0 + shift]
                        shift += 1
                    except IndexError:
                        break
                if graph[curr_node] == []:
                    left_node_list.pop(left_node_list.index(curr_node))
                    color_dict[curr_node] == 'black'
                if color_dict[curr_node] == 'black':
                    left_node_list.pop(left_node_list.index(curr_node))
                else:
                    next_select = True
            else:
                break
        if left_node_list == []:
            return node_weight_dict
        
if __name__ == '__main__':
    graph = {1:[(2, 10)], 2:[(1, 10), (3, 10), (4, 10), (5, 10), (6, 10)], 3:[(2, 10), (7, 10), (8, 10),], 4:[], 5:[(2, 10), (9, 10), (10, 10), (11, 10)], 6:[], 7:[], 8:[(3, 10)], 9:[], 10:[(5, 10)], 11:[]}
    start_point = 1
    print(f'Available path from node {start_point}\n(node:weight): {dijkstra(graph, start_point)}')
