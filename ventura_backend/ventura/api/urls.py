from rest_framework.routers import DefaultRouter
from ventura.api.views import CollegeViewSet, College_locationViewSet, usersViewSet, user_calificationsViewSet, user_frequenciesViewSet

router = DefaultRouter()
router.register(r'colleges', CollegeViewSet, basename='college')
router.register(r'college_locations', College_locationViewSet, basename='college_location')
router.register(r'users', usersViewSet, basename='user')
router.register(r'user_califications', user_calificationsViewSet, basename='user_calification')
router.register(r'user_frequencies', user_frequenciesViewSet, basename='user_frequency')

urlpatterns = router.urls
