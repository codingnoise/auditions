from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm
import uuid


# Code convetion: All table names are singular
"""
    Descripton: Contains all movies
"""
class Movie(models.Model):
    movie_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie_title = models.CharField(max_length=250)
    movie_genre = models.CharField(max_length=100)
    movie_description = models.CharField(max_length=1000, default="No Description")
    #movie_duration = models.DurationField()
    #movie_timestamp = models.DateTimeField()
    #movie_link = models.TextField()
    #movie_thumbnail = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.movie_title

class CreateMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["movie_title", "movie_genre", "movie_description"]


