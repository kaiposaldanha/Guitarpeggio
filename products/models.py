from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=64, default="Intrument")
    imagem = models.ImageField(upload_to="products/")
    
    def __str__(self):
        return f"{self.id}: {self.name} {self.price}"

class Carrinho(models.Model):
    pass

class ItemCarrinho(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()