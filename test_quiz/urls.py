from django.conf.urls import patterns, include, url
from django.contrib import admin
#from accounts.views import UserViewSet
from rest_framework import routers
from features import views
from interactions.views import CommentViewSet



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'portfolios', views.PortfolioViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'instruments', views.InstrumentViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_quiz.views.home', name='home'),
    # url(r'^test_quiz/', include('test_quiz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('^', include(router.urls)),
)
