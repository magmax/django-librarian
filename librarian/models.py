# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


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

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return '{surname}, {name}'.format(**self.__dict__)

    def __str__(self):
        return self.__unicode__()


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

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField("date/time created", auto_now_add=True)
    modified = models.DateTimeField("date/time modified", auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()


@receiver(pre_save, sender=Book)
def pre_save_books(instance, **kwargs):
    if instance.language is not None:
        instance.language = instance.language.lower()
