from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("instruments/", views.instruments, name="instruments"),
    path("whoweare/", views.instruments, name="whoweare"),
    path("guitarists/", views.guitarists, name="guitarists"),
    path("about/", views.about, name="about"),
    path("cart/", views.cart, name = "cart"), 
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
