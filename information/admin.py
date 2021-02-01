from django.contrib import admin
from .models import AboutUs, Benefits, Contact, ContactModel, Sale
# Register your models here.

admin.site.register(AboutUs)
admin.site.register(Sale)
admin.site.register(Benefits)
admin.site.register(ContactModel)
admin.site.register(Contact)

