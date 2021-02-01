from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=70, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active =models.BooleanField()
    number = models.IntegerField(default=0)
    max_discount = models.DecimalField(default=100 , max_digits=6 , decimal_places=2) 
    user = models.ManyToManyField(User , related_name='coupons' , blank=True)

    def __str__(self):
        return self.code

