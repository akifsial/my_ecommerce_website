import datetime
from django.db import models

# Create your models here.

# model for category
class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


# model for product
class Product(models.Model):
  name = models.CharField(max_length=500)
  price = models.IntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
  description = models.CharField(max_length=200, default="", blank=True)
  image = models.ImageField(upload_to="products_images/")

  staticmethod
  def get_products_by_id(ids):
    return Product.objects.filter(id__in =ids)
  
  def __str__(self):
    return self.name
  
  

# model for order
class Order(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  customer = models.CharField(max_length=50)
  quantity = models.IntegerField(default=1)
  price = models.IntegerField()
  address = models.CharField(max_length=50, default="", blank=True)
  phone = models.CharField(max_length=50, default="", blank=True)
  date = models.DateField(default=datetime.datetime.today)
  status = models.BooleanField(default=False)

  def __str__(self):
    return self.customer

  def placeOrder(self):
    self.save()
  