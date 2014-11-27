# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
# from django.contrib.auth.models import User


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

    class Meta:
        pass

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

    publisher = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    year = models.IntegerField(
        null=True,
        blank=True,
    )

    language = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    authors = models.ManyToManyField(Author)
#    owner = models.ForeignKey(User)

    created = models.DateTimeField("date/time created", auto_now_add=True)
    modified = models.DateTimeField("date/time modified", auto_now=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Book)
def pre_save_books(instance, **kwargs):
    if instance.language is not None:
        instance.language = instance.language.lower()
