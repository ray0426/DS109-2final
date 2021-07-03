from directGraph import DirectedGraph

def add_people(graph, people):
    key = [None] * len(people)
    for i in range(0, len(people)):
        key[i] = graph.add_vertex(people[i])
    return key

def remove_people(graph, key):
    for i in range(0, len(key)):
        graph.delete_vertex(key[i])
    return

# key is an array of keys of vertex, value is a dictionary
def add_relation(graph, key, value):
    for i in range(0, len(key) - 1):
        for j in range(i + 1, len(key)):
            graph.add_edge(key[i], key[j], value)
            graph.add_edge(key[j], key[i], value)
    return

# key is an array of keys of vertices
def remove_relation(graph, key):
    for i in range(0, len(key) - 1):
        for j in range(i + 1, len(key)):
            graph.delete_edge(key[i], key[j])
            graph.delete_edge(key[j], key[i])
    return

def insert_infected(graph, key, time):
    for i in range(0, len(key)):
        graph.set_vertex_specific_value(key[i], 'infected-time', time)
    return

def new_relative(graph, time):
    relative = []
    for idx,x in graph._vertices_list.items():
        value = graph.get_vertex_value(idx)
        if (value['infected-time'] == time):
            relative += graph.get_vertex_out_neighbors(idx)
    relative = list(set(relative))
    return relative    #回傳新一波被感染的人

def show_infected(graph, specifickey):
    infected = []
    for idx,x in graph._vertices_list.items():
        value = graph.get_vertex_value(idx)
        if (value['infected-time'] != ''):      # --> 我把time不是0的都當作是感染者
            infected += [idx]
            if (specifickey != None):
                print(value[specifickey], end = ' ')
    if (specifickey != None):
        print('\n', end = '')
    return infected

def isolation(graph, isolated, free, time):
    for i in range(0, len(isolated)):
        graph.set_vertex_specific_value(isolated[i], 'isolated-start', time)
    for i in range(0, len(free)):
        graph.set_vertex_specific_value(free[i], 'isolated-end', time)


if __name__ == '__main__':
    graph = DirectedGraph()
    n = add_people(graph, [{'name': 'ray', 'abc': '123', 'infected-time': '', 'isolated-start' : '',
    'isolated-end' : ''},{'name': 'aaa', 'abc': '456', 'infected-time': '', 'isolated-start' : '',
    'isolated-end' : ''},{'name': 'bbb', 'abc': '789', 'infected-time': '', 'isolated-start' : '',
    'isolated-end' : ''}])
    add_relation(graph, [0,1,2], {'distance':1})
    print(n)
    q = add_people(graph, [{'name': 'bbb', 'abc': '789', 'infected-time': '', 'isolated-start' : '',
    'isolated-end' : ''}, {'name': 'bbb', 'abc': '789', 'infected-time': '', 'isolated-start' : '',
    'isolated-end' : ''}])
    print(q)
    insert_infected(graph, [2,4], '2021/6/5')
    add_relation(graph, [1,3,4],{'distance':1})
    s = new_relative(graph, '2021/06/06')
    print(s)
    p = show_infected(graph, 'infected-time')
    print(p)
    isolation(graph, [2,4], [], '2021/06/07')
    isolation(graph, [], [2,4], '2021/06/08')
    graph.delete_vertex(2)
    for idx,x in graph._vertices_list.items():
        value = graph.get_vertex_value(idx)
        print(value)
