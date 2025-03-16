from django.db import models
# Create your models here.
class OrganizationSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True, default='Rs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FoodCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    type_options ={
        ('veg', 'Veg'),
        ('non-veg', 'Non-Veg'),
    }
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=255, choices=type_options, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='customers/', null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, unique= True)
    otp = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    status_options = {
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('on the way', 'On The Way'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    }
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, choices=status_options, default="pending")
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitute = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    destination_phone_number = models.CharField(max_length=255, unique= True)
    sub_total = models.CharField(max_length=255, default=0)
    delivery_charge = models.CharField(max_length=255, default=0)
    total = models.CharField(max_length=255, default=0)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    price = models.CharField(max_length=255, default=0)

    def __str__(self):
        return self.id

class Rating(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='notifications/', null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Banner(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='banners/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

