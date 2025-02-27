from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="category name"
    )
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="product name"
    )
    price = models.CharField(max_length=50,)
    description = models.CharField(
        max_length=255,
        help_text="description"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    link = models.URLField()
    url = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name
