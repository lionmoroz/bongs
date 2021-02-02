from django.db import models

# Create your models here.



class AboutUs (models.Model):
    tittle = models.CharField(max_length=250, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")
    photo = models.ImageField(verbose_name="Главное фото", upload_to='media', blank=True, null=True)

class Benefits(models.Model):
    benefits_title = models.CharField(max_length=250,verbose_name="Преимущества-заголовок")
    benefits_description = models.TextField(verbose_name="Преимущества-описание")


class Contact(models.Model):
    short_about = models.TextField(verbose_name="Краткое описание", blank=True, null=True)
    adress = models.CharField(verbose_name="Адрес", max_length=250, blank=True, null=True)
    phone_one = models.CharField(verbose_name="Телефон 1", max_length=250, blank=True, null=True)
    phone_two = models.CharField(verbose_name="Телефон 2", max_length=250, blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)


class Sale(models.Model):
    tittle = models.CharField(max_length=200, verbose_name="Акции" )


class ContactModel(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=254)
    question = models.TextField(verbose_name="Описание вопроса")