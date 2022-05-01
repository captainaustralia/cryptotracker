from django.db import models
from core.models import User, Portfolio


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

    date = models.DateTimeField(
        auto_now=True
    )

    likes = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.owner.email


class Comment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    text = models.CharField(
        max_length=200,
        blank=False
    )
    image = models.ImageField(
        upload_to='',
        blank=True,
        null=True
    )
    likes = models.PositiveIntegerField(
        default=0,
    )

    date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.owner
