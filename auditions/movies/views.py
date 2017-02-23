from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the movies app homepage </h1>")