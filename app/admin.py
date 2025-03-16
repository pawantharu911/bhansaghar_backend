from django.contrib import admin
from app.models import (Banner, Customer, Food, FoodCategory, Notification, Order, OrderItem,
    OrganizationSettings, Rating, Restaurant)

# Register your models here.
@admin.register(OrganizationSettings)
class OrganizationSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'currency')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'restaurant', 'category', 'type')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'photo', 'is_active')

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('customer', 'status', 'address', 'destination_phone_number', 'sub_total', 'delivery_charge', 'total',)
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'food', 'rating', 'review', 'is_active')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'url')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'image')