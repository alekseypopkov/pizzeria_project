from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Тема, которую изучает пользователь."""
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.name


class Topping(models.Model):
    """Информация, изученная пользователем по теме."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Начинка'
        verbose_name_plural = 'Начинка'
        
    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.name}"