from django.contrib import admin
from users.models import User_profile

# Register your models here.






@admin.register(User_profile)   # Nueva forma de registrarlo 
class User_profileAdmin(admin.ModelAdmin):  # forma para que te muestre lo que quieras en el admin site 
    list_display = ["user", "phone", "image"] 
