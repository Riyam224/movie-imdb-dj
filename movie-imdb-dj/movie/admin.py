from django.contrib import admin

# Register your models here.

from .models import Movie , DownloadLink , WatchedLink

admin.site.register(Movie)
admin.site.register(DownloadLink)
admin.site.register(WatchedLink)