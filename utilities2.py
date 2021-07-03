from directGraph import DirectedGraph
from utilities import *
import json

def find_contacted(graph, keys):
    contacts = []
    for key in keys:
#        infected_time = graph.get_vertex_value(key)['infected-time']
        for i in graph.get_vertex_out_neighbors(key):
            contacts.append(i)
    contacts = list(set(contacts))
    return contacts

def show_vertex_status(graph, sidx, eidx):
    print("=============================")
    print("graph status:")
    print("-----------------------------")
    print("total people: " + str(graph.vertex_num))
    print("total edge: " + str(int(graph.edge_num / 2)))
    NumInfected = 0
    for idx, vertex in graph._vertices_list.items():
        if vertex.value['infected-time'] != "":
            NumInfected += 1
    print("total infected: " + str(NumInfected))
    NumIsolated = 0
    for idx, vertex in graph._vertices_list.items():
        if vertex.value['isolated-start'] != "" and\
        vertex.value['isolated-end'] == "":
            NumIsolated += 1
    print("total isolation: " + str(NumIsolated))
    print("print people status:")
    fields = ['id', 'age', 'birth', 'infected-time']
    for idx, vertex in graph._vertices_list.items():
        print("name: " + str(vertex.value['name']), end='')
        for key in fields:
            print(", " + str(key) + ": " + str(vertex.value[key]), end='')
        print()


if __name__ == '__main__':
    graph = DirectedGraph()
    with open('data.json', 'r') as obj:
        data = json.load(obj)
    #print(data)

    n = add_people(graph, data)
    add_relation(graph, [0,1,2], {'distance':0})
    add_relation(graph, [5,6,7], {'distance':0})
    #print(n)
    #print(find_contacted(graph, [0, 3, 7]))
    show_vertex_status(graph, 0, 100)
