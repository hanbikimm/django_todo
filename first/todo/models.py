from django.db import models

# Create your models here.
class Todo(models.Model):
    #id는 auto니까 생략 가능!
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=200)
    todo_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
