from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from features.models import *
from interactions.serializers import *

class CommentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer