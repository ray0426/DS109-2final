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
        graph.set_vertex_specific_value(key[i], 'infected', time)
    return

def new_relative(graph, time):
    relative = []
    for i in range(0, graph.vertex_num):
        value = graph.get_vertex_value(i)
        if (value['infected'] == time):
            relative += graph.get_vertex_out_neighbors(i)
    relative = list(set(relative))
    return relative    #回傳新一波被感染的人

def show_infected(graph, specifickey):
    infected = []
    for i in range(0, graph.vertex_num):
        value = graph.get_vertex_value(i)
        if (value['infected'] != 0):      # --> 我把time不是0的都當作是感染者
            infected += [i]
            if (specifickey != None):
                print(value[specifickey], end = ' ')
    if (specifickey != None):
        print('\n', end = '')
    return infected

if __name__ == '__main__':
    graph = DirectedGraph()
    n = add_people(graph, [{'name': 'ray', 'abc': '123', 'infected': 0},{'name': 'aaa', 'abc': '456', 'infected': 0},{'name': 'bbb', 'abc': '789', 'infected': 0}])
    add_relation(graph, [0,1,2], {'distance':1})
    print(n)
    q = add_people(graph, [{'name': 'bbb', 'abc': '789', 'infected': 0}, {'name': 'bbb', 'abc': '789', 'infected': 0}])
    print(q)
    insert_infected(graph, [2,4], 1)
    add_relation(graph, [1,3,4],{'distance':1})
    s = new_relative(graph, 1)
    print(s)
    p = show_infected(graph, None)
    print(p)
