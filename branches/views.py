from django.shortcuts import render
from .models import Branch
from django.views.generic import ListView, CreateView, FormView

# Create your views here.


class BranchListView(ListView):
    model = Branch
    template_name = 'branches/branch_list.html'
