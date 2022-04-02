from django.db import models


class Resume(models.Model):
    class Meta:
        db_table = 'Таблица'
        verbose_name = 'Резюме'
        verbose_name_plural = 'Таблицы'

    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Просто текст')
    slug = models.SlugField( unique= True, verbose_name='Slag')

    def __str__ (self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=20)
    lol = models.ManyToManyField(Resume)

    def __str__(self):
        return self.title