from django.shortcuts import render


# Create your views here.

def home(request):
    jobs = "job1 summary"
    return render(request, "jobs/home.html", {"jobs": jobs})


def blog(request):
    return render(request, "jobs/blog.html")
