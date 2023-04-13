from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок меню')
    parent_id = models.IntegerField(null=True, default=None)
    url = models.SlugField()
    branch = models.IntegerField(default=0, verbose_name='Ветка меню')
    level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.parent_id:
            self.level = Menu.objects.get(pk=self.parent_id).level + 1
        else:
            self.level = 0
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['level', 'branch', 'title']
