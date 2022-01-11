from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.utils.text import slugify

CATEGORY_CHOICES = ( 
    ('action'  , 'ACTION'),
    ('drama' , 'DRAMA'),
    ('romance', 'ROMANCE'),
    ('comedy' , 'COMEDY')
)

LANGUNAGE_CHOICES = (
    ('english' , 'ENGLISH'),
    ('korean' , 'KOREAN'),
  
)

STATUS_CHOICES = (
    ('RA' , 'recently added'),
    ('MW' , 'most watched'),
    ('TR' , 'top rated')
)

class Movie(models.Model):

    title = models.CharField(_("title"), max_length=50)
    description  = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to='movie', blank=True , null=True)
    banner = models.ImageField(_("banner"), upload_to='movie_banner',  blank=True , null=True)
    category = models.CharField(_("category"), choices=CATEGORY_CHOICES,  max_length=50)
    language = models.CharField(_("language"), choices=LANGUNAGE_CHOICES , max_length=30)
    status = models.CharField(_("status"), choices=STATUS_CHOICES  , max_length=30)
    year_of_production  = models.DateTimeField(_("year of production"),auto_now_add=False)
    cast = models.CharField(_("cast"), max_length=50)
    views_count = models.IntegerField(_("views count ") , default=0)
    slug = models.SlugField(_("slug") , null=True , blank=True)
    trailer = models.URLField(_("movie trailer"), max_length=200)
 

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Movie , self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("movie:MovieDetail", kwargs={"pk": self.pk})





class WatchedLink(models.Model):
    movie = models.ForeignKey(Movie, verbose_name=_("movie"), on_delete=models.CASCADE)
    links = models.URLField(_("links"), max_length=200)

    class Meta:
        verbose_name = _("WatchedLink")
        verbose_name_plural = _("WatchedLinks")

    def __str__(self):
        return str(self.movie.title)



class DownloadLink(models.Model):
    movie = models.ForeignKey(Movie, verbose_name=_("movie"), on_delete=models.CASCADE)
    links = models.URLField(_("links"), max_length=200)

    class Meta:
        verbose_name = _("DownloadLink")
        verbose_name_plural = _("DownloadLinks")

    def __str__(self):
        return str(self.movie.title)


