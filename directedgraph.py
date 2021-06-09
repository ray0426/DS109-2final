class Vertex:
    pass
class DirectedGraph:
    pass
    
class Vertex:
    def __init__(self,
                 key = 0,
                 value = 0,
                 ) -> None:

        self.key = key if type(key) == int else 0
        self.value = value
        self.inEdges = {}
        self.outEdges = {}

    def __repr__(self) -> str:
        return 'Vertex(Object): key = {}'.format(self.key)

    def setKey(self,key) -> None:
        self.key = key if type(key) == int else 0

    def setValue(self, value) -> None:
        self.value = value

    def getNumIndegree(self) -> int:
        return len(self.inEdges.keys())

    def getNumOutdegree(self) -> int:
        return len(self.outEdges.keys())

class DirectedGraph:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.number_of_edges = 0
        self.nodeMap = {}

    def __repr__(self) -> str:
        return 'Graph(Object) : num_of_nodes : {} num_of_edges(directed) : {}'.format(self.number_of_nodes, self.number_of_edges)

    def getNodeNumber(self) -> int:
        return self.number_of_nodes
    
    def getEdgeNumber(self) -> int:
        return self.number_of_edges
    
    def isNodeExisted(self, nodekey) -> bool:
        return self.nodeMap.get(nodekey) != None
    
    def isEdgeExist(self, fromNodekey, toNodekey)-> bool:
        if self.isNodeExisted(fromNodekey) and self.isNodeExisted(toNodekey):
            if self.nodeMap[fromNodekey].outEdges.get(toNodekey) != None:
                return True
        else:
            return False

    def getNodeValue(self, nodekey):
        if self.isNodeExisted(nodekey):
            return self.nodeMap[nodekey].value
    
    def getNodeInNeighbors(self, nodekey) -> list:
        """ [int,int, ... , int] """
        if self.isNodeExisted(nodekey):
            return (self.nodeMap[nodekey].inEdges.keys())
        else:
            return []

    def getNodeOutNeighbors(self, nodekey) -> list:
        """ [int,int, ... , int] """
        if self.isNodeExisted(nodekey):
            return (self.nodeMap[nodekey].outEdges.keys())
        else:
            return []
    
    def addNode(self, nodekey, nodevalue = 0) -> None:
        if not self.isNodeExisted(nodekey):
            newNode = Vertex(key = nodekey, value = nodevalue)
            self.nodeMap[nodekey] = newNode
            self.number_of_nodes += 1
        else:
            self.setNode(nodekey, nodevalue)
    
    def setNode(self, nodekey, nodevalue = 0) -> None:
        if not self.isNodeExisted(nodekey):
            self.addNode(nodekey,nodevalue)
        else:
            ptr = self.nodeMap[nodekey]
            ptr.value = nodevalue
    
    def addEdge(self, fromNodekey, toNodekey) -> None:
        if self.isEdgeExist(fromNodekey,toNodekey):
            return None
        if not self.isNodeExisted(fromNodekey):
            self.addNode(fromNodekey)
        if not self.isNodeExisted(toNodekey):
            self.addNode(toNodekey)

        self.nodeMap[fromNodekey].outEdges[toNodekey] = True
        self.nodeMap[toNodekey].inEdges[fromNodekey] = True
        self.number_of_edges += 1

    def setEdge(self, fromNodekey, toNodekey) -> None:
        if not self.isEdgeExist(fromNodekey, toNodekey):
            self.addEdge(fromNodekey, toNodekey)
    
    def getAllNodes(self):
        """get all nodes -> [int,int, ... ,int] """
        return list(self.nodeMap.keys())

            