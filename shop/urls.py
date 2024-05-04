from django.urls import path
from .views import product_list, product_detail
from .views import create, update, delete
from .views import category_filter
from .views import signup, user_login
from .views import ProductListView,ProductDetailView

urlpatterns=[
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/<slug:slug>/',ProductDetailView.as_view() , name='product_detail'),

    path('products/create/', create, name='create'),
    path('products/<int:pk>/update/', update, name='update'),
    path('products/<int:pk>/delete/', delete, name='delete'),
    path('products/category/<int:pk>/', category_filter, name='category'),
    
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
]