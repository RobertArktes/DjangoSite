from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import models

urlpatterns = [
    url('', ListView.as_view(queryset=models.Articles.objects.all().order_by('-date')[:20],template_name='blog_template/home_page.html')),
]
