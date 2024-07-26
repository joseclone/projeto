from django.contrib import admin
from .models import *

# Register your models here.
# class Produtos(admin.ModelAdmin):
#      list_display = ("nomesDosModels")

admin.site.register(Produto)
