from django.db import models


class Author(models.Model):

    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    surname = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    def __str__(self):
        return '{surname}, {name}'.format(**self.__dict__)


class Book(models.Model):

    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=600,
        null=True,
        blank=True,
    )

    isbn_13 = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
