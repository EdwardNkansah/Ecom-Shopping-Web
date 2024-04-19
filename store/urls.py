from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('display_all/', views.display_all, name="display_all"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('customer/', views.customer, name="customer"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('search/', views.search, name='search'),
    # your other URL patterns
]