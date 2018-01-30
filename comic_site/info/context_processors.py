from django.conf import settings
from .models import Info

def debug(context):
    return {'DEBUG': settings.DEBUG}

def info(context):
    return {'info': Info.load()}