from django.shortcuts import render

# Create your views here.


def ResumePage(request):
    return render(request, "resume.html")