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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Movie, CreateMovieForm
from django.views.generic import View
from .forms import UserForm
import logging

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


class MoviePlayView(generic.DetailView):
    template_name = "movies/movie_player.html"
    model = Movie

    def get_queryset(self):
        return Movie.objects.all()


class MovieCreateView(CreateView):
    model = Movie
    form_class = CreateMovieForm


class MovieUpdateView(UpdateView):
    model = Movie
    form_class = CreateMovieForm


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("movies:index")


class UserFormView(View):
    form_class = UserForm
    template_name = "movies/registration_form.html"

    # display blank form
    def get(self, request):
        # Context is None - by default it doesn't have any data.
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    # process form data
    def post(self, request):
        print "In POST..."
        form = self.form_class(request.POST)

        if form.is_valid():
            print "form is valid..."
            # Creates a user obj but doesn't save in the database
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user:
                print "Checking if user not none..."
                if user.is_active:
                    logging.info("User is active...")
                    login(request, user)
            return redirect("movies:index")

        # if not valid, they'll be redirected to blank form
        return render(request, self.template_name, {"form": form})