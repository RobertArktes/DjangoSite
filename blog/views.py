from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog_template/home_page.html')