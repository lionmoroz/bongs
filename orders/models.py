from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon
from shop.models import Product
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
from novaposhta.models import Area, Warehouse, City
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Order (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    message = models.CharField(verbose_name='Message', max_length=250, blank=True)
    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        verbose_name=_('Area'),
        blank=True,
        null=True,
    )

    nova_city = ChainedForeignKey(
        City,
        chained_field="area",
        chained_model_field="area_id",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name=_('Nova Poshta City'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    nova_warehouse = ChainedForeignKey(
        Warehouse,
        chained_field="nova_city",
        chained_model_field="city_id",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name=_('Nova Poshta Warehouse'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.item.all())
        return total_cost - total_cost * \
            (self.discount/Decimal(100))
            
    def get_subtotal_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)
    
    def get_cost(self):
        return self.price * self.quantity


