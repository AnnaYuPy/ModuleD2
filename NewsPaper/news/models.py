from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

class Author(models.Model):
    author_name = models.OneToOneField(User, on_delete = models.CASCADE)
    author_rating = models.IntegerField(default = 0)

    def update_rating(self):
        return self.author_rating


class Categories(models.Model):
    politics = 'PL'
    sport = 'SP'
    education = 'ED'
    science = 'SC'
    general = 'GN'

    AREAS = [
        (politics, 'Politics'),
        (sport, 'Sport'),
        (education, 'Education'),
        (science, 'Science'),
        (general, 'General')
    ]

    category_name = models.CharField(max_length = 2, choices = AREAS, default = general, unique = True)

class Post(models.Model):

    article = 'AR'
    news = 'NW'

    TYPE = [
        (article, 'Article'),
        (news, 'News'),
    ]

    author_id = models.ForeignKey(Author, on_delete = models.CASCADE)
    post_type = models.CharField(max_length = 2, choices = TYPE)
    category_id = models.ManyToManyField(Categories, through = 'PostCategory')
    post_title = models.CharField(max_length = 64, default = 'No title')
    post_text = models.TextField(default = 'Tra-la-la')
    post_rating = models.IntegerField(default = 0)
    post_date = models.DateField(auto_now_add = True)

    def like(self):
        self.post_rating += 1

    def dislike(self):
        self.post_rating -= 1

    def preview(self):
        return self.post_text[:124] + '...'


class PostCategory(models.Model): # наследуемся от класса Model
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)

class Comment(models.Model): # наследуемся от класса Model
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment_text = models.TextField(default = "Tra-la-la")
    comment_date = models.DateField(auto_now_add = True)
    comment_rating = models.IntegerField(default = 0)

    def like(self):
        self.comment_rating += 1

    def dislike(self):
        self.comment_rating -= 1
