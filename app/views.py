from django.shortcuts import render

# Create your views here.
def games(request):
    return render(request,'pc_games.html')