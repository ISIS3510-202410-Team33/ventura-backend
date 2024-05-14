import heapq

INFINITY = 1_000_000_000_000


class Route:
    def __init__(self):
        self.nodes = list()
        self._complete = False
        self.distance = 0

    def add_node(self, node_id):
        self.nodes.append(node_id)

    def get_nodes(self):
        return self.nodes

    def set_distance(self, distance):
        self.distance = distance

    def set_complete(self):
        self._complete = True
        self.nodes.reverse()

    def is_complete(self):
        return self._complete



class Node:
    def __init__(self, site_id):
        self.site_id = site_id
        self.d = INFINITY
        self.parent = None
        self.visited = False
        self.adj = list()


class Graph:
    def __init__(self, id, vertices, edges):
        """
        :param id: the id of the graph
        :param vertices: iterable of vertix ids
        :param edges: iterable of edges in the form (u,v,w). Non directed.
        """
        self.id = id
        self.nodes = dict()
        self.__set_vertices(vertices)
        self.__set_edges(edges)

    def __set_vertices(self, vertices):
        """
        Sets the vertices
        :param vertices: iterable of vertex ids
        """
        for v in vertices:
            self.nodes[v] = Node(v)

    def __set_edges(self, edges: list):
        """
        Sets the edges
        :param edges: iterable of tuples (u,v,w). Edges are non directed and connect nodes inside the graph
        """
        for e in edges:
            u, v, w = e
            self.nodes[u].adj.append((v, w))
            self.nodes[v].adj.append((u, w))

    def reset_route(self):
        """
        Resets values needed for a route algorithm
        """
        for k in self.nodes:
            node = self.nodes[k]
            node.d = INFINITY
            node.parent = None
            node.visited = False

    def dijkstra(self, s: str, t: str) -> Route:
        """
        Finds the shortest path from s to t
        :param s: site_id to start
        :param t: site_id to finish
        :return: a route instance with the shortest path
        """
        self.reset_route()

        to = list()
        self.nodes[s].d = 0
        heapq.heappush(to, (self.nodes[s].d, s, None))

        while len(to) > 0:
            d, u, parent = heapq.heappop(to)
            self.nodes[u].d = d
            self.nodes[u].parent = parent
            self.nodes[u].visited = True

            for edge in self.nodes[u].adj:
                v, w = edge
                if not self.nodes[v].visited and self.nodes[u].d + w < self.nodes[v].d:
                    heapq.heappush(to, (self.nodes[u].d + w, v, u))

        route = Route()
        # t was reachable
        if self.nodes[t].d != INFINITY:
            route.set_distance(self.nodes[t].d)

            curr = t
            route.add_node(self.nodes[curr].site_id)
            while self.nodes[curr].parent is not None:
                route.add_node(self.nodes[curr].parent)
                curr = self.nodes[curr].parent

            route.set_complete()

        return route
