from django.shortcuts import render

from .models import Job
from blog.models import Blog

def home(request):
    jobs = Job.objects
    blogs = Blog.objects.all()
    return render(request, 'jobs/home.html', {'jobs':jobs,'blogs':blogs})
