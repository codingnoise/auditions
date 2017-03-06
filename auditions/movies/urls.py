from django.conf.urls import url
from . import views

app_name = "movies"

# urlpatterns = [
#     # /movies/
#     url(r"^$", views.index, name="index"),
#     # /movies/<id>
#     url(r"^(?P<movie_id>[^/]+)/$", views.detail, name="detail"),
# ]

urlpatterns = [
    # /movies/
    url(r"^$", views.IndexView.as_view(), name="index"),

    # /movies/<id>
    url(r"^(?P<pk>[^/]+)/$", views.DetailView.as_view(), name="detail"),

    # /movies/upload
    url(r"/upload/$", views.MovieCreateView.as_view(), name="movie-upload"),

    # /update/<id>/
    url(r"/update/(?P<pk>[^/]+)/$", views.MovieUpdateView.as_view(), name="movie-update"),

    # /delete/<id>/
    url(r"/delete/(?P<pk>[^/]+)$", views.MovieDeleteView.as_view(), name="movie-delete")
]