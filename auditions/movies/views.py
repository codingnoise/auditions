# from django.http.response import Http404
# # from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# # from django.template import loader
# from .models import Movie
#
# MOVIES_INDEX_TEMPLATE = "movies/index.html"
# MOVIES_DETAIL_TEMPLATE = "movies/detail.html"
#
# def index(request):
#     all_movies = Movie.objects.all()
#     #template = loader.get_template(MOVIES_INDEX_TEMPLATE)
#     context = {"all_movies": all_movies}
#     return render(request=request, template_name=MOVIES_INDEX_TEMPLATE, context=context)
#     #return HttpResponse(template.render(context, request))
#
#
# def detail(request, movie_id):
#     try:
#         movie = Movie.objects.get(pk=movie_id)
#     except (Movie.DoesNotExist, ValueError):
#         raise Http404("Movie does not exist")
#
#     #movie = get_object_or_404(Movie, pk=movie_id)
#
#     context = {"movie": movie}
#     return render(request=request, template_name=MOVIES_DETAIL_TEMPLATE, context=context)


from django.views import generic
from .models import Movie


class IndexView(generic.ListView):
    template_name = "movies/index.html"
    context_object_name = "all_movies"
    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic.DetailView):
    template_name = "movies/detail.html"

    model = Movie
    def get_queryset(self):
        return Movie.objects.all()
