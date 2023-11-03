from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        if self.id:
            return f'Name: name: {self.name}, email: {self.email}'
        return 'None'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.BooleanField()

    def __str__(self):
        if self.id:
            return f'Title is {self.title}'