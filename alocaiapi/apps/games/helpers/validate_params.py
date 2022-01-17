
  
from django.db.models import Q
from rest_framework.serializers import ValidationError

from ..models import Game


def validate_params(params):
    """
    Function that returns all the games 
    that will fit in the pen-drive
    """
    if params:
                   
        return "menu_obj"
    else:
        raise ValidationError({
            "message": 'Kindly pass pen_drive_space in params'}
        )
