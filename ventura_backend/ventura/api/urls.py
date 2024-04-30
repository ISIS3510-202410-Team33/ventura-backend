from django.urls import path
from rest_framework.routers import DefaultRouter
from ventura.api.views import (
    CollegeViewSet,
    College_locationViewSet,
    usersViewSet,
    user_calificationsViewSet,
    user_frequenciesViewSet,
    UserFrequencyLocationAnalysisViewSet,
)
from ventura.views import building_ratings  # import the new view

router = DefaultRouter()
router.register(r"colleges", CollegeViewSet, basename="college")
router.register(
    r"college_locations", College_locationViewSet, basename="college_location"
)
router.register(r"users", usersViewSet, basename="user")
router.register(
    r"user_califications", user_calificationsViewSet, basename="user_calification"
)
router.register(
    r"user_frequencies/analysis",
    UserFrequencyLocationAnalysisViewSet,
    basename="user_frequency_analysis",
)
router.register(r"user_frequencies", user_frequenciesViewSet, basename="user_frequency")

# add the new URL pattern
urlpatterns = [
    path("building_ratings/", building_ratings, name="building_ratings"),
] + router.urls
