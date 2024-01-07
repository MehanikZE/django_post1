from django.db import models

# Create your models here.

class Author_of_post(models.Model):
    name = models.CharField(max_length=30)
    family = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    # def __str__(self):
    #     return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media/', null=True)
    author = models.ForeignKey(Author_of_post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now_add=True)
        # def __str__(self):
        # return self.title


class Category(models.Model):
    technology = models.CharField(max_length=50, name='Категория')
    # politics = models.CharField(max_length=50, name='Политика')
    # other = models.CharField(max_length=50, name='Прочее')
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField(max_length=500)
    comments = models.ForeignKey(Post, on_delete=models.CASCADE)