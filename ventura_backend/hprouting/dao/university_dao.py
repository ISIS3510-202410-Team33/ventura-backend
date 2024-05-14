"""
    File for University data access
"""
from ..models import University


def get_university(university_id):
    data = University.objects.filter(pk=university_id)
    if len(data) > 0:
        return data[0]
    else:
        return None


def get_all_universities():
    return University.objects.all()
