from django.urls import re_path
from .views import search

app_name = 'posts'

urlpatterns = [
    re_path('^$',search,name='search'),



]
