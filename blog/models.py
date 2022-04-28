from django.db import models
from core.models import User, Portfolio


class Comment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=200
    )
    image = models.ImageField(
        upload_to='',
        blank=True,
        null=True
    )
    likes = models.PositiveIntegerField()

    date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.owner


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField(
        max_length=300
    )

    image = models.ImageField(
        upload_to='',
        blank=True,
        null=True
    )

    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    comments = models.ManyToManyField(
        Comment,
        blank=True
    )

    date = models.DateTimeField(
        auto_now=True
    )

    likes = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.owner.email
