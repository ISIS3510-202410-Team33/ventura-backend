

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from ventura.models import College, College_location, User, User_calification, User_frequency
from ventura.api.serializer import CollegeSerializer, College_locationSerializer, UserSerializer, User_calificationSerializer, User_frequencySerializer


# COLLEGES API
# GET /api/colleges/ -> returns all colleges
# GET /api/colleges/?id=<id> -> returns the college with id <id>
# POST /api/colleges/ -> creates a new college
# PUT /api/colleges/?id=<id> -> updates the college with id <id>

class CollegeViewSet(viewsets.ModelViewSet):

    #POST implementation is available by default in the ModelViewSet class
    #PUT implementation is available by default in the ModelViewSet class
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

    # GET implementation for the CollegeViewSet 
    # Available URLs:
    # /api/colleges/ -> returns all colleges
    # /api/colleges/?id=<id> -> returns the college with id <id>
    def get_queryset(self):
        college_id = self.request.query_params.get('id', None)
        if college_id is not None:
            return College.objects.filter(id=college_id)
        return College.objects.all()

# COLLEGE LOCATIONS API
# GET /api/college_locations/ -> returns all college locations
# GET /api/college_locations/?college_id=<college_id> -> returns the college locations of the college with id <college_id>
# GET /api/college_locations/?location_id=<location_id> -> returns the college location with id <location_id>
# GET /api/college_locations/?college_id=<college_id>&location_id=<location_id> -> returns the college location with id <location_id> of the college with id <college_id>
# POST /api/college_locations/ -> creates a new college location
# PUT /api/college_locations/?location_id=<location_id> -> updates the college location with id <location_id>

class College_locationViewSet(viewsets.ModelViewSet):

    #POST implementation is available by default in the ModelViewSet class
    #PUT implementation is available by default in the ModelViewSet class
    queryset = College_location.objects.all()
    serializer_class = College_locationSerializer

    # GET implementation for the College_locationViewSet
    # Available URLs:
    # /api/college_locations/ -> returns all college locations
    # /api/college_locations/?college_id=<college_id> -> returns the college locations of the college with id <college_id>
    # /api/college_locations/?location_id=<location_id> -> returns the college location with id <location_id>
    # /api/college_locations/?college_id=<college_id>&location_id=<location_id> -> returns the college location with id <location_id> of the college with id <college_id>

    def get_queryset(self):
        college_id = self.request.query_params.get('college_id', None)
        location_id = self.request.query_params.get('location_id', None)
        if location_id is not None and college_id is not None:
            return College_location.objects.filter(id=location_id, college_id=college_id)
        elif location_id is not None:
            return College_location.objects.filter(id=location_id)
        elif college_id is not None:
            return College_location.objects.filter(college_id=college_id)
        return College_location.objects.all()

# USERS API
# GET /api/users/ -> returns all users
# GET /api/users/?id=<id> -> returns the user with id <id>
# GET /api/users/?email=<email> -> returns the user with email <email>
# GET /api/users/?name=<name> -> returns the user with name <name>
# POST /api/users/ -> creates a new user
# PUT /api/users/?id=<id> -> updates the user with id <id>

class usersViewSet(viewsets.ModelViewSet):

    #POST implementation is available by default in the ModelViewSet class
    #PUT implementation is available by default in the ModelViewSet class
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # GET implementation for the usersViewSet
    # Available URLs:
    # /api/users/ -> returns all users
    # /api/users/?id=<id> -> returns the user with id <id>
    # /api/users/?email=<email> -> returns the user with email <email>
    # /api/users/?name=<name> -> returns the user with name <name>

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        email = self.request.query_params.get('email', None)
        name = self.request.query_params.get('name', None)
        if id is not None:
            return User.objects.filter(id=id)
        elif email is not None:
            return User.objects.filter(email=email)
        elif name is not None:
            return User.objects.filter(name=name)
        return User.objects.all()

# USER CALIFICATIONS API
# GET /api/user_califications/ -> returns all user califications
# GET /api/user_califications/?user_id=<user_id> -> returns the user califications of the user with id <user_id>
# GET /api/user_califications/?location_id=<location_id> -> returns the user califications of the location with id <location_id>
# GET /api/user_califications/?user_id=<user_id>&location_id=<location_id> -> returns the user califications of the user with id <user_id> of the location with id <location_id>
# POST /api/user_califications/ -> creates a new user calification
# PUT /api/user_califications/?id=<id> -> updates the user calification with id <id>
   
class user_calificationsViewSet(viewsets.ModelViewSet):

    #POST implementation is available by default in the ModelViewSet class
    #PUT implementation is available by default in the ModelViewSet class
    queryset = User_calification.objects.all()
    serializer_class = User_calificationSerializer


    # GET implementation for the user_calificationsViewSet
    # Available URLs:
    # /api/user_califications/ -> returns all user califications
    # /api/user_califications/?user_id=<user_id> -> returns the user califications of the user with id <user_id>
    # /api/user_califications/?location_id=<location_id> -> returns the user califications of the location with id <location_id>
    # /api/user_califications/?user_id=<user_id>&location_id=<location_id> -> returns the user califications of the user with id <user_id> of the location with id <location_id>
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

# USER FREQUENCIES API
# GET /api/user_frequencies/ -> returns all user frequencies
# GET /api/user_frequencies/?user_id=<user_id> -> returns the user frequencies of the user with id <user_id>
# GET /api/user_frequencies/?location_id=<location_id> -> returns the user frequencies of the location with id <location_id>
# GET /api/user_frequencies/?user_id=<user_id>&location_id=<location_id> -> returns the user frequencies of the user with id <user_id> of the location with id <location_id>
# POST /api/user_frequencies/ -> creates a new user frequency
# PUT /api/user_frequencies/?id=<id> -> updates the user frequency with id <id>
# PATCH /api/user_frequencies/?user_id=<user_id>&location_id=<location_id> -> increments the frequency of the user with id <user_id> of the location with id <location_id> by 1


class user_frequenciesViewSet(viewsets.ModelViewSet):

    #POST implementation is available by default in the ModelViewSet class
    #PUT implementation is available by default in the ModelViewSet class
    queryset = User_frequency.objects.all()
    serializer_class = User_frequencySerializer

    # GET implementation for the user_frequenciesViewSet
    # Available URLs:
    # /api/user_frequencies/ -> returns all user frequencies
    # /api/user_frequencies/?user_id=<user_id> -> returns the user frequencies of the user with id <user_id>
    # /api/user_frequencies/?location_id=<location_id> -> returns the user frequencies of the location with id <location_id>
    # /api/user_frequencies/?user_id=<user_id>&location_id=<location_id> -> returns the user frequencies of the user with id <user_id> of the location with id <location_id>

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
    
    # PATCH implementation for the user_frequenciesViewSet
    # Available URLs:
    # /api/user_frequencies/?user_id=<user_id>&location_id=<location_id> -> increments the frequency of the user with id <user_id> of the location with id <location_id> by 1

    def patch(self,request):

        user = self.request.query_params.get('user_id', None)
        location = self.request.query_params.get('location_id', None)
        
        if user is None or location is None:
            return JsonResponse(status = 400, data={"error": "There is no user_id or location_id in the request"})
       # if no user model exists by this PK, raise a 404 error
        userModel = User.objects.filter(id=user)
        locationModel = College_location.objects.filter(id=location)
        if userModel.count() == 0 or locationModel.count() == 0:
            return JsonResponse(status = 404, data={"error": "User or location not exists"})
        
        modelList = User_frequency.objects.filter(user_id=user, college_location_id=location)
        if modelList.count() == 0:
            User_frequency.objects.create(user_id=user, college_location_id=location, frequency=1)
            return JsonResponse(status = 201, data={"message": "New register created"})

        model = modelList.first()
        # this is the only field we want to update        
        data = {"frequency": model.frequency + int(1)}
        serializer = User_frequencySerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(status = 200, data=serializer.data)
        # return a meaningful error response
        return JsonResponse(status = 400, data={"error": "Bad request"})

class UserFrequencyLocationAnalysisViewSet(viewsets.ModelViewSet):
    queryset = College_location.objects.all()
    serializer_class = College_locationSerializer


    # GET implementation for the UserFrequencyLocationAnalysisViewSet
    # Available URLs:
    # /api/user_frequencies/analysis/?user_id=<user_id>&method=reccommended_most_visited -> returns the list of recommended college locations based on the most visited location by the user with id <user_id>
    # /api/user_frequencies/analysis/?method=recommended_most_visited -> returns the list of recommended college locations based on the most visited location by any user
    # /api/user_frequencies/analysis/?method=best_rated -> returns the list of recommended college locations based on the best rated location by any user
    # 
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        method = self.request.query_params.get('method', None)

        if method is not None: 
            print(method)
            if method == 'recommended_most_visited':
                nameMostVisited = None
                if user_id is not None:
                    mostVisitedByUser = User_frequency.objects.filter(user_id=user_id).order_by('-frequency').first()
                    if mostVisitedByUser is not None:
                        nameMostVisited = mostVisitedByUser.college_location.name
                else:
                    mostVisited = User_frequency.objects.order_by('-frequency').first()
                    if mostVisited is not None:
                        nameMostVisited = mostVisited.college_location.name
                if nameMostVisited is None:
                    return College_location.objects.none()
                print("Most visited location")
                print(nameMostVisited)
                return College_location.objects.filter(name__icontains=nameMostVisited)
            if method == 'best_rated':
                bestRated = User_calification.objects.order_by('-calification').first()
                print(bestRated.id)
                if bestRated is None:
                    return College_location.objects.none()
                return College_location.objects.filter(id=bestRated.college_location.id)
        else:
            return College_location.objects.none()