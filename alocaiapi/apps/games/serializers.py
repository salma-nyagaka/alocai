from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Game


class   GameSerializer(serializers.ModelSerializer):
    """ Serialize a game's data"""
    # Ensure that name is unique, does not exist,
    # and cannot be left be blank
    
    name = serializers.RegexField(
        regex='[a-zA-Z0-9 ]',
        min_length=4,
        max_length=30,
        required=True,
        validators=[UniqueValidator(
            queryset=Game.objects.all(),
            message='The name already exists. Kindly try another.'
        )],
        error_messages={
            "blank": "Name cannot be empty.",
            "min_length": "Name should have more than 4 characters",
            "max_length": "Name should have less than  characters",

        },   
        )
   
    price = serializers.RegexField(
        regex='[+-]?([0-9]*[.])?[0-9]+',
        required=True,
    )

    space = serializers.RegexField(
        regex='^[1-9]+[0-9]*$',
        required=True,
    )
    
    class Meta:
        model = Game
        fields = ['name', 'price', 'space']

        extra_kwargs = {
                    'name': {
                        'error_messages': {
                            'blank': 'my custom error message for title'
                        }
                    }
                }