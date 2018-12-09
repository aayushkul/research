from django.urls import re_path
from . import views

app_name = 'branches'

urlpatterns = [
    re_path('^$',views.BranchListView.as_view(),name='branch'),

]
