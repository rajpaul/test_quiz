from django.db import models
from django.contrib.auth.models import User
from interactions.models import Comments

# Create your models here.

OBJECT_TYPE = (
    ('PORTFOLIO', 'PORTFOLIO'),
    ('USER', 'USER'),
    ('INSTRUMENT', 'INSTRUMENT'),

)

class ObjectType(models.Model):
    '''
        Define ObjectType for the reference to any related models(Class) i.e. Portfolio, Instrument etc.
    '''

    name = models.CharField(max_length=80)
    created_by = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Portfolio(models.Model):
    '''
     Define Portfolio model with reference object_type and its attributes.
    '''
    name = models.CharField(max_length=80)
    #object_type = models.ForeignKey(ObjectType, blank=True, null=True)
    object_type = models.CharField(max_length=31, choices=OBJECT_TYPE, verbose_name="ObjectType",blank=True, null=True)
    today_prc = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return "Name : {0} - Type : {1}".format(self.name, self.object_type)


class Instrument(models.Model):
    '''
     Define Portfolio model with reference object_type and its attributes.
    '''
    name = models.CharField(max_length=80)
    object_type = models.CharField(max_length=31, choices=OBJECT_TYPE, verbose_name="ObjectType", blank=True, null=True)
    today_prc = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return "Name : {0} - Type : {1}".format(self.name, self.object_type)

class User(models.Model):
    '''
     Define User model with reference object_type and its attributes.
     NOTE : We could use django core User from django.contrib.auth.models package as User class
    '''
    name = models.CharField(max_length=80)
    object_type = models.CharField(max_length=31, choices=OBJECT_TYPE, verbose_name="ObjectType", blank=True, null=True)

    def __str__(self):
        return "Name : {0} - Type : {1}".format(self.name, self.object_type)