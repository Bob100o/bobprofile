from django.shortcuts import render

# Create your views here.
def learnmore(request):
    return render(request,'learnmore/learnmore.html')
