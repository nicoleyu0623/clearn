class Node(object):
    def __init__(self, value):
        self._value = value
        self._edges = []
        self._visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self._value = value
        self._node_from = node_from
        self._node_to = node_to



class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self._nodes = nodes or []
        self._edges = edges or []
        self._node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self._node_names = list(names)


    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self._nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node


    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self._nodes:                        #fill nodes from self._nodes
            if node._value in nodes:
                nodes[node._value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:              #ensure to insert brand new node
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from._edges.append(new_edge)
        node_to._edges.append(new_edge)
        self._edges.append(new_edge)


    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(e._value, e._node_from._value, e._node_to._value)
                for e in self._edges]

    def get_edge_list_names(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge._value,
                 self._node_names[edge._node_from._value],
                 self._node_names[edge._node_to._value])
                for edge in self._edges]


    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self._edges:
            from_value, to_value = edg._node_from._value, edg._node_to._value
            adjacency_list[from_value].append((to_value, edg._value))
        return [a or None for a in adjacency_list] # replace []'s with None


    def get_adjacency_list_names_orig(self):      ## does not print well
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""
        adjacency_list = self.get_adjacency_list()
        def convert_to_names(pair, graph=self):
            node_number, value = pair
            return (graph._node_names[node_number], value)
        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)
        m =  [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]
        return m

    def get_adjacency_list_names(self):   # O(n^2) simplest implementation
        adjacency_list = self.get_adjacency_list()
        al_names = []
        for ale in adjacency_list:
            al_node = []
            if ale:
                for pair in ale:
                    al_node.append(( self._node_names[pair[0]], pair[1] ))
                al_names.append(al_node)
            else:
                al_names.append(None)
        return(al_names)

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]
        for edg in self._edges:
            from_index, to_index = edg._node_from._value, edg._node_to._value
            adjacency_matrix[from_index][to_index] = edg._value
        return adjacency_matrix

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self._node_names) > 0:
            return len(self._node_names)
        max_index = -1
        if len(self._nodes):
            for node in self._nodes:
                if node._value > max_index:
                    max_index = node._value
        return max_index

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self._nodes:
            node._visited = False


    def dfs_helper(self, start_node):
        """The helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        REQUIRES: self._clear_visited() to be called before
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the traversed node values (integers).
         """
        ret_list = [start_node._value]
        start_node._visited = True
        edges_out  = [e for e in start_node._edges
                      if e._node_to._value != start_node._value]
        for edge in edges_out:
            if not edge._node_to._visited:
                ret_list.extend(self.dfs_helper(edge._node_to))

        return ret_list

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self._node_names[num] for num in self.dfs(start_node_num)]


    def bfs(self, start_node_num):
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = []
        queue = [node] # a list
        node._visited = True
        def enqueue(n, q=queue): #func in a func
            n._visited = True
            q.append(n)
        def unvisited_outgoing_edge(n,e):
             return ((e._node_from._value == n._value) and not (e._node_to._visited))

        while queue: #as some elements in
            node = queue.pop(0) #get a head element from the queue
            ret_list.append(node._value)
            for e in node._edges:
                if unvisited_outgoing_edge(node, e):
                    enqueue(e._node_to)
        return ret_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self._node_names[num] for num in self.bfs(start_node_num)]

#---------------- testing ---------------#
def testGraphTraversal():

    graph = Graph()

    graph.set_node_names(('Mountain View', # 0
                        'San Francisco',   # 1
                        'London',          # 2
                        'Shanghai',        # 3
                        'Berlin',          # 4
                        'Sao Paolo',       # 5
                        'Bangalore'))      # 6

    graph.insert_edge(51, 0, 1)     # MV <-> SF
    graph.insert_edge(51, 1, 0)     # SF <-> MV
    graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
    graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
    graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
    graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
    graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
    graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
    graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
    graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
    graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
    graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
    graph.insert_edge(932, 2, 4)    # London <-> Berlin
    graph.insert_edge(932, 4, 2)    # Berlin <-> London
    graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
    graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London

    # (6) 'Bangalore' is intentionally disconnected (no edges)
    # for this problem and should produce None in the
    # Adjacency List, etc.

    import pprint
    pp = pprint.PrettyPrinter(indent=2)

    print("Edge List")
    pp.pprint(graph.get_edge_list_names())

    print("\nAdjacency List")
    pp.pprint(graph.get_adjacency_list_names())

    print("\nAdjacency Matrix")
    pp.pprint(graph.get_adjacency_matrix())

    #DFS
    print("\nDepth First Search")   #no bangalore as it is a disconneted node
    pp.pprint(graph.dfs_names(2))

    #BFS
    print("Breadth First Search")
    pp.pprint(graph.bfs_names(2))


def main():
    testGraphTraversal()



if __name__ == '__main__':
        main()
