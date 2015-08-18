from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from interactions.models import *
from features.serializers import *

from django.contrib.auth import authenticate
from django.template.loader import render_to_string
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class CommentsSerializer(serializers.ModelSerializer):
    '''
     Serializer class for Portfolio model
    '''
    parent = serializers.SerializerMethodField()

    def get_parent(self, obj):
        parent = None
        if obj.parent_portfolio:
            parent_obj = obj.parent_portfolio
            parent = PortfolioSerializer(parent_obj)
        elif obj.parent_user:
            parent_obj = obj.parent_user
            parent = UserSerializer(parent_obj)
        elif obj.parent_instrument:
            parent_obj = obj.parent_instrument
            parent = InstrumentSerializer(parent_obj)

        return parent.data

    class Meta:
        model = Comments
        fields = ('id','comment','parent')
