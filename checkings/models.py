from django.db import models


class Representable(models.Model):

    def __str__(self):
        attrs = ((k, self.__dict__[k]) for k in self.__dict__ if not k.startswith('_'))
        return '{} = > {}'.format(self.__class__, str(list(attrs)))

    class Meta:
        abstract = True


class CheckModel(Representable):
    str_null = models.CharField(max_length=30, null=True)
    str_null_blank = models.CharField(max_length=30, null=True, blank=True)
    int_null = models.IntegerField(null=True)
    int_null_blank = models.IntegerField(null=True, blank=True)
    int_blank = models.IntegerField(blank=True, default=None)
