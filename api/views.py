from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializer import ApplyCreditUserSerializer
from . models import ApplyCreditUser

@api_view(['GET'])
def getCredits(request):
    credits = ApplyCreditUser.objects.all()
    serializer = ApplyCreditUserSerializer(credits, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def getCredit(request, id):
    credit = ApplyCreditUser.objects.get(id = id)
    serializer = ApplyCreditUserSerializer(credit, many = False)

    return Response(serializer.data)

@api_view(['POST'])
def postCredit(request):
    serializer = ApplyCreditUserSerializer(data = request.data, many = False)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateCredit(request, id):
    credit = ApplyCreditUser.objects.get(id = id)
    serializer = ApplyCreditUserSerializer(instance = credit, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
