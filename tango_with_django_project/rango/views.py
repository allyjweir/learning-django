from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to Rango</h1> <br> hello world")

def about(request):
    return HttpResponse("<h3>This is Rango's about page.</h3>")
