from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('health-check/', views.health_check, name='hprouting'),
    path('university/<int:university_id>/', views.university_detail, name='university-details'),
    path('building/<str:building_id>/', views.building_detail, name='building-details'),
    path('site/<str:site_id>/', views.site_detail, name='site-details'),
    path('university/<int:university_id>/buildings/', views.buildings_by_university, name='buildings-by-university'),
    path('building/<str:building_id>/sites/', views.sites_by_building, name='sites-by-building'),
    path('shortest-route-between-sites/', views.shortest_route_between_sites, name='shortest-route-between-sites')
]
