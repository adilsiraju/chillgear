from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    # Status
    LIVE = 1
    DELETE = 0

    DELETE_STATUS = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )

    # Fields
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    # Foreign Key to User
    # related_name is used to access the Customer object from User object
    # on_delete=models.CASCADE is used to delete the Customer object when the User object is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')

    delete_status = models.IntegerField(choices=DELETE_STATUS, default=LIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name