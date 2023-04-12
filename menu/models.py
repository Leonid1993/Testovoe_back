from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок меню')
    parent_id = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['title']
