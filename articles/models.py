from django.db import models


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    published = models.DateTimeField()
    mainImage = models.ImageField(upload_to='images/')
    yourArticleContent = models.TextField(blank=True)
    summary = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class ExtraContent(models.Model):
    welcome = models.CharField(max_length=200)
    headerImage = models.ImageField(upload_to='images/', blank=True)
    profileImage = models.ImageField(upload_to='images/')
    welcomeMessage = models.TextField(blank=True)
    profileText = models.TextField(blank=True)
    aboutMessage = models.TextField(blank=True)
    contactMeMessage = models.TextField(blank=True)
