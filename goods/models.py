from tabnanny import verbose
from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='alias')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
        
class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='alias')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в процентах')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория') # PROTECT чтобы запретить удалить, CASCADE все записи категории сгинут. Так что на боевом его не ставь
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'  
        ordering = ('id',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug}) # product_slug из urls.py
    
    
    def display_id(self):
        return f"{self.id:05}" # 00007 добавление 0
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        
        return self.price
    