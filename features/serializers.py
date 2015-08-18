from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from features.models import *

from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class PortfolioSerializer(serializers.ModelSerializer):
    '''
     Serializer class for Portfolio model
    '''
    class Meta:
        model = Portfolio
        fields = ('id', 'name', 'object_type', 'today_prc')

class UserSerializer(serializers.ModelSerializer):
    '''
     Serializer class for User model
    '''
    class Meta:
        model = User
        fields = ('id', 'name', 'object_type')


class InstrumentSerializer(serializers.ModelSerializer):
    '''
     Serializer class for User model
    '''
    class Meta:
        model = Instrument
        fields = ('id', 'name', 'object_type', 'today_prc')