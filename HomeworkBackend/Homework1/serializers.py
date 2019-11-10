from rest_framework import serializers

from HomeworkBackend.Homework1.models import Pokemon, PokemonTrainer


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'type', 'catch_date', 'level', 'trainer']


class PokemonTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonTrainer
        fields = ['id', 'first_name', 'last_name', 'age']