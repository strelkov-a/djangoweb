from django.db import models
from django.core.urlresolvers import reverse
from .my_validators import name_and_slug_validator
from .my_validators import interf_capacity_validator

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя', validators=[interf_capacity_validator()])
    slug = models.SlugField(max_length=200, db_index=True, unique=True, validators=[name_and_slug_validator()])

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __init__(self, *args, **kwargs): # Конструктор, наследующийся от родительского класса.
        super().__init__(*args, **kwargs) # Супер - наследование от родительского класса
        # селф - обьект сам на себя. аргс - множество переменных, что передаются в функцию и возвращаются в видде кортежа
        # кваргс - именованные переменные возвращаемые в виде словаря.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('selecter:ProductListByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название", validators=[name_and_slug_validator()])
    slug = models.SlugField(max_length=200, db_index=True, validators=[name_and_slug_validator()])
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    interface = models.CharField(max_length=30, db_index=True, verbose_name="Интерфейс", validators=[interf_capacity_validator()])
    capacity = models.CharField(max_length=30, db_index=True, verbose_name="Объём", validators=[interf_capacity_validator()])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('selecter:Product.Detail', args=[self.id, self.slug])