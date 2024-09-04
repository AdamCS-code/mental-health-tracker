from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306227160',
        'name': 'Adam Caldipawell Sembiring',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
