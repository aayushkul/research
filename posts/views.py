from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from branches.models import Branch, Journal
from django.shortcuts import render
# Create your views here.

def search(request):

    if request.method == 'POST':
        branch_name = request.POST.get('branch')
        object_list = Post.objects.filter(journal__branch__name=branch_name)
        return render(request,'posts/post_list.html',context={'object_list':object_list, 'branch_name':branch_name})
    else:
        pass
