
from django.http import JsonResponse
from rest_framework import viewsets
from ventura.models import College, College_location, User, User_calification, User_frequency
from ventura.api.serializer import CollegeSerializer, College_locationSerializer, UserSerializer, User_calificationSerializer, User_frequencySerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    def get_queryset(self):
        college_id = self.request.query_params.get('id', None)
        if college_id is not None:
            return College.objects.filter(id=college_id)
        return College.objects.all()

class College_locationViewSet(viewsets.ModelViewSet):
    queryset = College_location.objects.all()
    serializer_class = College_locationSerializer

    def get_queryset(self):
        college_id = self.request.query_params.get('college_id', None)
        location_id = self.request.query_params.get('location_id', None)
        if location_id is not None:
            return College_location.objects.filter(id=location_id)
        elif college_id is not None:
            return College_location.objects.filter(college_id=college_id)
        return College_location.objects.all()


class usersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        if id is not None:
            return User.objects.filter(id=id)
        return User.objects.all()
    
class user_calificationsViewSet(viewsets.ModelViewSet):
    queryset = User_calification.objects.all()
    serializer_class = User_calificationSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user_id', None)
        location = self.request.query_params.get('location_id', None)
        if user is not None and location is not None:
            return User_calification.objects.filter(user_id=user , college_location_id=location)
        elif user is not None:
            return User_calification.objects.filter(user_id=user)
        elif location is not None:
            return User_calification.objects.filter(college_location_id=location)
        
        return User_calification.objects.all()

class user_frequenciesViewSet(viewsets.ModelViewSet):
    queryset = User_frequency.objects.all()
    serializer_class = User_frequencySerializer

    def get_queryset(self):
        user = self.request.query_params.get('user_id', None)
        location = self.request.query_params.get('location_id', None)
        if user is not None and location is not None:
            return User_frequency.objects.filter(user_id=user , college_location_id=location)
        elif user is not None:
            return User_frequency.objects.filter(user_id=user)
        elif location is not None:
            return User_frequency.objects.filter(college_location_id=location)
        return User_frequency.objects.all()
    
    def patch(self,request):

        user = self.request.query_params.get('user_id', None)
        location = self.request.query_params.get('location_id', None)
        
        if user is None or location is None:
            return JsonResponse(status = 400, data={"error": "There is no user_id or location_id in the request"})
       # if no model exists by this PK, raise a 404 error
        modelList = User_frequency.objects.filter(user_id=user, college_location_id=location)
        if modelList.count() == 0:
            return JsonResponse(status=404, data={"error": "No register exists by this user or location"})

        model = modelList.first()
        # this is the only field we want to update        
        data = {"frequency": model.frequency + int(1)}
        serializer = User_frequencySerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(status = 200, data=serializer.data)
        # return a meaningful error response
        return JsonResponse(status = 400, data={"error": "Bad request"})
    

    
    

        