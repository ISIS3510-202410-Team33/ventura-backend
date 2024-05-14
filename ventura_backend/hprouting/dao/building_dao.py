"""
    File for Building data access
"""
from ..models import Building


def get_building(building_id):
    data = Building.objects.filter(pk=building_id)
    if len(data) > 0:
        return data[0]
    else:
        return None


def get_all_buildings():
    return Building.objects.all()


def get_buildings_by_university(university_id):
    return Building.objects.filter(university=university_id)
