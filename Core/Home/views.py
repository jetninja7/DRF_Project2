from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .Serializers import PeopleSerializer

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):
    courses = {
            'course_name': 'Python',
            'learn': ['Flask', 'Django', 'FastAPI'],
            'course_provider': 'AMAZON'
    }
    if request.method == 'GET':
        print("You are in get method")
        return Response(courses)

    elif request.method == 'POST':
        print("You are in post method")
        return Response(courses)

    elif request.method == 'PUT':
        print("You are in put method")
        return Response(courses)

    elif request.method == 'PATCH':
        print("You are in patch method")
        return Response(courses)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        objs = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(objs, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        objs = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(objs, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    else:
        data = request.data
        objs = Person.objects.get(id=data['id'])
        objs.delete()
        return Response({"message": "User Deleted Successfully"})
