import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .dao import site_dao, university_dao, building_dao
from .logic import shortest_route
from .models import University, Building, Site


# Create your views here.
def health_check(request):
    return HttpResponse(200)


# def test_load(request):
#     university_id = 3  # Replace with the desired university ID
#     university_data, building_data, site_type_data, site_data, site_adjacency_data = load_university(university_id)
#     print("University data:", university_data)
#     print("Building data:", building_data)
#     print("Site type data:", site_type_data)
#     print("Site data:", site_data)
#     print("Site adjacency data:", site_adjacency_data)
#
#     return JsonResponse(site_data, safe=False)


def university_detail(request, university_id: int):
    """
    Fetches the corresponding university data
    """
    if request.method == 'GET':
        university = university_dao.get_university(university_id)

        if university is None:
            return HttpResponse(status=404)
        else:
            return JsonResponse(university.to_json(), safe=False)
    else:
        return HttpResponse(status=403)


def building_detail(request, building_id: str):
    if request.method == 'GET':
        building = building_dao.get_building(building_id)

        if building is None:
            return HttpResponse(status=400)
        else:
            return JsonResponse(building.to_json(), safe=False)
    else:
        return HttpResponse(status=403)


def site_detail(request, site_id: str):
    if request.method == 'GET':
        site = site_dao.get_site(site_id)

        if site is None:
            return HttpResponse(status=404)
        else:
            return JsonResponse(site.to_json(), safe=False)
    else:
        return HttpResponse(status=403)


def buildings_by_university(request, university_id: int):
    if request.method == 'GET':
        buildings = building_dao.get_buildings_by_university(university_id)

        if buildings is None:
            return HttpResponse(status=404)
        else:
            return JsonResponse(
                [b.to_json() for b in buildings],
                safe=False
            )
    else:
        return HttpResponse(status=404)


def sites_by_building(request, building_id: int):
    if request.method == 'GET':
        sites = site_dao.get_sites_by_building(building_id)

        if sites is None:
            return HttpResponse(status=404)
        else:
            return JsonResponse(
                [s.to_json() for s in sites],
                safe=False
            )
    else:
        return HttpResponse(status=403)


@csrf_exempt
def shortest_route_between_sites(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        # extracts relevant ids
        site_from_id = json_data.get('site_from_id')
        site_to_id = json_data.get('site_to_id')
        university_id = json_data.get('university_id')

        # body is incomplete
        if site_from_id is None or site_to_id is None or university_id is None:
            return HttpResponse(status=400)

        route = shortest_route.shortest_path(university_id, site_from_id, site_to_id)

        if route.is_complete():
            pulled_sites = [site_dao.get_site(site_id).to_json() for site_id in route.nodes]

            route_json = {
                "sites": pulled_sites,
                "distance": route.distance
            }
        else:
            route_json = {
                "sites": list(),
                "distance": -1
            }

        return JsonResponse(route_json)
    else:
        return HttpResponse(status=403)
