from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    picture = models.ImageField(default='default.png', blank=True, upload_to='chapters/%Y/%m/%D')
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug,
                             ])


class CV(models.Model):
    picture = models.ImageField(default='default.png', blank=True, upload_to='chapters/CVFace')
    name_surname = models.CharField(max_length=50)
    born_date = models.CharField(max_length=50)
    adress = models.CharField(max_length=150)
    post_office_code = models.CharField(max_length=150)
    email = models.CharField(max_length=50)

    experience = models.TextField(null=True, blank=True)
    education = models.TextField()
    language = models.TextField(null=True, blank=True)
    more_education = models.TextField(null=True, blank=True)

    skills = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)

    links = models.FileField(null=True)


class AboutMe(models.Model):
    picture = models.ImageField(upload_to='chapters/CVFace')
    about = RichTextField()
