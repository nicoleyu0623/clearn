class Node:
    def __init__(self, value):
        self._value = value
        self._edges = []


class Edge:
    def __init__(self, value, node_from, node_to):
        self._value = value
        self._node_from = node_from
        self._node_to = node_to


class Graph:
    def __init__(self, nodes=[], edges=[]):
        self._nodes = nodes
        self._edges = edges


    def insert_node(self, new_node_value):
        new_node = Node(new_node_value)
        self._nodes.append(new_node)


    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for n in self._nodes:
                if n._value == node_from_val:
                    from_found = n
                if n._value == node_to_val:
                    to_found = n
        if from_found is None:
            from_found = Node(node_from_val)
            self._nodes.append(from_found)
        if to_found is None:
            to_found = Node(node_to_val)
            self._nodes.append(to_found)

        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found._edges.append(new_edge)
        to_found._edges.append(new_edge)
        self._edges.append(new_edge)


    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_vals = []
        for e in self._edges:
            edge_vals.append((e._value, e._node_from._value, e._node_to._value))
        return edge_vals

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)
        szi working for directed graphs
        """

        adjency_l = [None] * (self.find_max_index()+1)

        for e in self._edges:
            if adjency_l[e._node_from._value] is not None:
                adjency_l[e._node_from._value].append((e._node_to._value, e._value ))
            else:
                adjency_l[e._node_from._value] = [(e._node_to._value, e._value )]

        return adjency_l

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_idx = self.find_max_index()
        nodes_l = [None] * (max_idx+1)
        for n in self._nodes:
            nodes_l[n._value] = n
        adj_matrix = []
        for node in nodes_l:
            node_conn = [0] * (max_idx+1)
            if node:
                for e in self._edges:
                    if node._value == e._node_from._value:
                        node_conn[e._node_to._value] = e._value
            adj_matrix.append(node_conn)
        return adj_matrix

    def get_adjacency_matrix_clean(self):
        max_index = self.find_max_index()
        adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        for edge_object in self._edges:
            adjacency_matrix[edge_object._node_from._value][edge_object._node_to._value] = edge_object._value
        return adjacency_matrix


    def find_max_index(self):
        max_index = -1
        if len(self._nodes):
            for n in self._nodes:
                if n._value > max_index:
                    max_index = n._value
        return max_index


#---------------- testing ---------------#
def testGraphRepresentation():

    graph = Graph()
    graph.insert_edge(100, 1,2)
    graph.insert_edge(101, 1,3)
    graph.insert_edge(102, 1,4)
    graph.insert_edge(103, 3,4)
    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print(graph.get_edge_list())
    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print(graph.get_adjacency_list())
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print(graph.get_adjacency_matrix())
    print(graph.get_adjacency_matrix_clean())

def main():
    testGraphRepresentation()

if __name__ == '__main__':
        main()
