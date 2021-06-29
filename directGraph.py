class Vertex():
    def __init__(self,key,value) -> None:    
        self.key = key  # 儲存在Graph.vertices中
        self.value = value # key:哪些關係點進這個vertex
        self.out_neighbors = {}
        self.in_neighbors = {}


class Edge():
    def __init__(self,from_node,to_node,value) -> None:     
        self.key = (from_node,to_node)  # 儲存在Graph.edges中
        self.value = value  # 看問題決定這段關係需要甚麼樣的額外資訊

class DirectedGraph():
    def __init__(self) -> None:    
        self._vertices_list = {} # 儲存每個人的詳細資料
        self._edges_list = {}  # 儲存關係的詳細資料
        self.value = {}  # 額外Graph(例如這個圖是用來幹嘛的?)
        self.vertex_num = 0 # vertex總數
        self.edge_num = 0 # edge總數

    def is_edge_in_graph(self,fromkey,tokey):
        if type(fromkey) != int or type(tokey) != int:
            raise 'Wrong input: is_edge_in_graph() key is not int'
        try:
            self._edges_list[(fromkey,tokey)]
            return True
        except:
            return False

    def is_vertex_in_graph(self,key):
        if type(key) != int:
            raise 'Wrong input: is_vertex_in_graph() key is not int'
        try:
            self._vertices_list[key]
            return True
        except:
            return False

    def add_vertex(self,value):
        if type(value) != dict:
            raise 'Wrong input: add_vertex() value is not dictionary'
        key = self.vertex_num
        self._vertices_list[key] = Vertex(key, value) 
        self.vertex_num += 1
        return key

    def set_vertex_value(self,key,value):
        if type(value) != dict:
            raise 'Wrong input: set_vertex_value() value is not dictionary'
        if self.is_vertex_in_graph(key):
            self._vertices_list[key].value = value
        else:
            raise 'Wrong: set_vertex_value() no this vertex'
            
    def set_vertex_specific_value(self,key,specifickey, specificvalue):
        if self.is_vertex_in_graph(key):
            self._vertices_list[key].value[specifickey] = specificvalue
        else:
            raise 'Wrong: set_vertex_specific_value() no this vertex'

    def delete_vertex(self,key):
        if type(key) != int:
            raise 'Wrong input: delete_vertex() key is not int'
        if self.is_vertex_in_graph(key):
            self.edge_num -= len(self._vertices_list[key].out_neighbors.keys())+\
                len(self._vertices_list[key].in_neighbors.keys())
            self.vertex_num -= 1
            for idx in list(self._vertices_list[key].out_neighbors.keys()):
                self._vertices_list[idx].in_neighbors.pop(key,None)
                self._edges_list.pop((key,idx),None)
            for idx in list(self._vertices_list[key].in_neighbors.keys()):
                self._vertices_list[idx].out_neighbors.pop(key,None)
                self._edges_list.pop((idx,key),None)
            self._vertices_list.pop(key,None)
        else:
            raise 'Wrong: delete_vertex() no this vertex'

    def add_edge(self,fromkey,tokey,value):
        if type(value) != dict:
            raise 'Wrong input: add_edge() value is not dictionary'
        if type(fromkey) != int or type(tokey) != int:
            raise 'Wrong input: add_edge() key is not int'
        if not self.is_vertex_in_graph(fromkey) or\
            not self.is_vertex_in_graph(tokey):
            raise 'Wrong input: add_edge() no fromkey or no tokey'
        if fromkey == tokey:
            raise 'Wrong input: add_edge() fromkey == tokey is not allowed'
        if not self.is_edge_in_graph(fromkey,tokey):
            self._edges_list[(fromkey,tokey)] = Edge(fromkey,tokey,value)
            self.edge_num += 1
            self._vertices_list[fromkey].out_neighbors[tokey] = 1
            self._vertices_list[tokey].in_neighbors[fromkey] = 1
        else:
            self._edges_list[(fromkey,tokey)].value = value

    def set_edge_value(self,fromkey,tokey,value):
        if type(value) != dict:
            raise 'Wrong input: set_edge_value() value is not dictionary'
        if type(fromkey) != int or type(tokey) != int:
            raise 'Wrong input: set_edge_value() key is not int'
        if self.is_edge_in_graph(fromkey,tokey):
            self._edges_list[(fromkey,tokey)].value = value
        else:
            raise 'Wrong: set_edge_value() no this edges'

    def set_edge_specific_value(self,fromkey,tokey,specifickey,specificvalue):
        if type(fromkey) != int or type(tokey) != int:
            raise 'Wrong input: set_edge_specific_value() key is not int'
        if self.is_edge_in_graph(fromkey,tokey):
            self._edges_list[(fromkey,tokey)].value[specifickey] = specificvalue
        else:
            raise 'Wrong: set_edge_specific_value() no this edges'


    def delete_edge(self,fromkey,tokey):
        if type(fromkey) != int or type(tokey) != int:
            raise 'Wrong input: delete_edge() key is not int'
        if self.is_edge_in_graph(fromkey,tokey):
            self.edge_num -= 1
            self._edges_list.pop((fromkey,tokey),None)
            self._vertices_list[fromkey].out_neighbors.pop(tokey,None)
            self._vertices_list[tokey].in_neighbors.pop(fromkey,None)
        else:
            raise 'Wrong: delete_edge() no this edges'
    
    def get_all_vertices(self):
        return list(self._vertices_list.keys())

    def get_all_edges(self):
        return list(self._edges_list.keys())

    def get_vertex_value(self,key):
        try:
            return self._vertices_list[key].value
        except:
            raise 'Wrong: get_vertex_value() no this vertex'
    def get_vertex_out_neighbors(self,key):
        try:
            return list(self._vertices_list[key].out_neighbors.keys())
        except:
            raise 'Wrong: get_vertex_out_neighbors() no this vertex'
    def get_vertex_in_neighbors(self,key):
        try:
            return list(self._vertices_list[key].in_neighbors.keys())
        except:
            raise 'Wrong: get_vertex_in_neighbors() no this vertex'

    def get_edge_value(self,fromkey,tokey):
        try:
            return self._edges_list[(fromkey,tokey)].value
        except:
            raise 'Wrong: get_edge_value() no this edge'



def check(s,g):
    print(s)
    print('vertice:',g.get_all_vertices())
    print('edges:',g.get_all_edges())
    print('vertices_num',g.vertex_num)
    print('edges_num',g.edge_num)
def test1():
    g = DirectedGraph()
    for i in range(10):
        g.add_vertex({'name':'hello'})
    for i in range(10):
        for j in range(i+1,10):
            g.add_edge(i,j,{'distance':1})
    check('新增點和邊測試',g)
    print('0->',g.get_vertex_out_neighbors(0))
    print(g.get_vertex_in_neighbors(5),'->5')
    print()
    for i in range(10):
        g.add_vertex({'name':'hello'})
    for i in range(10):
        for j in range(i+1,10):
            g.add_edge(i,j,{'distance':2})
    check('重複新增點和邊測試',g)
    print('11->',g.get_vertex_out_neighbors(11))
    print()
    for i in [1,3,5,7,9]:
        g.delete_vertex(i)
    check('刪除點測試',g)
    g.delete_edge(6,8)
    check('刪除邊測試',g)
    print()
    g.set_vertex_specific_value(4,'test','hello')
    print(4,'->value:',g.get_vertex_value(4))
    print(2,'->value:',g.get_vertex_value(2))
    print((4,8),'->value:',g.get_edge_value(4,8))
if __name__ == '__main__':
    test1()