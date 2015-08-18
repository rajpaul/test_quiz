from django.db import models
#from features.models import *

# Create your models here.


class Comments(models.Model):
    '''
    Define comment class with different type of parents
    '''
    comment = models.TextField()
    parent_portfolio = models.ForeignKey('features.Portfolio', blank=True, null=True)
    parent_user = models.ForeignKey('features.User', blank=True, null=True)
    parent_instrument = models.ForeignKey('features.Instrument', blank=True, null=True)

    def __str__(self):
        return "Comment : {0}".format(self.comment)

