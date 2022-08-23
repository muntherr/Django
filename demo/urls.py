# this is for the project
from django.urls import path, include
from . import views
from .views import Another
from rest_framework import routers
from .views import  BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet) # Register a url
urlpatterns = [
    path('',include(router.urls)), # I can have some folder in my application, and will refrence to another file
   # path('firstfunction',first), # TO make entry view, and pointing to the class
]


# A token is a random string of char that generated from django used to authenticate the user
#