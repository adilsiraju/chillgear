from django.db import models
from  customers.models import Customer
from products.models import Product

# Create your models here.

class Order(models.Model):
    # Status
    LIVE = 1
    DELETE = 0

    DELETE_STATUS = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )

    CART_STAGE = 0
    ORDER_CONFIRM = 1
    ORDER_PROCESS = 2
    ORDER_DISPATCH = 3
    ORDER_DELIVERED = 4
    ORDER_CANCEL = 5

    status_choices = (

        (CART_STAGE, 'Cart Stage'),
        (ORDER_CONFIRM, 'Order Confirm'),
        (ORDER_PROCESS, 'Order Process'),
        (ORDER_DISPATCH, 'Order Dispatch'),
        (ORDER_DELIVERED, 'Order Delivered'),
        (ORDER_CANCEL, 'Order Cancel')
    )

    owner = models.ForeignKey(Customer, related_name = 'orders', on_delete=models.CASCADE, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    order_status = models.IntegerField(choices=status_choices, default=CART_STAGE)

    delete_status = models.IntegerField(choices=DELETE_STATUS, default=LIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'FS-{self.id}'

class OrderItem(models.Model):

    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, related_name='added_items', on_delete=models.CASCADE)