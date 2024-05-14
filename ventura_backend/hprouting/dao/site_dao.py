"""
    File for Site model access
"""
from ..models import Site


def get_site(site_id: str):
    data = Site.objects.filter(pk=site_id)
    if len(data) > 0:
        return data[0]
    else:
        return None


def get_all_sites():
    return Site.objects.all()


def get_sites_by_building(building_id: int):
    return Site.objects.filter(building=building_id)
