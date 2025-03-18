from django.db import models

# Create your models here.

class Product(models.Model):

    # Status
    LIVE = 1
    DELETE = 0

    DELETE_STATUS = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )

    # Fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    Size = models.ForeignKey('Size', on_delete=models.CASCADE)

    priority = models.IntegerField(default=0)

    delete_status = models.IntegerField(choices=DELETE_STATUS, default=LIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    
    nameOfCategory = models.CharField(max_length=200)

    def __str__(self):
        return self.nameOfCategory
    
class Size(models.Model):
    
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.size