from django.db import models
from django.urls import reverse
# Create your models here.

LABEL_CHOICES = (
    ('N', 'new'),
    ('S', 'sale'),

)

class Category(models.Model):

   

    name = models.CharField(verbose_name="Название", max_length=120, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    is_active = models.BooleanField(verbose_name="категория активна", default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
    
    def image_directory_path(instance, filename):
        return 'category/{0}/{1}'.format(instance.slug, filename)

    image = models.ImageField(verbose_name="Главное фото", upload_to=image_directory_path, blank=True, null=True)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=120, db_index=True)
    description = models.TextField(verbose_name='Описание',)
    slug = models.SlugField(max_length=200, unique=True)
    def image_directory_path(instance, filename):
        return 'products/{0}/main_image/{1}'.format(instance.slug, filename)
    main_image = models.ImageField(verbose_name="Главное фото", upload_to=image_directory_path, blank=True, null=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True, null=True)
    old_price = models.DecimalField(verbose_name="Старая цена", max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(verbose_name="В наличии", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    

    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug, self.id ])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    def image_directory_path(instance, filename):
        return 'products/{0}/seconds_image/{1}/{2}'.format(instance.product.slug, instance.title ,filename)
    seconds_image = models.ImageField(verbose_name="Другие фото", upload_to=image_directory_path, 
    blank=True, null=True)

    def __str__(self):
        return self.title


