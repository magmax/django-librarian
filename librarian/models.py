from django.db import models


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
