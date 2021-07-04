from directGraph import DirectedGraph
from utilities1415 import *
from utilities import *
import time
import json

def find_contacted(graph, keys):
    contacts = []
    for key in keys:
        if graph._vertices_list[key].value['infected-time'] != '':
            infected_time = graph.get_vertex_value(key)['infected-time']
            for neighbors in graph._vertices_list[key].tmp_neighbors:
                result = time.strptime(infected_time, '%Y/%m/%d')
                t = int(time.mktime(result))
                idx = list(neighbors.keys())[0]
                if idx > t:
                    temp_contects = list(neighbors.values())[0]
                    contacts += temp_contects

            for i in graph.get_vertex_out_neighbors(key):
                contacts.append(i)
    contacts = list(set(contacts))
    return contacts

def show_vertex_status(graph, sidx, eidx, show_all):
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
    if show_all:
        print("print people status: ")
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
    insert_infected(graph, [0, 2], '2021/6/7')
    set_vertex_tmp_neighbors(graph, 2, '2021/6/6-17:20', [1, 3, 7])
    set_vertex_tmp_neighbors(graph, 2, '2021/6/7-18:20', [5, 4, 8])
    set_vertex_tmp_neighbors(graph, 0, '2021/6/6-18:20', [1, 3, 7])
    show_vertex_status(graph, 0, 100, false)
    #print(n)
    print(find_contacted(graph, [0]))
    print(find_contacted(graph, [2]))
