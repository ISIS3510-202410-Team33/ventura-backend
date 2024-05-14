"""
    Functionality in order to find the shortest route between two places

    @author: <c4ts0up>
"""
from ..models import University, Building, SiteType, Site, SiteAdjacency
from .algorithms.graphs import Graph
from django.core.cache import cache
from django.conf import settings


def load_university_graph(university_id: int):
    """
    Retrieves data from the database and loads it as a graph in cache
    """
    # checks if its already loaded

    if cache.get(university_id) is None:
        print("Caching university", university_id)
        # loads all the data from the database
        university = University.objects.get(id=university_id)

        buildings_id = Building.objects.filter(university=university).values('id')
        buildings_id_fast = set([d['id'] for d in buildings_id])

        sites_id = Site.objects.filter(building__id__in=buildings_id_fast).values('id')
        sites_id_fast = set([d['id'] for d in sites_id])

        site_adjacency_from = SiteAdjacency.objects.filter(a_site__id__in=sites_id_fast)
        site_adjacency_to = SiteAdjacency.objects.filter(b_site__id__in=sites_id_fast)
        site_adjacency_from.union(site_adjacency_to)

        site_adjacency = site_adjacency_from.values('a_site', 'b_site', 'distanceInM')

        adjacency = [(d['a_site'], d['b_site'], d['distanceInM']) for d in site_adjacency]

        # creates the graph
        # sites_id_fast is iterable, so it works for vertices
        g = Graph(id=university_id, vertices=sites_id_fast, edges=adjacency)

        cache.set(university_id, g, timeout=settings.UNIVERSITY_GRAPH_CACHE_TIMEOUT)
    else:
        print("University", university_id, "taken from caché")

    return cache.get(university_id)


def shortest_path(university_id, site_from_id, site_to_id):
    # loads the graph
    university_graph = load_university_graph(university_id)
    # clear the graph
    university_graph.reset_route()
    # apply shortest path algorithm
    route = university_graph.dijkstra(site_from_id, site_to_id)

    return route

