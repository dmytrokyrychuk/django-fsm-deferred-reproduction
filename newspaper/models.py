from django.db import models
from django_fsm import FSMField


class Article(models.Model):
    author_name = models.CharField(max_length=73)
    large_content = models.TextField()
    state = FSMField(default="draft")
