from django.db import models

# Create your models here.

# Create a model which contains a string field which have text field and to field which have char field and fromm field which have char field
class order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)

