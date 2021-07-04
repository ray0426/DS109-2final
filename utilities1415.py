from directGraph import DirectedGraph
from utilities import add_people, show_infected,insert_infected,add_relation,set_infectable
import time
def set_vertex_tmp_neighbors(graph,key,time_string,neighbors):
    result = time.strptime(time_string,'%Y/%m/%d-%H:%M') 
    t = int(time.mktime(result))
    if not graph.is_vertex_in_graph(key):
        raise 'Wrong: in set_vertex_tmp_neighbors() no this key'
    graph._vertices_list[key].tmp_neighbors.append({t:neighbors})

def add_tmp_relation(graph, keys, time):
    for i in range(0, len(keys)):
        set_vertex_tmp_neighbors(graph, keys[i], time, keys[:i] + keys[i + 1:])

def get_tracked_n_people(graph,n):
    whoCov19 = show_infected(graph)
    ans = {}
    soft_const = 1
    hard_const = 2
    outdated = graph.outdated
    for x in whoCov19:
        # 硬關係
        if not graph.is_vertex_in_graph(x):
            raise 'Wrong: in show_infected() no this infected man'
        for y in graph.get_vertex_out_neighbors(x):
            try:
                ans[y] -= hard_const 
            except:
                ans[y] = -hard_const
        # 軟關係
        for  data in graph._vertices_list[x].tmp_neighbors:
            idx = list(data.keys())[0]
            y = list(data.values())[0]
            if idx >= outdated:
                for z in y:
                    try:
                        ans[z] -= soft_const 
                    except:
                        ans[z] = -soft_const

    lst = [[ans[x],x] for x in ans]
    lst.sort()
    n = min(n,len(lst))
    ans = list(zip(*lst))[1]
    return ans[:n]
            
def test1():
    g = DirectedGraph()
    vertex = []
    for i in range(10):
        v = add_people(g,[{'name': 'name{}'.format(i), 'infected-time': '', 'isolated-start' : '',\
            'isolated-end' : '', 'infectable' : ''}])
        vertex += v
    #print(vertex)
    add_relation(g, [0,1,2], {'distance':1})
    add_relation(g, [3,4], {'distance':1})
    add_relation(g, [7,8,9], {'distance':1})
    insert_infected(g, [2,4], '2021/6/5')
    set_infectable(g, [2,4], ['2021/6/4', '2021/6/4'])
    #set_vertex_tmp_neighbors(g,2,'2021/6/6-17:20',[1,3,6])
    #set_vertex_tmp_neighbors(g,4,'2021/6/7-21:03',[6,8,9])
    add_tmp_relation(g, vertex, '2021/6/4-21:03')
    for idx,x in g._vertices_list.items():
        print(g._vertices_list[idx].tmp_neighbors)
    ans = get_tracked_n_people(g,6)
    print(ans)

if __name__ == '__main__':
    test1()
