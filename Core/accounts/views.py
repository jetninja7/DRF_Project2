from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AccountSerializer
from .models import Account

# Create your views here.
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        objs = Account.objects.all()
        serializer = AccountSerializer(objs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
