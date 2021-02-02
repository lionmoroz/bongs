from .views import  product_list, product_detail
from django.urls import path
# product_detail,
app_name = 'shop'
urlpatterns = [
    path('', product_list, name='product_list' ),
    # path('list2/' , product_list_2, name='product_list_2'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<slug:slug>/<int:id>/', product_detail,  name='product_detail', ),
]