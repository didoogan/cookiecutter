from django.db import models


class Representable(models.Model):

    def __str__(self):
        attrs = ((k, self.__dict__[k]) for k in self.__dict__ if not k.startswith('_'))
        return '{} = > {}'.format(self.__class__, str(list(attrs)))

    class Meta:
        abstract = True
