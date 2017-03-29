from django.db import models

from utility.model_mixins import Representable


class CheckModel(Representable):
    str_null = models.CharField(max_length=30, null=True)
    str_null_blank = models.CharField(max_length=30, null=True, blank=True)
    int_null = models.IntegerField(null=True)
    int_null_blank = models.IntegerField(null=True, blank=True)
    int_blank = models.IntegerField(blank=True, default=None)
