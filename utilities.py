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

if __name__ == '__main__':
    graph = DirectedGraph()
    n = add_people(graph, [{'name': 'ray', 'abc': '123'},{'name': 'aaa', 'abc': '456'}])
    print(n)
    remove_people(graph, [0])
