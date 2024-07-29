from django.db import models
from django.utils.translation import gettext_lazy as _


class Ad(models.Model):
    """
    Ad model.
    """
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title'),
    )
    ad_id = models.PositiveIntegerField(
        primary_key=True,
        unique=True,
        verbose_name=_('ID'),
    )
    author = models.CharField(
        max_length=50,
        verbose_name=_('Author'),
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Views'),
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Position'),
    )

    def __str__(self):
        return f'{self.title} - {self.ad_id}: {self.author}'

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')
