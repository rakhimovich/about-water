from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    description = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации',auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
