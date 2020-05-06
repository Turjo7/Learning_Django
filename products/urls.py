from django.urls import path
from . import views # from the current folder inport the views

# /products
# /products/1/detail
# /products/new

#views.index sending reference
urlpatterns =[
    path('',views.index),
    path('new',views.new)

]
