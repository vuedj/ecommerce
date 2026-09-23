from django.contrib import admin

from .models import Category, Order, OrderItem, Product, UserProfile

admin.site.register([Category, Order, OrderItem, Product, UserProfile])
