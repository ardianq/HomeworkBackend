from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from HomeworkBackend.Homework1.models import Pokemon, PokemonTrainer
from HomeworkBackend.Homework1.serializers import PokemonSerializer, PokemonTrainerSerializer


@csrf_exempt
@api_view(['GET','POST'])
def pokemon_list(request):
    if request.method == 'GET':
        pokemon = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemon, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PokemonSerializer(data=request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','PUT', 'DELETE'])
def pokemon_detail(request, id):
    try:
        pokemon = Pokemon.objects.get(pk=id)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET','POST'])
def pokemon_trainer_list(request):
    if request.method == 'GET':
        pokemon_trainer = PokemonTrainer.objects.all()
        serializer = PokemonTrainerSerializer(pokemon_trainer, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PokemonTrainerSerializer(data=request.data, many = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT', 'DELETE'])
def pokemon_trainer_detail(request, id):
    try:
        pokemon_trainer = PokemonTrainer.objects.get(pk=id)
    except PokemonTrainer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PokemonTrainerSerializer(pokemon_trainer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PokemonTrainerSerializer(pokemon_trainer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pokemon_trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

